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
from mm_texts import M as _MM
import blog as BLOG
for _l in LANGS:
    C[_l].SLUG["nodeposit"] = _ND[_l][0]; C[_l].P["nodeposit"] = _ND[_l][1]; C[_l].L["mm"].update(_MM[_l]); C[_l].SLUG["blog"] = "blog"; C[_l].P["blog"] = BLOG.INDEX[_l]
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
<link rel="icon" href="/favicon.png" type="image/png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="theme-color" content="#f7f3ee">
<style>{CSS}{xcss}</style>
<script type="application/ld+json">{json.dumps(ld_all, ensure_ascii=False)}</script>
</head><body><a class="skip" href="#main">{esc(T.ui["skip"])}</a>
<header class="top"><div class="wrap bar"><a class="logo" href="{path_of(lang, "home")}"><b>RAM</b><span>Rent Apartment Milan<small>{esc(T.ui["logo_sub"])}</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">☰ {esc(T.ui["menu"])}</button><nav class="main" id="nav">{nav}</nav></div></header>
{crumb_html}<main id="main">{body}</main>
<footer class="site"><div class="wrap"><div class="cols">
<div><a class="logo" href="{path_of(lang, "home")}" style="color:#fff"><b>RAM</b><span>Rent Apartment Milan</span></a><p style="margin-top:14px">{esc(T.ui["foot_about"])}</p><p><a href="mailto:{CONFIG["email"]}">{CONFIG["email"]}</a></p></div>
<div><p class="fh">{esc(T.ui["nav_apartments"])}</p><ul>{foot_apts}</ul></div>
<div><p class="fh">{esc(T.ui["nav_guides"])}</p><ul>{foot_guides}</ul></div>
<div><p class="fh">RAM</p><ul><li><a href="{path_of(lang, "about")}">{esc(T.ui["nav_about"])}</a></li><li><a href="{path_of(lang, "reviews")}">{esc(T.ui["nav_reviews"])}</a></li><li><a href="{path_of(lang, "faq")}">FAQ</a></li><li><a href="{path_of(lang, "contact")}">{esc(T.ui["nav_contact"])}</a></li><li><a href="{path_of(lang, "privacy")}">Privacy &amp; cookie</a></li></ul></div>
</div><div class="legal"><span>© {datetime.date.today().year} RAM · Rent Apartment Milan · Milano</span><span>{esc(T.ui["cin_note"])}</span></div></div></footer>
<div id="consent" role="dialog" aria-label="Cookie" aria-live="polite"><p>{T.ui["cookie_text"].replace("{privacy}", path_of(lang, "privacy"))}</p><button class="btn small" data-c="1">{esc(T.ui["cookie_ok"])}</button> <button class="btn small ghost" data-c="0">{esc(T.ui["cookie_no"])}</button></div>
<script>{JS}{xjs}</script></body></html>"""


JS = """(function(){var b=document.querySelector('.menu-btn'),n=document.getElementById('nav');b&&b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o)});
function ga(){if(window.__ga)return;window.__ga=1;var s=document.createElement('script');s.async=1;s.src='https://www.googletagmanager.com/gtag/js?id=GAID';document.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config','GAID',{anonymize_ip:true})}
var c=document.getElementById('consent'),v=null;try{v=localStorage.getItem('ram_consent')}catch(e){}
if(v==='1'){ga()}else if(v===null){setTimeout(function(){c.style.display='block'},1200)}
c.addEventListener('click',function(e){var x=e.target.getAttribute('data-c');if(x===null)return;try{localStorage.setItem('ram_consent',x)}catch(e){}c.style.display='none';if(x==='1')ga()});
document.addEventListener('click',function(e){var a=e.target.closest('[data-evt]');if(a&&window.gtag)gtag('event',a.getAttribute('data-evt'),{label:a.getAttribute('data-label')||''})});
var g=[].slice.call(document.querySelectorAll('[data-lb]'));if(g.length){var lb=document.createElement('div');lb.className='lb';lb.innerHTML='<button class="x" aria-label="Close">✕</button><button class="pv" aria-label="Previous">‹</button><img alt=""><button class="nx" aria-label="Next">›</button><div class="ct"></div>';document.body.appendChild(lb);var im=lb.querySelector('img'),ct=lb.querySelector('.ct'),i=0;
function show(k){i=(k+g.length)%g.length;im.src=g[i].getAttribute('href');im.alt=g[i].getAttribute('data-alt')||'';ct.textContent=(i+1)+' / '+g.length;lb.classList.add('on')}
g.forEach(function(a,k){a.addEventListener('click',function(e){e.preventDefault();show(k)})});
lb.addEventListener('click',function(e){if(e.target===lb||e.target.classList.contains('x'))lb.classList.remove('on');else if(e.target.classList.contains('pv'))show(i-1);else if(e.target.classList.contains('nx'))show(i+1)});
document.addEventListener('keydown',function(e){if(!lb.classList.contains('on'))return;if(e.key==='Escape')lb.classList.remove('on');if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1)})}})();""".replace("GAID", CONFIG["ga4"])


# ---------------------------------------------------------------- blocks
def month_price(lid):
    p = PRICING[lid]
    return int(round(p["base"] * 30 * (1 - p["monthly"] / 100), -1))


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
    guides = "".join(f'<a class="feat" style="text-decoration:none;color:inherit" href="{path_of(lang, k)}"><h3>{esc(T.P[k]["nav"])} →</h3><p>{esc(T.P[k]["desc"])}</p></a>' for k in CONFIG["guides"])
    body = f"""<section class="hero"><div class="wrap hero-grid"><div><span class="kicker">{esc(P["kicker"])}</span><h1>{esc(P["h1"])}</h1><p class="lead">{esc(P["lead"])}</p>
<div class="cta-row"><a class="btn" href="{path_of(lang, "apartments")}" data-evt="cta_apartments">{esc(T.ui["see_apts"])}</a><a class="btn ghost" href="{path_of(lang, "contact")}" data-evt="cta_contact">{esc(T.ui["ask"])}</a></div>
<div class="trust">{badge_sh(T)}<span class="badge">★ {CONFIG["rating"]} · {T.ui["n_reviews"].format(n=CONFIG["reviews_count"])}</span><span class="badge">Ⓜ M1 Precotto · Turro</span></div></div>
<div class="hero-img">{img("valdinon", 0, "(max-width:860px) 100vw, 50vw", eager=True, alt=P["hero_alt"])}</div></div></section>
<section><div class="wrap"><div class="sec-head"><div><span class="kicker">{esc(T.ui["nav_apartments"])}</span><h2>{esc(P["apts_title"])}</h2></div><a href="{path_of(lang, "apartments")}">{esc(T.ui["all_apts"])} →</a></div><div class="grid g4 stations">{cards}</div></div></section>
<section class="band"><div class="wrap"><span class="kicker" style="color:#f0a5ad">{esc(P["why_kicker"])}</span><h2 class="mt0">{esc(P["why_title"])}</h2><div class="grid g4" style="margin-top:24px">{features(T, ["deposit", "bills", "contract", "metro"])}</div></div></section>
<section><div class="wrap split"><div class="round">{img("vito", 0, "(max-width:860px) 100vw, 50vw", alt=T.ui["alt_vito"])}</div><div><span class="kicker">{esc(P["host_kicker"])}</span><h2 class="mt0">{esc(P["host_title"])}</h2>{P["host_html"]}<div class="trust">{badge_sh(T)}<span class="badge">{esc(T.ui["resp_badge"])}</span></div><div class="cta-row"><a class="btn ghost" href="{path_of(lang, "about")}">{esc(T.ui["meet_host"])}</a></div></div></div></section>
<section><div class="wrap"><div class="sec-head"><div><span class="kicker">{esc(T.ui["nav_reviews"])}</span><h2>{esc(P["rev_title"])}</h2></div><a href="{path_of(lang, "reviews")}">{esc(T.ui["all_reviews"])} →</a></div><div class="grid g3">{reviews_grid(lang, 6)}</div></div></section>
<section><div class="wrap"><span class="kicker">{esc(T.ui["nav_guides"])}</span><h2 class="mt0">{esc(P["guides_title"])}</h2><div class="grid g3" style="margin-top:20px">{guides}</div></div></section>
{cta_band(lang)}"""
    ld = {"@context": "https://schema.org", "@type": "LodgingBusiness", "name": "RAM – Rent Apartment Milan", "url": url_of(lang, "home"),
          "image": img_src("valdinon", 0), "email": CONFIG["email"], "description": P["desc"],
          "address": {"@type": "PostalAddress", "addressLocality": "Milano", "postalCode": "20128", "addressRegion": "MI", "addressCountry": "IT"},
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
          "petsAllowed": False, "address": {"@type": "PostalAddress", "streetAddress": L.get("street", ""), "addressLocality": "Milano", "postalCode": "20128", "addressCountry": "IT"},
          "containedInPlace": {"@type": "Place", "name": t["area"]}}
    if L.get("floor_m2"):
        ld["floorSize"] = {"@type": "QuantitativeValue", "value": L["floor_m2"], "unitCode": "MTK"}
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
    if key == "faq":
        extra = "".join(f'<details class="faq"><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in P["faq"])
        ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in P["faq"]]}
    if key == "reviews":
        extra = f'<div class="grid g3" style="margin-top:20px">{reviews_grid(lang, 200)}</div>'
    if key == "contact":
        opts = "".join(f'<option value="{lid}">{esc(T.L[lid]["short"])}</option>' for lid in LISTINGS)
        F = T.FORM
        extra = f"""<form class="contact" method="post" action="/contact.php"><input type="hidden" name="lang" value="{lang}"><label class="hp">Website<input name="website" tabindex="-1" autocomplete="off"></label>
<div class="row"><label>{F["name"]}<input name="name" required autocomplete="name"></label><label>{F["email"]}<input type="email" name="email" required autocomplete="email"></label></div>
<div class="row"><label>{F["apt"]}<select name="apt" id="apt"><option value="">{F["any"]}</option>{opts}</select></label><label>{F["guests"]}<input type="number" name="guests" min="1" max="8" value="1"></label></div>
<div class="row"><label>{F["in"]}<input type="date" name="checkin"></label><label>{F["out"]}<input type="date" name="checkout"></label></div>
<label>{F["reason"]}<select name="reason">{"".join(f"<option>{esc(o)}</option>" for o in F["reasons"])}</select></label>
<label>{F["msg"]}<textarea name="message" rows="5" required></textarea></label>
<label style="display:flex;gap:10px;align-items:flex-start;font-weight:400"><input type="checkbox" required style="margin-top:5px"> <span>{F["privacy"].replace("{privacy}", path_of(lang, "privacy"))}</span></label>
<button class="btn" type="submit" data-evt="form_submit">{F["send"]}</button></form>
<script>(function(){{var p=new URLSearchParams(location.search).get('apt');if(p){{var s=document.getElementById('apt');s&&(s.value=p)}}}})()</script>"""
    if key == "about":
        pics = "".join('<div class="round">' + img("vito", i, "(max-width:620px) 100vw, 50vw", alt=T.ui["alt_vito"]) + "</div>" for i in (4, 5))
        extra = f'<div class="grid g2" style="margin:26px 0">{pics}</div>'
    side = ""
    if P.get("apts"):
        side = f'<section><div class="wrap"><h2>{esc(T.ui["apts_for_this"])}</h2><div class="grid g3">{"".join(listing_card(lang, l) for l in P["apts"])}</div></div></section>'
    if key == "guides":
        extra = "".join(f'<a class="feat" style="display:block;text-decoration:none;color:inherit;margin-bottom:12px" href="{path_of(lang, k)}"><h3>{esc(T.P[k]["h1"])} →</h3><p>{esc(T.P[k]["desc"])}</p></a>' for k in CONFIG["guides"])
    kick = f'<span class="kicker">{esc(P["kicker"])}</span>' if P.get("kicker") else ""
    body = f"""<section style="padding-top:20px"><div class="wrap">{kick}<h1>{esc(P["h1"])}</h1>{f'<p class="lead">{esc(P["lead"])}</p>' if P.get("lead") else ""}{hero}
<div class="prose">{P.get("html", "")}{extra}</div></div></section>{side}{"" if key in ("contact", "privacy") else cta_band(lang)}"""
    if P.get("article"):
        art = {"@context": "https://schema.org", "@type": "Article", "headline": P["h1"], "description": P["desc"], "inLanguage": lang,
               "author": {"@type": "Person", "name": "Vito Semeraro", "url": url_of(lang, "about")}, "publisher": {"@type": "Organization", "name": "RAM – Rent Apartment Milan"},
               "dateModified": TODAY, "mainEntityOfPage": url_of(lang, key)}
        ld = [art] + ([ld] if ld else [])
    if key == "about":
        ld = {"@context": "https://schema.org", "@type": "Person", "name": "Vito Semeraro", "jobTitle": "Host", "image": img_src("vito", 0), "worksFor": {"@type": "Organization", "name": "RAM – Rent Apartment Milan"}}
    crumbs = []
    if key in CONFIG["guides"]:
        crumbs.append((T.ui["nav_guides"], path_of(lang, "guides")))
    crumbs.append((P.get("nav", P["h1"]), path_of(lang, key)))
    return layout(lang, key, P["title"], P["desc"], body, ld=ld, crumbs=crumbs, robots="noindex,follow" if key == "thanks" else "index,follow")


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
    open(os.path.join(DIST, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /contact.php\nDisallow: /availability.php\n\nSitemap: {SITE}/sitemap.xml\n")
    for f in os.listdir(os.path.join(HERE, "static")):
        shutil.copy(os.path.join(HERE, "static", f), os.path.join(DIST, f))
    # 404 multilingua semplice
    T = C["en"]
    write("/404.html", layout("en", "home", "Page not found – RAM", "Page not found", f'<section><div class="wrap prose"><h1>Page not found</h1><p>The page you are looking for has moved. <a href="/">Go to the homepage</a> · <a href="/it/">Italiano</a> · <a href="/apartments/">Apartments</a></p></div></section>', robots="noindex"))
    print("pagine:", len(urls), "+ thanks/404")


if __name__ == "__main__":
    main()
