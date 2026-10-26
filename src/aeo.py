# AEO: risposte dirette (domanda → risposta in 40-60 parole) mostrate in cima alle guide e marcate FAQPage,
# llms.txt per i motori di risposta e lista IndexNow.
import json

QA = {
"en": {
 "nodeposit": ("Can I rent an apartment in Milan without a deposit?", "Yes. RAM rents furnished studios and flats in north-east Milan for monthly stays without the usual three-month deposit. Bills and gigabit Wi-Fi are included in one monthly price, the lease is registered, and the apartments are a few minutes from the M1 metro (Precotto and Turro)."),
 "monthly": ("How much does a monthly rental cost in Milan?", "A furnished one-bedroom flat outside the centre but on the metro typically costs €1,900–2,700 per month on the main platforms. RAM's monthly apartments on the M1 start from about €1,580 per month for the Turro studio, with bills and Wi-Fi included and no three-month deposit."),
 "students": ("Where should students live in Milan?", "Choose by commute, not by fame. From Precotto and Turro on the M1 you reach Bicocca in about 15 minutes, Politecnico (Città Studi) in 15–20 and the Statale in 20–25. Whole furnished apartments with a registered student or transitional lease avoid shared-flat contracts and big deposits."),
 "bicocca": ("Where to stay near Bicocca University in Milan?", "Precotto borders Bicocca to the east: from Via Val di Non the university buildings are about 15 minutes away on foot, by bike or tram 7, and the M1 takes you to the Duomo in about 20 minutes. RAM offers a one-bedroom flat with desk, balcony and gigabit fibre from 28 nights."),
 "fairs": ("Where to stay for Rho Fiera and Salone del Mobile?", "Stay on the M1 red line: trains bound for Rho Fiera run from Precotto and Turro with no changes, and the same line takes you to the Duomo in the evening. RAM's Precotto home sleeps up to 8 people with two bathrooms and two kitchens, ideal for exhibitor teams."),
 "neighborhood": ("Is Precotto–Turro a good area to stay in Milan?", "Yes, for quiet and value: it is a residential area of north-east Milan along the Naviglio Martesana cycle path, with 24-hour supermarkets, the NoLo district nearby and two M1 stations (Precotto, Turro). The Duomo is about 20 minutes away and Milano Centrale about 15."),
 "contract": ("What is a transitional lease (contratto transitorio) in Italy?", "It is a lease for a temporary need such as work, an internship or study, lasting 1 to 18 months under law 431/1998, art. 5. The reason is written in the contract, which must be registered with the Agenzia delle Entrate; the registration is valid for residence and permits."),
},
"it": {
 "nodeposit": ("Si può affittare un appartamento a Milano senza deposito?", "Sì. RAM affitta monolocali e bilocali arredati a Milano nord-est per soggiorni mensili senza i soliti tre mesi di deposito. Utenze e Wi-Fi in fibra sono inclusi nel canone, il contratto è registrato e gli appartamenti sono a pochi minuti dalla M1 (Precotto e Turro)."),
 "monthly": ("Quanto costa un affitto mensile a Milano?", "Un bilocale arredato fuori dal centro ma sulla metro costa in genere 1.900–2.700 € al mese sulle principali piattaforme. Gli appartamenti mensili di RAM sulla M1 partono da circa 1.580 € al mese per il monolocale di Turro, con utenze e Wi-Fi inclusi e senza tre mesi di deposito."),
 "students": ("Dove conviene vivere a Milano per uno studente?", "Scegli in base al tragitto, non alla fama della zona. Da Precotto e Turro sulla M1 arrivi in Bicocca in circa 15 minuti, al Politecnico (Città Studi) in 15–20 e alla Statale in 20–25. Un appartamento intero con contratto per studenti o transitorio registrato evita stanze in nero e depositi alti."),
 "bicocca": ("Dove alloggiare vicino all'Università Bicocca?", "Precotto confina con la Bicocca: da via Val di Non gli edifici dell'università sono a circa 15 minuti a piedi, in bici o con il tram 7, e con la M1 il Duomo è a circa 20 minuti. RAM offre un bilocale con scrivania, balcone e fibra gigabit da 28 notti."),
 "fairs": ("Dove dormire per Rho Fiera e il Salone del Mobile?", "Sulla linea rossa M1: da Precotto e Turro i treni diretti a Rho Fiera non richiedono cambi, e la sera la stessa linea porta in Duomo. La casa di RAM a Precotto ospita fino a 8 persone con due bagni e due cucine, ideale per i team di uno stand."),
 "neighborhood": ("Precotto e Turro sono una buona zona di Milano?", "Sì, se cerchi tranquillità e prezzi più bassi del centro: è una zona residenziale di Milano nord-est lungo la ciclabile della Martesana, con supermercati aperti 24 ore, NoLo vicino e due fermate M1 (Precotto, Turro). Il Duomo è a circa 20 minuti, la Centrale a circa 15."),
 "contract": ("Cos'è il contratto di locazione transitorio?", "È un contratto per esigenze temporanee come lavoro, stage o studio, da 1 a 18 mesi secondo la legge 431/1998, art. 5. Il motivo va scritto nel contratto, che deve essere registrato all'Agenzia delle Entrate: la registrazione vale per residenza e permessi di soggiorno."),
},
}


def answer_box(lang, key, esc):
    qa = QA.get(lang, {}).get(key)
    if not qa:
        return "", None
    q, a = qa
    html = f'<div class="tip" style="border-left-color:var(--acc)"><p style="margin:0 0 4px;font-weight:700">{esc(q)}</p><p style="margin:0">{esc(a)}</p></div>'
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}]}
    return html, ld


def llms_txt(M):
    C, SITE, path_of, LISTINGS, PRICING = M.C, M.SITE, M.path_of, M.LISTINGS, M.PRICING
    T = C["en"]; cfg = M.CONFIG
    out = ["# Rent Apartment Milan (RAM)", "",
           "> Furnished apartments in north-east Milan (Precotto and Turro, M1 red line) for short stays and monthly stays, managed personally by Vito Semeraro. Book directly with the host: no agency fee, monthly stays with bills included, registered contract and no three-month deposit.", "",
           f"- Contact: {cfg['email']}, {cfg['phone']}", f"- Address: {cfg['street']}, {cfg['zip']} Milano, Italy", "- Languages: English, Italiano, Español, Français, Deutsch", "",
           "## Apartments"]
    for lid, L in LISTINGS.items():
        t = T.L[lid]; p = PRICING.get(lid, {})
        if p.get("soon"):
            price = "opening soon"
        elif p.get("min_nights", 1) >= 28:
            price = f"monthly stays from about €{M.month_price(lid)}/month, minimum {p['min_nights']} nights"
        else:
            price = f"from €{p['base']}/night, minimum {p['min_nights']} nights, up to {p['max_guests']} guests"
        out.append(f"- [{t['name']}]({SITE}{path_of('en', 'l_' + lid)}): {t['card']} {price}.")
    out += ["", "## Guides"]
    for k in cfg["guides"]:
        out.append(f"- [{T.P[k]['nav']}]({SITE}{path_of('en', k)}): {T.P[k]['desc']}")
    out += ["", "## Other languages", f"- Italiano: {SITE}/it/", f"- Español: {SITE}/es/", f"- Français: {SITE}/fr/", f"- Deutsch: {SITE}/de/", "",
            "## Booking", f"- Each apartment page has a calendar with live availability and an instant quote (nightly price, cleaning, discounts and Milan tourist tax). Requests go to {cfg['email']}.", ""]
    return "\n".join(out)


def indexnow_payload(M, urls, key):
    host = M.SITE.replace("https://", "")
    return json.dumps({"host": host, "key": key, "keyLocation": f"{M.SITE}/{key}.txt", "urlList": urls[:10000]})
