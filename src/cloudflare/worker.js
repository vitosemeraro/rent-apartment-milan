// RAM – rent-apartment-milan.com su Cloudflare Workers (file statici + piccole funzioni).
// Sostituisce .htaccess, contact.php, availability.php, ev.php ed ev-stats.php del vecchio hosting Netsons.
// Segreti e binding (impostati su Cloudflare, mai nel repository):
//   ICS_JSON  secret  {"mm":"https://www.airbnb.it/calendar/ical/…", …}   URL iCal privati di Airbnb
//   EMAIL     send_email                                                 invio delle richieste a Gmail
//   DB        D1 "ram-events"                                            registro eventi anonimo
//   ASSETS    file statici del sito

const SITE = 'https://rent-apartment-milan.com';
const FROM = 'hello@rent-apartment-milan.com';
const TO = 'vsemeraro@gmail.com';

// ---------- redirect dal vecchio WordPress (stesse regole del vecchio .htaccess) ----------
const R301 = [
  [/^\/about-ram\/?$/, '/about/'],
  [/^\/pages\/our-staff\/?$/, '/about/'],
  [/^\/accommodation\/authentic-milanese-studio\/?$/, '/apartments/studio-turro-martesana/'],
  [/^\/available-offer\/?$/, '/apartments-milan-no-deposit/'],
  [/^\/accommodation\/cozy-two-room-apartment\/?$/, '/apartments/one-bedroom-val-di-non-balcony/'],
  [/^\/(accommodation|accommodation-category|apartments-available|availability-search)(\/.*)?$/, '/apartments/'],
  [/^\/dsads\/?$/, '/long-term-flat-rentals-in-milan/'],
  [/^\/pages\/faq\/?$/, '/faq/'],
  [/^\/pages\/our-reviews\/?$/, '/reviews/'],
  [/^\/pages\/whats-nearby\/?$/, '/precotto-turro-martesana-neighbourhood-guide/'],
  [/^\/home\/contact-us\/?$/, '/contact/'],
  [/^\/booking-confirmation\/terms-conditions\/?$/, '/privacy/'],
  [/^\/booking-confirmation(\/.*)?$/, '/contact/'],
  [/^\/blog\/blog-style[^/]*\/?$/, '/blog/'],
  [/^\/category(\/.*)?$/, '/blog/'],
  [/^\/(home|home-3|home-4|pages|pages\/gallery|pages\/offers)\/?$/, '/'],
];
const GONE = [
  /^\/(feed|comments\/feed|wp-json|xmlrpc\.php|wp-login\.php|wp-admin|wp-includes)(\/.*)?$/,
  /^\/wp-content\/.*$/,
  /^\/(tiny-homes|services|shop|my-account|sample-page|elementor-thhf|author|pages\/covid-19)(\/.*)?$/,
];
const SECURITY = {
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'X-Frame-Options': 'SAMEORIGIN',
  'Strict-Transport-Security': 'max-age=31536000',
};

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);
    // dominio canonico senza www (http->https lo fa Cloudflare con "Always Use HTTPS")
    if (url.hostname === 'www.rent-apartment-milan.com' || (url.protocol === 'http:' && url.hostname === 'rent-apartment-milan.com')) {
      return Response.redirect(SITE + url.pathname + url.search, 301);
    }
    const p = url.pathname;
    if (p === '/contact.php') return contact(req, env);
    if (p === '/availability.php') return availability(url, env, ctx);
    if (p === '/ev.php') return ev(req, env, ctx);
    if (p === '/ev-stats.php') return evStats(url, env);
    if (p.endsWith('.php') || p === '/wp-config.php') return gone(req, env);

    if (p === '/' && /(^|&)(p|page_id|attachment_id|cat|author)=[0-9]+/i.test(url.search.slice(1))) {
      return Response.redirect(SITE + '/', 301);
    }
    for (const [re, to] of R301) if (re.test(p)) return Response.redirect(SITE + to, 301);
    for (const re of GONE) if (re.test(p)) return gone(req, env);

    const res = await env.ASSETS.fetch(req);
    // "/pagina" -> "/pagina/": redirect permanente (gli asset rispondono 307)
    if (res.status === 307 && res.headers.get('Location')) {
      return Response.redirect(new URL(res.headers.get('Location'), SITE).toString().replace(url.origin, SITE), 301);
    }
    return withHeaders(res, p);
  },
};

function withHeaders(res, p) {
  const r = new Response(res.body, res);
  for (const [k, v] of Object.entries(SECURITY)) r.headers.set(k, v);
  if (/\.(webp|jpe?g|png|ico)$/i.test(p)) r.headers.set('Cache-Control', 'public, max-age=31536000, immutable');
  else if ((r.headers.get('Content-Type') || '').includes('text/html')) r.headers.set('Cache-Control', 'public, max-age=3600');
  return r;
}

async function gone(req, env) {
  const nf = await env.ASSETS.fetch(new Request(SITE + '/404.html'));
  const r = new Response(nf.body, { status: 410, headers: { 'Content-Type': 'text/html; charset=utf-8' } });
  for (const [k, v] of Object.entries(SECURITY)) r.headers.set(k, v);
  return r;
}

const see = (to) => new Response(null, { status: 303, headers: { Location: to } });

// ---------- modulo contatti / richieste di prenotazione ----------
const THANKS = { en: '/thank-you/', it: '/it/grazie/', es: '/es/gracias/', fr: '/fr/merci/', de: '/de/danke/' };
const NAMES = { mm: 'Casa comfort Precotto (MM)', pa: 'Design Precotto (PA)', turro: 'Monolocale Turro', vdn: 'Bilocale Val di Non' };

async function contact(req, env) {
  if (req.method !== 'POST') return see('/');
  let fd;
  try { fd = await req.formData(); } catch { return see('/'); }
  const f = (k, n = 2000) => String(fd.get(k) || '').replace(/<[^>]*>/g, '').slice(0, n).trim();
  if (f('website')) return see('/'); // honeypot
  const lang = THANKS[f('lang', 2)] ? f('lang', 2) : 'en';
  const email = f('email', 200);
  const emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  const booking = f('kind', 10) === 'booking';
  const name = f('name', 120).replace(/[\r\n]+/g, ' ');
  if (!emailOk || !name || (!booking && !f('message'))) return see(lang === 'en' ? '/contact/' : `/${lang}/`);
  const apt = f('apt', 20);
  const aptName = NAMES[apt] || apt || '-';
  const din = f('checkin', 12) || f('checkin_ns', 12);
  const dout = f('checkout', 12) || f('checkout_ns', 12);
  const guests = booking ? `${f('adults', 2)} adulti + ${f('children', 2)} bambini` : f('guests', 3);
  const ip = req.headers.get('CF-Connecting-IP') || '';
  const body = (booking ? 'RICHIESTA DI PRENOTAZIONE' : 'Nuova richiesta') + ' dal sito rent-apartment-milan.com\n\n'
    + `Nome: ${name}\nEmail: ${email}\nLingua: ${lang}\nAppartamento: ${aptName}\nArrivo: ${din}\nPartenza: ${dout}\nOspiti: ${guests}`
    + (booking ? "\n\nPreventivo mostrato all'ospite:\n" + f('quote', 1500).split(' | ').join('\n') : '\nMotivo: ' + f('reason', 80))
    + '\n\nMessaggio:\n' + (f('message') || '-')
    + "\n\nRispondi direttamente a questa email per scrivere all'ospite.\nIP: " + ip;
  // stessi criteri anti-spam del vecchio contact.php: l'oggetto cambia, il filtro Gmail evidenzia solo "[RAM richiesta]"
  const msg = f('message').toLowerCase();
  const spam = f('js', 1) !== '1'
    || /unsubscribe|opt out|opt-out|seo services|lead gen|free trial|backlink|our agency|web design|marketing services/.test(msg)
    || (msg.match(/https?:\/\//g) || []).length >= 2
    || (!booking && (!din || !dout));
  const subject = (spam ? '[RAM possibile spam] ' : '[RAM richiesta] ') + (booking ? `Prenotazione ${aptName} ` : '') + `${name} ${din}` + (dout ? ` - ${dout}` : '');
  try {
    await env.EMAIL.send({ to: TO, from: { email: FROM, name: 'RAM sito' }, replyTo: { email, name }, subject, text: body });
  } catch (e) {
    console.log('email error', e && e.code, e && e.message);
  }
  return see(THANKS[lang]);
}

// ---------- disponibilità dagli iCal Airbnb (solo intervalli occupati) ----------
async function availability(url, env, ctx) {
  const json = (o, s = 200) => new Response(JSON.stringify(o), { status: s, headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'public, max-age=600' } });
  let ics = {};
  try { ics = JSON.parse(env.ICS_JSON || '{}'); } catch {}
  const id = url.searchParams.get('apt') || '';
  if (!ics[id]) return json({ busy: [] }, 404);
  const cache = caches.default;
  const key = new Request(SITE + '/__ics_cache/' + id);
  const hit = await cache.match(key);
  if (hit) return json(await hit.json());
  let raw = '';
  try {
    const r = await fetch(ics[id], { headers: { 'User-Agent': 'RAM-site' }, cf: { cacheTtl: 0 } });
    if (r.ok) raw = await r.text();
  } catch {}
  if (!raw) return json({ busy: [] });
  const busy = [];
  const d = (s) => `${s.slice(0, 4)}-${s.slice(4, 6)}-${s.slice(6, 8)}`;
  for (const m of raw.matchAll(/DTSTART;VALUE=DATE:(\d{8})[\s\S]*?DTEND;VALUE=DATE:(\d{8})/g)) busy.push([d(m[1]), d(m[2])]);
  const out = { busy, updated: new Date().toISOString() };
  ctx.waitUntil(cache.put(key, new Response(JSON.stringify(out), { headers: { 'Cache-Control': 'max-age=1200' } })));
  return json(out);
}

// ---------- registro eventi anonimo (niente cookie, IP o user agent salvati) ----------
const EVENTS = ['view', 'read', 'link', 'out', 'cal', 'cal_nav', 'dates', 'guests', 'quote', 'booking_request', 'form_submit', 'gallery'];
async function ev(req, env, ctx) {
  const none = new Response(null, { status: 204, headers: { 'Cache-Control': 'no-store' } });
  if (req.method !== 'POST' || !env.DB) return none;
  if (/bot|crawl|spider|slurp|headless|lighthouse|preview/i.test(req.headers.get('User-Agent') || '')) return none;
  let j;
  try { j = JSON.parse((await req.text()).slice(0, 2000)); } catch { return none; }
  if (!j || !EVENTS.includes(j.e)) return none;
  const clean = (v, n) => String(v ?? '').replace(/[^A-Za-z0-9/\-_.:%]/g, '').slice(0, n);
  const p = clean(j.p, 160);
  if (!p.startsWith('/')) return none;
  const ts = new Date().toISOString().slice(0, 16).replace('T', ' ');
  ctx.waitUntil(env.DB.prepare('INSERT INTO events (ts, e, p, l, s, v) VALUES (?, ?, ?, ?, ?, ?)')
    .bind(ts, j.e, p, clean(j.l, 160), clean(j.s, 40), parseInt(j.v, 10) || 0).run().catch(() => {}));
  return none;
}

async function evStats(url, env) {
  const h = { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex' };
  const days = Math.max(1, Math.min(120, parseInt(url.searchParams.get('days') || '35', 10) || 35));
  const since = new Date(Date.now() - days * 86400000).toISOString().slice(0, 10);
  if (!env.DB) return new Response(JSON.stringify({ since, rows: [] }), { headers: h });
  const { results } = await env.DB.prepare(
    'SELECT substr(ts,1,10) AS day, e, p, l, s, COUNT(*) AS n, SUM(v) AS v FROM events WHERE ts >= ? GROUP BY day, e, p, l, s'
  ).bind(since).all();
  return new Response(JSON.stringify({ since, rows: results }), { headers: h });
}
