# Generatore del sito statico RAM: python build.py  ->  ../dist
import json, os, re, html, datetime, importlib, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "..", "dist")
from common import SITE, LANGS, LANG_NAMES, LISTINGS, CONFIG

IMAGES = json.load(open(os.path.join(HERE, "images.json"), encoding="utf8"))
REVIEWS = json.load(open(os.path.join(HERE, "data", "reviews.json"), encoding="utf8"))
CONFIG["reviews_count"] = CONFIG.get("reviews_total") or len(REVIEWS)
CSS = open(os.path.join(HERE, "site.css"), encoding="utf8").read()
import booking as BK
PRICING = json.load(open(os.path.join(HERE, "data", "pricing.json"), encoding="utf8"))
CSS = re.sub(r"\s*\n\s*", "", CSS)
C = {l: importlib.import_module("lang_" + l) for l in LANGS}
from nodeposit import D as _ND
from prices import D as _PD, SHORT as _PS
from mm_texts import M as _MM
import blog as BLOG
import aeo as AEO
from faq_pages import FAQ as _GFAQ
INDEXNOW_KEY = "7058b7a634092b9c7269dcca6835e7f9"
for _l in LANGS:
    C[_l].SLUG["nodeposit"] = _ND[_l][0]; C[_l].P["nodeposit"] = _ND[_l][1]; C[_l].SLUG["prices"] = _PD[_l][0]; C[_l].P["prices"] = _PD[_l][1]; C[_l].L["mm"].update(_MM[_l]); C[_l].SLUG["blog"] = "blog"; C[_l].P["blog"] = BLOG.INDEX[_l]
TODAY = datetime.date.today().isoformat()
esc = html.escape


def prefix(lang):
    return "" if lang == CONFIG["default_lang"] else lang + "/"


def path_of(lang, key):
    slug = C[lang].SLUG[key]
    p = prefix(lang) + (slug + "/" if slug else "")
    return "/" + p


def url_of(lang, key):
    return SITE + path_of(lang, key)


def img(set_, i=0, sizes="100vw", cls="", eager=False, alt=""):
    lst = IMAGES.get(set_) or IMAGES["valdinon"]
    m = lst[i % len(lst)]
    b = f"/img/{set_ if set_ in IMAGES else 'valdinon'}/{m['base']}"
    ws = [w for w in (480, 960, 1600) if w <= m["w"] or w == 480]
    srcset = ", ".join(f"{b}-{w}.webp {w}w" for w in ws)
    h = round(960 * m["h"] / m["w"])
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    return (f'<picture><source type="image/webp" srcset="{srcset}" sizes="{sizes}">'
            f'<img src="{b}.jpg" width="960" height="{h}" alt="{esc(alt)}" {load}{" class=%s" % cls if cls else ""}></picture>')


def img_src(set_, i=0, w=1600):
    lst = IMAGES.get(set_) or IMAGES["valdinon"]
    m = lst[i % len(lst)]
    return f"{SITE}/img/{set_ if set_ in IMAGES else 'valdinon'}/{m['base']}.jpg"


def stars(n=5):
    return "★" * n


def badge_sh(T):
    return f'<span class="badge sh"><i>◆</i> {T.ui["superhost"]}</span>' if CONFIG["superhost"] else ""


# ---------------------------------------------------------------- layout
def layout(lang, key, title, desc, body, ld=None, og_img=None, crumbs=None, robots="index,follow", xcss="", xjs="", canon=None):
    T = C[lang]
    if canon:  # articoli: URL proprio, hreflang solo sulla lingua dell'articolo
        alts = f'<link rel="alternate" hreflang="{lang}" href="{SITE}{canon}">'
    else:
        alts = "".join(f'<link rel="alternate" hreflang="{l}" href="{url_of(l, key)}">' for l in LANGS)
        alts += f'<link rel="alternate" hreflang="x-default" href="{url_of(CONFIG["default_lang"], key)}">'
    nav = ""
    for k in ("apartments", "monthly", "blog", "about", "reviews", "contact"):
        cur = ' aria-current="page"' if k == key else ""
        nav += f'<a href="{path_of(lang, k)}"{cur}>{esc(T.ui["nav_" + ("guides" if k == "blog" else k)])}</a>'
    langs = "".join(f'<li><a href="{path_of(l, "blog" if canon else key)}" hreflang="{l}" lang="{l}">{LANG_NAMES[l]}</a></li>' for l in LANGS)
    nav += f'<details class="lang"><summary aria-label="Language">🌐 {lang.upper()}</summary><ul>{langs}</ul></details>'
    ld_all = [{
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p}
                            for i, (n, p) in enumerate([(T.ui["home"], path_of(lang, "home"))] + (crumbs or []))]}]
    if ld:
        ld_all += ld if isinstance(ld, list) else [ld]
    crumb_html = ""
    if crumbs:
        parts = [f'<a href="{path_of(lang, "home")}">{esc(T.ui["home"])}</a>'] + [
            f'<a href="{p}">{esc(n)}</a>' if i < len(crumbs) - 1 else esc(n) for i, (n, p) in enumerate(crumbs)]
        crumb_html = f'<div class="wrap crumbs">{" › ".join(parts)}</div>'
    og = og_img or img_src("valdinon", 0)
    foot_apts = "".join(f'<li><a href="{path_of(lang, "l_" + lid)}">{esc(T.L[lid]["short"])}</a></li>' for lid in LISTINGS)
    foot_guides = "".join(f'<li><a href="{path_of(lang, k)}">{esc(T.P[k]["nav"])}</a></li>' for k in CONFIG["guides"])
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(desc)}"><meta name="robots" content="{robots}">
<link rel="canonical" href="{SITE + canon if canon else url_of(lang, key)}">{alts}
<meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{SITE + canon if canon else url_of(lang, key)}"><meta property="og:image" content="{og}"><meta property="og:locale" content="{T.LOCALE}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" href="/favicon.png" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="theme-color" content="#f7f3ee">
<style>{CSS}{xcss}</style>
<script type="application/ld+json">{json.dumps(ld_all, ensure_ascii=False)}</script>
</head><body><a class="skip" href="#main">{esc(T.ui["skip"])}</a>
<header class="top"><div class="wrap bar"><a class="logo" href="{path_of(lang, "home")}"><b>RAM</b><span>Rent Apartment Milan<small>{esc(T.ui["logo_sub"])}</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">☰ {esc(T.ui["menu"])}</button><nav class="main" id="nav">{nav}</nav></div></header>
{crumb_html}<main id="main">{body}</main>
<footer class="site"><div class="wrap"><div class="cols">
<div><a class="logo" href="{path_of(lang, "home")}" style="color:#fff"><b>RAM</b><span>Rent Apartment Milan</span></a><p style="margin-top:14px">{esc(T.ui["foot_about"])}</p><p><a href="mailto:{CONFIG["email"]}">{CONFIG["email"]}</a><br><a href="tel:{CONFIG["phone"].replace(" ", "")}">{CONFIG["phone"]}</a><br>{CONFIG["street"]}, {CONFIG["zip"]} Milano<br><a href="{CONFIG["same_as"][0]}" rel="noopener" target="_blank">Google Maps</a></p></div>
<div><p class="fh">{esc(T.ui["nav_apartments"])}</p><ul>{foot_apts}</ul></div>
<div><p class="fh">{esc(T.ui["nav_guides"])}</p><ul>{foot_guides}</ul></div>
<div><p class="fh">RAM</p><ul><li><a href="{path_of(lang, "about")}">{esc(T.ui["nav_about"])}</a></li><li><a href="{path_of(lang, "reviews")}">{esc(T.ui["nav_reviews"])}</a></li><li><a href="{path_of(lang, "faq")}">FAQ</a></li><li><a href="{path_of(lang, "contact")}">{esc(T.ui["nav_contact"])}</a></li><li><a href="{path_of(lang, "privacy")}">Privacy &amp; cookie</a></li></ul></div>
</div><div class="legal"><span>© {datetime.date.today().year} RAM · Rent Apartment Milan · Milano</span><span>{esc(T.ui["cin_note"])}</span></div></div></footer>
<div id="consent" role="dialog" aria-label="Cookie" aria-live="polite"><p>{T.ui["cookie_text"].replace("{privacy}", path_of(lang, "privacy"))}</p><button class="btn small" data-c="1">{esc(T.ui["cookie_ok"])}</button> <button class="btn small ghost" data-c="0">{esc(T.ui["cookie_no"])}</button></div>
<script>{JS}{xjs}</script><script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{{"token": "{CONFIG["cf_beacon"]}"}}'></script></body></html>"""


JS = """(function(){var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');b&&b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
var c=document.getElementById('consent'),v=null;try{v=localStorage.getItem('ram_consent')}catch(e){}
window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};
gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:v==='1'?'granted':'denied',wait_for_update:500});
gtag('set','ads_data_redaction',true);gtag('set','url_passthrough',false);
(function(){var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id=GAID';document.head.appendChild(s);gtag('js',new Date());gtag('config','GAID',{anonymize_ip:true})})();
if(v===null){setTimeout(function(){c.style.display='block'},1200)}
c.addEventListener('click',function(e){var x=e.target.getAttribute('data-c');if(x===null)return;try{localStorage.setItem('ram_consent',x)}catch(e){}c.style.display='none';gtag('consent','update',{analytics_storage:x==='1'?'granted':'denied'})});
function src(h){var m=[['chatgpt|openai','chatgpt'],['perplexity','perplexity'],['gemini|bard','gemini'],['copilot','copilot'],['claude','claude'],['google','google'],['bing','bing'],['duckduckgo','duckduckgo'],['yahoo','yahoo'],['facebook|fb.','facebook'],['instagram','instagram'],['airbnb','airbnb'],['booking.com','booking']];for(var i=0;i<m.length;i++)if(new RegExp(m[i][0]).test(h))return m[i][1];return h.slice(0,40)}
var S='direct';try{var u=new URLSearchParams(location.search).get('utm_source'),r=document.referrer?new URL(document.referrer).hostname.replace(/^www[.]/,''):'';if(u)S=src(u.toLowerCase());else if(r)S=r==location.hostname?'internal':src(r)}catch(e){}
window.ramEv=function(e,l,v){try{var d=JSON.stringify({e:e,p:location.pathname,l:l||'',s:S,v:Math.round(v||0)});if(!(navigator.sendBeacon&&navigator.sendBeacon('/ev.php',d)))fetch('/ev.php',{method:'POST',body:d,keepalive:true})}catch(x){}};
ramEv('view');var rd=0;addEventListener('scroll',function(){if(rd)return;var h=document.documentElement;if(h.scrollTop+innerHeight>=h.scrollHeight*.75){rd=1;ramEv('read')}},{passive:true});
document.addEventListener('submit',function(e){var f=e.target;if(!f.matches||!f.matches('form.bk,form.contact'))return;var bk=f.matches('.bk'),ap=(f.apt&&f.apt.value)||'',v=+(f.getAttribute('data-tot')||0);if(window.gtag){var p={form_type:bk?'booking':'contact',apartment:ap,transport_type:'beacon'};if(v){p.value=v;p.currency='EUR'}gtag('event','generate_lead',p)}ramEv('lead',ap,v)});
document.addEventListener('click',function(e){var a=e.target.closest('[data-evt]');if(a){if(window.gtag)gtag('event',a.getAttribute('data-evt'),{label:a.getAttribute('data-label')||''});ramEv(a.getAttribute('data-evt'),a.getAttribute('data-label'));return}
var l=e.target.closest('a[href]');if(!l||l.hasAttribute('data-lb'))return;try{var t=new URL(l.href,location.href)}catch(x){return}if(t.hostname==location.hostname){if(t.pathname!=location.pathname)ramEv('link',t.pathname)}else if(/^https?:/.test(t.protocol))ramEv('out',t.hostname.replace(/^www[.]/,''))});
var g=[].slice.call(document.querySelectorAll('[data-lb]'));if(g.length){var lb=document.createElement('div');lb.className='lb';lb.innerHTML='<button class="x" aria-label="Close">✕</button><button class="pv" aria-label="Previous">‹</button><img alt=""><button class="nx" aria-label="Next">›</button><div class="ct"></div>';document.body.appendChild(lb);var im=lb.querySelector('img'),ct=lb.querySelector('.ct'),i=0;
function show(k){if(!lb.classList.contains('on'))window.ramEv&&ramEv('gallery');i=(k+g.length)%g.length;im.src=g[i].getAttribute('href');im.alt=g[i].getAttribute('data-alt')||'';ct.textContent=(i+1)+' / '+g.length;lb.classList.add('on')}
g.forEach(function(a,k){a.addEventListener('click',function(e){e.preventDefault();show(k)})});
lb.addEventListener('click',function(e){if(e.target===lb||e.target.classList.contains('x'))lb.classList.remove('on');else if(e.target.classList.contains('pv'))show(i-1);else if(e.target.classList.contains('nx'))show(i+1)});
document.addEventListener('keydown',function(e){if(!lb.classList.contains('on'))return;if(e.key==='Escape')lb.classList.remove('on');if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1)})}})();""".replace("GAID", CONFIG["ga4"])


# ---------------------------------------------------------------- blocks
def month_price(lid):
    p = PRICING[lid]
    if p.get("month"):
        return p["month"]  # canone mensile spese incluse fissato da Vito
    return int(round(p["base"] * 30 * (1 - p["monthly"] / 100), -1))


# Prezzo minimo mensile (appartamenti da 28+ notti) nel title della pagina senza deposito
MIN_MONTH = min(month_price(k) for k, v in PRICING.items() if isinstance(v, dict) and v.get("min_nights", 0) >= 28 and not v.get("soon"))
for _l in LANGS:
    C[_l].P["nodeposit"]["title"] = C[_l].P["nodeposit"]["title"].replace("{min_month}", f"{MIN_MONTH:,}".replace(",", "."))


PRICE_TABLE = {
    "it": ("I prezzi mensili di RAM per zona", ["Appartamento", "Zona", "Ospiti", "Canone mensile", "Pulizia finale", "Soggiorno minimo"], "da {p} €", "{p} € una volta", "{n} notti",
           "Canone mensile spese incluse: utenze, riscaldamento e Wi-Fi. Il preventivo esatto dipende dalle date: <a href=\"{c}\">chiedilo qui</a>."),
    "en": ("RAM monthly prices by area", ["Apartment", "Area", "Guests", "Monthly rent", "Final cleaning", "Minimum stay"], "from €{p}", "€{p} one-off", "{n} nights",
           "Monthly rent with all bills included: utilities, heating and Wi-Fi. The exact quote depends on your dates: <a href=\"{c}\">ask here</a>."),
    "es": ("Precios mensuales de RAM por zona", ["Apartamento", "Zona", "Huéspedes", "Alquiler mensual", "Limpieza final", "Estancia mínima"], "desde {p} €", "{p} € una vez", "{n} noches",
           "Alquiler mensual con todos los gastos incluidos: suministros, calefacción y wifi. El presupuesto exacto depende de tus fechas: <a href=\"{c}\">pídelo aquí</a>."),
    "fr": ("Les prix mensuels de RAM par quartier", ["Appartement", "Quartier", "Voyageurs", "Loyer mensuel", "Ménage final", "Séjour minimum"], "à partir de {p} €", "{p} € une fois", "{n} nuits",
           "Loyer mensuel charges comprises : énergie, chauffage et Wi-Fi. Le devis exact dépend de vos dates : <a href=\"{c}\">demandez-le ici</a>."),
    "de": ("Monatspreise von RAM nach Stadtteil", ["Wohnung", "Stadtteil", "Gäste", "Monatsmiete", "Endreinigung", "Mindestaufenthalt"], "ab {p} €", "{p} € einmalig", "{n} Nächte",
           "Monatsmiete inklusive aller Nebenkosten: Strom, Gas, Heizung und WLAN. Das genaue Angebot hängt von Ihren Daten ab: <a href=\"{c}\">hier anfragen</a>."),
}


def price_table(lang):
    """Tabella prezzi mensili per zona, calcolata da data/pricing.json (solo appartamenti da 28+ notti)."""
    T = C[lang]; h2, cols, f_rent, f_clean, f_min, note = PRICE_TABLE.get(lang, PRICE_TABLE["en"])
    fmt = lambda v: f"{v:,}".replace(",", "." if lang in ("it", "es", "de") else ",")
    rows = ""
    for lid, L in LISTINGS.items():
        p = PRICING.get(lid, {})
        if L["status"] != "live" or p.get("soon") or p.get("min_nights", 1) < 28:
            continue
        t = T.L[lid]
        rows += (f'<tr><td><a href="{path_of(lang, "l_" + lid)}">{esc(t["short"])}</a></td><td>{esc(t["area"])}</td><td>{L["guests"]}</td>'
                 f'<td>{f_rent.format(p=fmt(month_price(lid)))}</td><td>{f_clean.format(p=p["cleaning"])}</td><td>{f_min.format(n=p["min_nights"])}</td></tr>')
    head = "".join(f"<th>{c}</th>" for c in cols)
    return f'<h2>{h2}</h2><table><tr>{head}</tr>{rows}</table><p class="muted">{note.format(c=path_of(lang, "contact"))}</p>\n'


def short_table(lang):
    """Tabella prezzi a notte degli appartamenti per soggiorni brevi (min. < 28 notti), da data/pricing.json."""
    T = C[lang]; cols, f_b, f_w, f_d, f_c, f_n, note = _PS.get(lang, _PS["en"])
    rows, extra = "", ""
    for lid, L in LISTINGS.items():
        p = PRICING.get(lid, {})
        if L["status"] != "live" or p.get("soon") or p.get("min_nights", 1) >= 28:
            continue
        t = T.L[lid]
        rows += (f'<tr><td><a href="{path_of(lang, "l_" + lid)}">{esc(t["short"])}</a></td><td>{esc(t["area"])}</td><td>{L["guests"]}</td>'
                 f'<td>{f_b.format(b=p["base"])}</td><td>{f_w.format(w=p["weekend"])}</td><td>{f_d.format(wk=p["weekly"], mo=p["monthly"])}</td>'
                 f'<td>{f_c.format(c=p["cleaning"])}</td><td>{f_n.format(n=p["min_nights"])}</td></tr>')
        if p.get("extra_fee"):
            extra += note.format(x=p["extra_after"], f=p["extra_fee"]) + " "
    head = "".join(f"<th>{c}</th>" for c in cols)
    return f'<table><tr>{head}</tr>{rows}</table>' + (f'<p class="muted">{extra.strip()}</p>' if extra else "") + "\n"


def fill_data(lang, s):
    """Segnaposto della pagina dati prezzi: numeri da pricing.json, data di build e link interni."""
    fmt = lambda v: f"{v:,}".replace(",", "." if lang in ("it", "es", "de") else ",")
    s = s.replace("[[turro]]", fmt(month_price("turro"))).replace("[[vdn]]", fmt(month_price("vdn"))).replace("[[date]]", TODAY).replace("[[min_month]]", fmt(MIN_MONTH))
    return re.sub(r"\[\[path:(\w+)\]\]", lambda m: path_of(lang, m.group(1)), s)


def listing_card(lang, lid, sizes="(max-width:620px) 100vw, (max-width:960px) 50vw, 33vw"):
    T = C[lang]; L = LISTINGS[lid]; t = T.L[lid]
    tag = f'<span class="tag soon">{esc(T.ui["soon"])}</span>' if L["status"] == "soon" else f'<span class="tag">{esc(t["stay_tag"])}</span>'
    pr = PRICING.get(lid, {})
    if pr.get("soon"): price = T.ui["price_month_req"]
    elif pr.get("min_nights", 1) >= 28: price = T.ui["price_month"].format(p=f"{month_price(lid):,}".replace(",", "."))
    else: price = T.ui["price_night"].format(p=pr["base"])
    return f"""<article class="card">{tag}<div class="ph">{img(L["photos"], L.get("cover", 0), sizes, alt=t["name"])}</div><div class="bd">
<h3><a href="{path_of(lang, "l_" + lid)}">{esc(t["name"])}</a></h3><div class="meta"><span>{esc(t["area"])}</span><span>{T.ui["guests"].format(n=L["guests"])}</span><span>{esc(t["rooms"])}</span></div>
<p class="muted" style="margin:0;font-size:15px">{esc(t["card"])}</p><div class="price">{price}</div></div></article>"""


def reviews_grid(lang, n=6, listing=None):
    T = C[lang]
    rs = [r for r in REVIEWS if (listing is None or r.get("listing") == listing)][:n]
    out = ""
    for r in rs:
        src = r.get("source", "Airbnb")
        lst = f' · {esc(T.L[r["listing"]]["short"])}' if r.get("listing") in T.L else ""
        out += f'<article class="rev"><div class="stars" aria-label="5/5">{stars(r.get("stars", 5))}</div><p>“{esc(r["text"])}”</p><footer><b>{esc(r["name"])}</b> · {esc(src)} · {esc(r.get("date", ""))}{lst}</footer></article>'
    return out


def features(T, keys, band=False):
    return "".join(f'<div class="feat"><div class="ic" aria-hidden="true">{T.FEAT[k][0]}</div><h3>{esc(T.FEAT[k][1])}</h3><p>{esc(T.FEAT[k][2])}</p></div>' for k in keys)


def cta_band(lang):
    T = C[lang]
    return f"""<section class="band"><div class="wrap split"><div><span class="kicker" style="color:#f0a5ad">{esc(T.ui["cta_kicker"])}</span><h2 class="mt0">{esc(T.ui["cta_title"])}</h2><p class="lead">{esc(T.ui["cta_text"])}</p>
<div class="cta-row"><a class="btn" href="{path_of(lang, "contact")}" data-evt="cta_contact">{esc(T.ui["cta_btn"])}</a><a class="btn ghost" style="color:#fff!important;border-color:#fff" href="{path_of(lang, "apartments")}">{esc(T.ui["see_apts"])}</a></div></div>
<div class="round">{img("vito", 2, "(max-width:860px) 100vw, 50vw", alt=T.ui["alt_vito_phone"])}</div></div></section>"""


# ---------------------------------------------------------------- pages
def page_home(lang):
    T = C[lang]; P = T.P["home"]
    cards = "".join(listing_card(lang, lid) for lid in LISTINGS)
    hn = P.get("hero_note")
    hero_note = f'<p style="margin:-6px 0 18px">{esc(hn[0])}: <a href="{path_of(lang, hn[1])}" data-evt="hero_students">{esc(hn[2])} →</a></p>' if hn else ""
    # Risposta diretta in apertura (prezzi da pricing.json) e link alle guide più cercate
    answer = ""
    if P.get("answer"):
        fmt = lambda v: f"{v:,}".replace(",", "." if lang in ("it", "es", "de") else ",")
        nights = [PRICING[k]["base"] for k, L in LISTINGS.items() if L["status"] == "live" and not PRICING.get(k, {}).get("soon") and PRICING[k].get("min_nights", 1) < 28]
        answer = '<p class="answer"><b>' + esc(P["answer"].format(turro=fmt(month_price("turro")), vdn=fmt(month_price("vdn")), night=min(nights) if nights else "")) + '</b></p>'
        if P.get("answer_links"):
            lab, keys = P["answer_links"]
            answer += f'<p class="answer-links">{esc(lab)}: ' + " · ".join(f'<a href="{path_of(lang, k)}" data-evt="hero_guide">{esc(T.P[k]["nav"])}</a>' for k in keys) + '</p>'
    guides = "".join(f'<a class="feat" style="text-decoration:none;color:inherit" href="{path_of(lang, k)}"><h3>{esc(T.P[k]["nav"])} →</h3><p>{esc(T.P[k]["desc"])}</p></a>' for k in CONFIG["guides"])
    body = f"""<section class="hero"><div class="wrap hero-grid"><div><span class="kicker">{esc(P["kicker"])}</span><h1>{esc(P["h1"])}</h1>{answer}<p class="lead">{esc(P["lead"])}</p>{hero_note}
<div class="cta-row"><a class="btn" href="{path_of(lang, "apartments")}" data-evt="cta_apartments">{esc(T.ui["see_apts"])}</a><a class="btn ghost" href="{path_of(lang, "contact")}" data-evt="cta_contact">{esc(T.ui["ask"])}</a></div>
<div class="trust">{badge_sh(T)}<span class="badge">★ {CONFIG["rating"]} · {T.ui["n_reviews"].format(n=CONFIG["reviews_count"])}</span><span class="badge">Ⓜ M1 Precotto · Turro</span></div></div>
<div class="hero-img">{img("valdinon", 0, "(max-width:860px) 100vw, 50vw", eager=True, alt=P["hero_alt"])}</div></div></section>
<section><div class="wrap"><div class="sec-head"><div><span class="kicker">{esc(T.ui["nav_apartments"])}</span><h2>{esc(P["apts_title"])}</h2></div><a href="{path_of(lang, "apartments")}">{esc(T.ui["all_apts"])} →</a></div><div class="grid g4 stations">{cards}</div></div></section>
<section class="band"><div class="wrap"><span class="kicker" style="color:#f0a5ad">{esc(P["why_kicker"])}</span><h2 class="mt0">{esc(P["why_title"])}</h2><div class="grid g4" style="margin-top:24px">{features(T, ["deposit", "bills", "contract", "metro"])}</div></div></section>
<section><div class="wrap split"><div class="round">{img("vito", 0, "(max-width:860px) 100vw, 50vw", alt=T.ui["alt_vito"])}</div><div><span class="kicker">{esc(P["host_kicker"])}</span><h2 class="mt0">{esc(P["host_title"])}</h2>{P["host_html"]}<div class="trust">{badge_sh(T)}<span class="badge">{esc(T.ui["resp_badge"])}</span></div><div class="cta-row"><a class="btn ghost" href="{path_of(lang, "about")}">{esc(T.ui["meet_host"])}</a></div></div></div></section>
<section><div class="wrap"><div class="sec-head"><div><span class="kicker">{esc(T.ui["nav_reviews"])}</span><h2>{esc(P["rev_title"])}</h2></div><a href="{path_of(lang, "reviews")}">{esc(T.ui["all_reviews"])} →</a></div><div class="grid g3">{reviews_grid(lang, 6)}</div></div></section>
<section><div class="wrap"><span class="kicker">{esc(T.ui["nav_guides"])}</span><h2 class="mt0">{esc(P["guides_title"])}</h2><div class="grid g3" style="margin-top:20px">{guides}</div></div></section>
{cta_band(lang)}"""
    ld = {"@context": "https://schema.org", "@type": "LodgingBusiness", "name": "Rent Apartment Milan", "alternateName": ["RAM", "Rent a flat in Milan"], "url": url_of(lang, "home"),
          "image": img_src("valdinon", 0), "email": CONFIG["email"], "description": P["desc"],
          "address": {"@type": "PostalAddress", "streetAddress": CONFIG["street"], "addressLocality": "Milano", "postalCode": CONFIG["zip"], "addressRegion": "MI", "addressCountry": "IT"},
          "telephone": CONFIG["phone"], "sameAs": CONFIG["same_as"], "hasMap": CONFIG["same_as"][0],
          "areaServed": "Milano", "founder": {"@type": "Person", "name": "Vito Semeraro"},
          "knowsLanguage": ["it", "en"], "inLanguage": lang}
    return layout(lang, "home", P["title"], P["desc"], body, ld=ld)


def page_apartments(lang):
    T = C[lang]; P = T.P["apartments"]
    cards = "".join(listing_card(lang, lid, "(max-width:620px) 100vw, 50vw") for lid in LISTINGS)
    body = f"""<section><div class="wrap"><h1>{esc(P["h1"])}</h1><p class="lead">{esc(P["lead"])}</p><h2 class="sr">{esc(T.ui["nav_apartments"])}</h2><div class="grid g2" style="margin-top:26px">{cards}</div></div></section>
<section><div class="wrap prose">{P["html"]}</div></section>{cta_band(lang)}"""
    ld = {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": url_of(lang, "l_" + lid), "name": T.L[lid]["name"]} for i, lid in enumerate(LISTINGS)]}
    return layout(lang, "apartments", P["title"], P["desc"], body, ld=ld, crumbs=[(T.ui["nav_apartments"], path_of(lang, "apartments"))])


def page_listing(lang, lid):
    T = C[lang]; L = LISTINGS[lid]; t = T.L[lid]; key = "l_" + lid
    ph = IMAGES.get(L["photos"], IMAGES["valdinon"]); setn = L["photos"] if L["photos"] in IMAGES else "valdinon"
    order = [L.get("cover", 0)] + [i for i in range(len(ph)) if i != L.get("cover", 0)]
    gal = ""
    for j, i in enumerate(order):
        m = ph[i]; href = f"/img/{setn}/{m['base']}-1600.webp" if m["w"] >= 1600 else f"/img/{setn}/{m['base']}-960.webp"
        if not os.path.exists(os.path.join(DIST, href.lstrip("/"))): href = f"/img/{setn}/{m['base']}.jpg"
        alt = f'{t["name"]} – {T.ui["photo"]} {j + 1}'
        inner = img(setn, i, "(max-width:760px) 100vw, 60vw" if j == 0 else "25vw", eager=(j == 0), alt=alt) if j < 5 else ""
        more = f'<span>+{len(ph) - 5} {T.ui["photos"]}</span>' if j == 4 and len(ph) > 5 else ""
        gal += f'<a href="{href}" data-lb data-alt="{esc(alt)}"{" class=more" if more else ""}{"" if j < 5 else " hidden"}>{inner}{more}</a>'
    facts = "".join(f"<span>{esc(f)}</span>" for f in t["facts"])
    am = "".join(f"<li>{esc(a)}</li>" for a in t["amenities"])
    near = "".join(f"<li><span>{esc(a)}</span><b>{esc(b)}</b></li>" for a, b in t["nearby"])
    P_ = PRICING.get(lid, {})
    if L["status"] == "soon":
        price = f'<div class="p">{esc(T.ui["soon"])}</div><p class="muted" style="font-size:14px">{esc(T.ui["soon_text"])}</p>'
        cta = f'<a class="btn" href="{path_of(lang, "contact")}?apt={lid}" data-evt="cta_contact" data-label="{lid}">{esc(T.ui["notify"])}</a>'
    else:
        if P_.get("min_nights", 1) >= 28:
            price = f'<div class="p">{T.ui["from"]} €{month_price(lid):,} <small>/ {T.ui["month"]}</small></div>'.replace(",", ".")
        else:
            price = f'<div class="p">{T.ui["from"]} €{P_["base"]} <small>/ {T.ui["night"]}</small></div>'
        cta = BK.render(lang, lid, PRICING, path_of(lang, "privacy"))
    box_list = "".join(f"<li>{esc(x)}</li>" for x in t["box"])
    revs = reviews_grid(lang, 6, lid)
    rev_sec = f'<h2>{esc(T.ui["guests_say"])}</h2><div class="grid g2">{revs}</div>' if revs else ""
    others = "".join(listing_card(lang, o) for o in LISTINGS if o != lid)
    body = f"""<div class="wrap"><div class="gallery">{gal}</div>
<div class="listing"><div><span class="kicker">{esc(t["area"])}</span><h1 style="font-size:clamp(1.8rem,4vw,2.7rem)">{esc(t["name"])}</h1><div class="facts">{facts}</div>
<div class="trust" style="margin:0 0 18px">{badge_sh(T) if L.get("superhost") else ""}{('<span class="badge sh"><i>★</i> '+L["rating"]+" · "+T.ui["n_reviews"].format(n=L["nrev"])+" Airbnb</span>") if L.get("rating") else ""}{('<span class="badge sh"><i>◆</i> '+T.ui["guestfav"]+"</span>") if L.get("guestfav") else ""}</div>
{t["html"]}
<h2>{esc(T.ui["amenities"])}</h2><ul class="am">{am}</ul>
<h2>{esc(T.ui["location"])}</h2><p>{esc(t["location"])}</p><ul class="mapline">{near}</ul>
{rev_sec}</div>
<aside class="box">{price}{cta}<ul>{box_list}</ul><p style="font-size:13px;margin:14px 0 0" class="muted">{(chr(9733)+" "+T.ui["guestfav"]+"<br>") if L.get("guestfav") else ""}CIN {L.get("cin","")}</p></aside></div></div>
<section><div class="wrap"><h2>{esc(T.ui["other_apts"])}</h2><div class="grid g3">{others}</div></div></section>{cta_band(lang)}"""
    ld = {"@context": "https://schema.org", "@type": "Apartment", "name": t["name"], "description": t["desc"], "url": url_of(lang, key),
          "image": [img_src(setn, i) for i in order[:6]], "numberOfRooms": L["rooms_n"], "numberOfBedrooms": L["bedrooms"],
          "numberOfBathroomsTotal": L["baths"], "occupancy": {"@type": "QuantitativeValue", "maxValue": L["guests"]},
          "petsAllowed": False, "address": {"@type": "PostalAddress", "streetAddress": L.get("street", ""), "addressLocality": "Milano", "postalCode": L.get("zip", "20128"), "addressRegion": "MI", "addressCountry": "IT"},
          "containedInPlace": {"@type": "Place", "name": t["area"]}}
    if L.get("floor_m2"):
        ld["floorSize"] = {"@type": "QuantitativeValue", "value": L["floor_m2"], "unitCode": "MTK"}
    if L["status"] != "soon" and P_:
        # Stesso prezzo "da" mostrato nella scheda (data/pricing.json): mensile per i soggiorni da 28+ notti, altrimenti a notte
        monthly = P_.get("min_nights", 1) >= 28
        amount = month_price(lid) if monthly else P_["base"]
        ld["@type"] = ["Apartment", "Product"]
        ld["offers"] = {"@type": "Offer", "url": url_of(lang, key), "priceCurrency": "EUR", "price": amount, "availability": "https://schema.org/InStock",
                        "priceSpecification": {"@type": "UnitPriceSpecification", "price": amount, "priceCurrency": "EUR", "unitCode": "MON" if monthly else "DAY",
                                               "referenceQuantity": {"@type": "QuantitativeValue", "value": 1, "unitCode": "MON" if monthly else "DAY"}}}
    return layout(lang, key, t["title"], t["desc"], body, ld=ld, og_img=img_src(setn, order[0]), xcss=BK.CSS if L["status"] != "soon" else "", xjs=BK.JS if L["status"] != "soon" else "",
                  crumbs=[(T.ui["nav_apartments"], path_of(lang, "apartments")), (t["short"], path_of(lang, key))])


def page_article(lang, key):
    T = C[lang]; P = T.P[key]
    extra, ld = "", None
    hero = ""
    if P.get("img"):
        s, i = P["img"]
        pic = img(s, i, "(max-width:1160px) 100vw, 1160px", eager=True, alt=P["h1"]).replace("<img ", '<img style="width:100%;height:100%;object-fit:cover" ')
        hero = f'<div class="round" style="margin:10px 0 26px;aspect-ratio:21/9">{pic}</div>'
    faq_list, faq_h = P.get("faq"), ""
    if not faq_list and _GFAQ.get(lang, {}).get(key):
        faq_list = _GFAQ[lang][key]
        faq_h = f'<h2>{esc(C[lang].P["faq"]["nav"])}</h2>'
    if faq_list:
        P = dict(P, faq=faq_list)
        extra = faq_h + "".join(f'<details class="faq"><summary>{esc(fill_data(lang, q))}</summary><p>{fill_data(lang, a)}</p></details>' for q, a in P["faq"])
        ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": fill_data(lang, q), "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", fill_data(lang, a))}} for q, a in P["faq"]]}
    if key == "reviews":
        extra = f'<div class="grid g3" style="margin-top:20px">{reviews_grid(lang, 200)}</div>'
    if key == "contact":
        opts = "".join(f'<option value="{lid}">{esc(T.L[lid]["short"])}</option>' for lid in LISTINGS)
        F = T.FORM
        extra = f"""<form class="contact" method="post" action="/contact.php"><input type="hidden" name="lang" value="{lang}"><label class="hp">Website<input name="website" tabindex="-1" autocomplete="off"></label>
<div class="row"><label>{F["name"]}<input name="name" required autocomplete="name"></label><label>{F["email"]}<input type="email" name="email" required autocomplete="email"></label></div>
<div class="row"><label>{F["apt"]}<select name="apt" id="apt"><option value="">{F["any"]}</option>{opts}</select></label><label>{F["guests"]}<input type="number" name="guests" min="1" max="8" value="1"></label></div>
<div class="row"><label>{F["in"]}<input type="date" name="checkin" required></label><label>{F["out"]}<input type="date" name="checkout" required></label></div><input type="hidden" name="js" value="0">
<label>{F["reason"]}<select name="reason">{"".join(f"<option>{esc(o)}</option>" for o in F["reasons"])}</select></label>
<label>{F["msg"]}<textarea name="message" rows="5" required></textarea></label>
<label style="display:flex;gap:10px;align-items:flex-start;font-weight:400"><input type="checkbox" required style="margin-top:5px"> <span>{F["privacy"].replace("{privacy}", path_of(lang, "privacy"))}</span></label>
<button class="btn" type="submit" data-evt="form_submit">{F["send"]}</button></form>
<script>(function(){{document.querySelectorAll('input[name=js]').forEach(function(i){{i.value='1'}});var p=new URLSearchParams(location.search).get('apt');if(p){{var s=document.getElementById('apt');s&&(s.value=p)}}}})()</script>"""
    if key == "about":
        pics = "".join('<div class="round">' + img("vito", i, "(max-width:620px) 100vw, 50vw", alt=T.ui["alt_vito"]) + "</div>" for i in (4, 5))
        extra = f'<div class="grid g2" style="margin:26px 0">{pics}</div>'
    side = ""
    if P.get("apts"):
        side = f'<section><div class="wrap"><h2>{esc(T.ui["apts_for_this"])}</h2><div class="grid g3">{"".join(listing_card(lang, l) for l in P["apts"])}</div></div></section>'
    if key == "guides":
        extra = "".join(f'<a class="feat" style="display:block;text-decoration:none;color:inherit;margin-bottom:12px" href="{path_of(lang, k)}"><h3>{esc(T.P[k]["h1"])} →</h3><p>{esc(T.P[k]["desc"])}</p></a>' for k in CONFIG["guides"])
    kick = f'<span class="kicker">{esc(P["kicker"])}</span>' if P.get("kicker") else ""
    qa_html, qa_ld = AEO.answer_box(lang, key, esc, fill_data)
    body = f"""<section style="padding-top:20px"><div class="wrap">{kick}<h1>{esc(P["h1"])}</h1>{f'<p class="lead">{esc(fill_data(lang, P["lead"]))}</p>' if P.get("lead") else ""}{hero}
<div class="prose">{qa_html}{fill_data(lang, P.get("html", "").replace("<!--PRICES-->", price_table(lang) if key in ("monthly", "students", "prices") else "").replace("<!--SHORT-->", short_table(lang) if key == "prices" else ""))}{extra}</div></div></section>{side}{"" if key in ("contact", "privacy") else cta_band(lang)}"""
    if P.get("article"):
        art = {"@context": "https://schema.org", "@type": "Article", "headline": P["h1"], "description": fill_data(lang, P["desc"]), "inLanguage": lang,
               "author": {"@type": "Person", "name": "Vito Semeraro", "url": url_of(lang, "about")}, "publisher": {"@type": "Organization", "name": "RAM – Rent Apartment Milan"},
               "dateModified": TODAY, "mainEntityOfPage": url_of(lang, key)}
        ld = [art] + ([ld] if ld else [])
    if qa_ld:
        ld = (ld if isinstance(ld, list) else ([ld] if ld else []))
        faqld = next((x for x in ld if x.get("@type") == "FAQPage"), None)
        if faqld:  # un solo FAQPage per pagina: la risposta diretta va in testa alle FAQ
            faqld["mainEntity"] = qa_ld["mainEntity"] + faqld["mainEntity"]
        else:
            ld = ld + [qa_ld]
    if key == "about":
        ld = {"@context": "https://schema.org", "@type": "Person", "name": "Vito Semeraro", "jobTitle": "Host", "image": img_src("vito", 0), "worksFor": {"@type": "Organization", "name": "RAM – Rent Apartment Milan"}}
    crumbs = []
    if key in CONFIG["guides"]:
        crumbs.append((T.ui["nav_guides"], path_of(lang, "guides")))
    crumbs.append((P.get("nav", P["h1"]), path_of(lang, key)))
    return layout(lang, key, fill_data(lang, P["title"]), fill_data(lang, P["desc"]), body, ld=ld, crumbs=crumbs, robots="noindex,follow" if key == "thanks" else "index,follow")


# ---------------------------------------------------------------- build
def write(path, s):
    full = os.path.join(DIST, path.lstrip("/"), "index.html") if path.endswith("/") else os.path.join(DIST, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf8", newline="\n").write(s)


def main():
    for d in os.listdir(DIST):
        if d not in ("img",):
            p = os.path.join(DIST, d); shutil.rmtree(p, ignore_errors=True) if os.path.isdir(p) else os.remove(p)
    keys = list(C[CONFIG["default_lang"]].SLUG.keys())
    urls = []
    for lang in LANGS:
        for key in keys:
            if key == "blog": s = BLOG.page_index(lang, sys.modules[__name__])
            elif key == "home": s = page_home(lang)
            elif key == "apartments": s = page_apartments(lang)
            elif key.startswith("l_"): s = page_listing(lang, key[2:])
            else: s = page_article(lang, key)
            write(path_of(lang, key), s)
            if key != "thanks": urls.append((key, lang))
    # sitemap con hreflang
    sm = ['<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for key, lang in urls:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url_of(l, key)}"/>' for l in LANGS)
        sm.append(f"<url><loc>{url_of(lang, key)}</loc><lastmod>{TODAY}</lastmod>{alts}<xhtml:link rel=\"alternate\" hreflang=\"x-default\" href=\"{url_of('en', key)}\"/></url>")
    for a in BLOG.ARTICLES:
        open_ = None
        write(a["url"], BLOG.page_article(a, sys.modules[__name__]))
        sm.append(f"<url><loc>{SITE}{a['url']}</loc><lastmod>{a['updated']}</lastmod></url>")
    sm.append("</urlset>")
    open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf8").write("\n".join(sm))
    bots = "".join(f"User-agent: {b}\nAllow: /\n\n" for b in ("GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot", "Google-Extended", "Bingbot", "Applebot-Extended"))
    open(os.path.join(DIST, "robots.txt"), "w").write(f"{bots}User-agent: *\nAllow: /\nDisallow: /contact.php\nDisallow: /availability.php\nDisallow: /ev.php\nDisallow: /ev-stats.php\n\nSitemap: {SITE}/sitemap.xml\n")
    me = sys.modules[__name__]
    open(os.path.join(DIST, "llms.txt"), "w", encoding="utf8").write(AEO.llms_txt(me))
    open(os.path.join(DIST, INDEXNOW_KEY + ".txt"), "w").write(INDEXNOW_KEY)
    all_urls = [url_of(l, k) for k, l in urls] + [SITE + a["url"] for a in BLOG.ARTICLES]
    open(os.path.join(DIST, "indexnow.json"), "w").write(AEO.indexnow_payload(me, all_urls, INDEXNOW_KEY))
    for f in os.listdir(os.path.join(HERE, "static")):
        shutil.copy(os.path.join(HERE, "static", f), os.path.join(DIST, f))
    # Cloudflare Workers: script, configurazione e file da escludere dagli asset
    os.makedirs(os.path.join(DIST, "_worker"), exist_ok=True)
    CF = os.path.join(HERE, "cloudflare")
    shutil.copy(os.path.join(CF, "worker.js"), os.path.join(DIST, "_worker", "worker.js"))
    shutil.copy(os.path.join(CF, "wrangler.jsonc"), os.path.join(DIST, "wrangler.jsonc"))
    shutil.copy(os.path.join(CF, "assetsignore"), os.path.join(DIST, ".assetsignore"))
    shutil.copy(os.path.join(CF, "schema.sql"), os.path.join(DIST, "schema.sql"))
    # 404 multilingua semplice
    T = C["en"]
    write("/404.html", layout("en", "home", "Page not found – RAM", "Page not found", f'<section><div class="wrap prose"><h1>Page not found</h1><p>The page you are looking for has moved. <a href="/">Go to the homepage</a> · <a href="/it/">Italiano</a> · <a href="/apartments/">Apartments</a></p></div></section>', robots="noindex"))
    print("pagine:", len(urls), "+ thanks/404")


if __name__ == "__main__":
    main()
