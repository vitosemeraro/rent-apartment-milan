# Blog: articoli in articles/*.md (front-matter + markdown), pagina indice /blog/ per lingua
import os, re, glob, datetime
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))

INDEX = {
    "en": {"nav": "Blog", "kicker": "Blog", "title": "Blog: renting an apartment in Milan, guides and news | RAM", "desc": "Guides and articles on renting in Milan: monthly stays, student housing, no-deposit rentals, trade fairs and life in Precotto and Turro.", "h1": "Blog and guides", "lead": "Practical articles for students, professionals and visitors looking for a home in Milan.", "guides": "Essential guides", "latest": "Latest articles", "read": "Read", "updated": "Updated"},
    "it": {"nav": "Blog", "kicker": "Blog", "title": "Blog: affittare casa a Milano, guide e novità | RAM", "desc": "Guide e articoli per affittare a Milano: soggiorni mensili, alloggi per studenti, affitti senza deposito, fiere e vita a Precotto e Turro.", "h1": "Blog e guide", "lead": "Articoli pratici per studenti, professionisti e visitatori che cercano casa a Milano.", "guides": "Guide essenziali", "latest": "Ultimi articoli", "read": "Leggi", "updated": "Aggiornato"},
    "es": {"nav": "Blog", "kicker": "Blog", "title": "Blog: alquilar piso en Milán, guías y novedades | RAM", "desc": "Guías y artículos para alquilar en Milán: estancias mensuales, alojamiento para estudiantes, pisos sin fianza y ferias.", "h1": "Blog y guías", "lead": "Artículos prácticos para estudiantes, profesionales y visitantes que buscan casa en Milán.", "guides": "Guías esenciales", "latest": "Últimos artículos", "read": "Leer", "updated": "Actualizado"},
    "fr": {"nav": "Blog", "kicker": "Blog", "title": "Blog : louer un appartement à Milan, guides et actualités | RAM", "desc": "Guides et articles pour louer à Milan : séjours au mois, logement étudiant, location sans caution, salons.", "h1": "Blog et guides", "lead": "Des articles pratiques pour étudiants, professionnels et visiteurs qui cherchent un logement à Milan.", "guides": "Guides essentiels", "latest": "Derniers articles", "read": "Lire", "updated": "Mis à jour"},
    "de": {"nav": "Blog", "kicker": "Blog", "title": "Blog: Wohnung in Mailand mieten, Ratgeber und News | RAM", "desc": "Ratgeber und Artikel zum Mieten in Mailand: Wohnen auf Zeit, Studentenwohnungen, Mieten ohne Kaution, Messen.", "h1": "Blog und Ratgeber", "lead": "Praktische Artikel für Studierende, Berufstätige und Besucher auf Wohnungssuche in Mailand.", "guides": "Wichtige Ratgeber", "latest": "Neueste Artikel", "read": "Lesen", "updated": "Aktualisiert"},
}


def _parse(path):
    raw = open(path, encoding="utf8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1); fm[k.strip()] = v.strip()
    fm["body"] = m.group(2)
    base = os.path.splitext(os.path.basename(path))[0]
    fm["slug"] = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", base)
    fm.setdefault("date", base[:10])
    fm.setdefault("updated", fm["date"])
    fm["apts"] = [x.strip() for x in fm.get("apts", "").split(",") if x.strip()]
    if fm.get("path"):
        fm["url"] = "/" + fm["path"].strip("/") + "/"
    else:
        pre = "" if fm["lang"] == "en" else fm["lang"] + "/"
        fm["url"] = f"/{pre}blog/{fm['slug']}/"
    return fm


ARTICLES = sorted((_parse(p) for p in glob.glob(os.path.join(HERE, "articles", "*.md"))
                   if os.path.basename(p)[:10] <= datetime.date.today().isoformat()),
                  key=lambda a: a["date"], reverse=True)


def page_article(a, M):
    lang = a["lang"]; T = M.C[lang]; I = INDEX[lang]
    html_body = markdown.markdown(a["body"], extensions=["tables"])
    hero = ""
    if a.get("image"):
        s, i = a["image"].split(":")
        pic = M.img(s, int(i), "(max-width:1160px) 100vw, 1160px", eager=True, alt=a["h1"]).replace("<img ", '<img style="width:100%;height:100%;object-fit:cover" ')
        hero = f'<div class="round" style="margin:10px 0 26px;aspect-ratio:21/9">{pic}</div>'
    apts = "".join(M.listing_card(lang, l) for l in a["apts"] if l in M.LISTINGS)
    side = f'<section><div class="wrap"><h2>{M.esc(T.ui["apts_for_this"])}</h2><div class="grid g3">{apts}</div></div></section>' if apts else ""
    body = f"""<section style="padding-top:20px"><div class="wrap"><span class="kicker">{I["kicker"]}</span><h1>{M.esc(a["h1"])}</h1>
<p class="muted" style="font-size:14px">{I["updated"]}: {a["updated"]} · Vito Semeraro</p>{hero}<div class="prose">{html_body}</div></div></section>{side}{M.cta_band(lang)}"""
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["h1"], "description": a["description"], "inLanguage": lang,
          "datePublished": a["date"], "dateModified": a["updated"], "mainEntityOfPage": M.SITE + a["url"],
          "author": {"@type": "Person", "name": "Vito Semeraro", "url": M.url_of(lang, "about")},
          "publisher": {"@type": "Organization", "name": "RAM – Rent Apartment Milan"}}
    if a.get("image"):
        s, i = a["image"].split(":"); ld["image"] = M.img_src(s, int(i))
    return M.layout(lang, "blog", a["title"], a["description"], body, ld=ld, canon=a["url"],
                    crumbs=[("Blog", M.path_of(lang, "blog")), (a["h1"][:60], a["url"])])


def page_index(lang, M):
    T = M.C[lang]; I = INDEX[lang]
    guides = "".join(f'<a class="feat" style="text-decoration:none;color:inherit" href="{M.path_of(lang, k)}"><h3>{M.esc(T.P[k]["nav"])} →</h3><p>{M.esc(T.P[k]["desc"])}</p></a>' for k in M.CONFIG["guides"])
    own = [a for a in ARTICLES if a["lang"] == lang] or [a for a in ARTICLES if a["lang"] == "en"]
    arts = "".join(f'<a class="feat" style="text-decoration:none;color:inherit" href="{a["url"]}"><p class="muted" style="font-size:13px;margin:0 0 6px">{a["updated"]}</p><h3>{M.esc(a["h1"])}</h3><p>{M.esc(a["description"])}</p></a>' for a in own)
    body = f"""<section style="padding-top:20px"><div class="wrap"><span class="kicker">{I["kicker"]}</span><h1>{I["h1"]}</h1><p class="lead">{I["lead"]}</p>
<h2>{I["latest"]}</h2><div class="grid g3">{arts}</div><h2>{I["guides"]}</h2><div class="grid g3">{guides}</div></div></section>{M.cta_band(lang)}"""
    return M.layout(lang, "blog", I["title"], I["desc"], body, crumbs=[("Blog", M.path_of(lang, "blog"))])
