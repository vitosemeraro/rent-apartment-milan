# AEO: risposte dirette (domanda → risposta in 40-60 parole) mostrate in cima alle guide e marcate FAQPage,
# llms.txt per i motori di risposta e lista IndexNow.
import json

QA = {
"en": {
 "nodeposit": ("Can I rent an apartment in Milan without a deposit?", "Yes. RAM rents furnished studios and flats in north-east Milan for monthly stays without the usual three-month deposit. Bills and gigabit Wi-Fi are included in one monthly price, the lease is registered, and the apartments are a few minutes from the M1 metro (Precotto and Turro)."),
 "monthly": ("How much does a monthly rental cost in Milan?", "A furnished one-bedroom flat outside the centre but on the metro typically costs €1,900–2,700 per month on the main platforms. RAM's monthly apartments on the M1 start from about €1,300 per month for the Turro studio, with all bills included and no three-month deposit."),
 "students": ("Where should students live in Milan?", "Choose by commute, not by fame. From Precotto and Turro on the M1 you reach Bicocca in about 15 minutes, Politecnico (Città Studi) in 15–20 and the Statale in 20–25. Whole furnished apartments with a registered student or transitional lease avoid shared-flat contracts and big deposits."),
 "bicocca": ("Where to stay near Bicocca University in Milan?", "Precotto borders Bicocca to the east: from Via Val di Non the university buildings are about 15 minutes away on foot, by bike or tram 7, and the M1 takes you to the Duomo in about 20 minutes. RAM offers a one-bedroom flat with desk, balcony and gigabit fibre from 28 nights."),
 "fairs": ("Where to stay for Rho Fiera and Salone del Mobile?", "Stay on the M1 red line: trains bound for Rho Fiera run from Precotto and Turro with no changes, and the same line takes you to the Duomo in the evening. RAM's Precotto home sleeps up to 8 people with two bathrooms and two kitchens, ideal for exhibitor teams."),
 "neighborhood": ("Is Precotto–Turro a good area to stay in Milan?", "Yes, for quiet and value: it is a residential area of north-east Milan along the Naviglio Martesana cycle path, with 24-hour supermarkets, the NoLo district nearby and two M1 stations (Precotto, Turro). The Duomo is about 20 minutes away and Milano Centrale about 15."),
 "contract": ("What is a transitional lease (contratto transitorio) in Italy?", "It is a lease for a temporary need such as work, an internship or study, lasting 1 to 18 months under law 431/1998, art. 5. The reason is written in the contract, which must be registered with the Agenzia delle Entrate; the registration is valid for residence and permits."),
},
"it": {
 "nodeposit": ("Si può affittare un appartamento a Milano senza deposito?", "Sì. RAM affitta monolocali e bilocali arredati a Milano nord-est per soggiorni mensili senza i soliti tre mesi di deposito. Utenze e Wi-Fi in fibra sono inclusi nel canone, il contratto è registrato e gli appartamenti sono a pochi minuti dalla M1 (Precotto e Turro)."),
 "monthly": ("Quanto costa un affitto mensile a Milano?", "Un bilocale arredato fuori dal centro ma sulla metro costa in genere 1.900–2.700 € al mese sulle principali piattaforme. Gli appartamenti mensili di RAM sulla M1 partono da circa 1.300 € al mese per il monolocale di Turro, spese incluse e senza tre mesi di deposito."),
 "students": ("Dove conviene vivere a Milano per uno studente?", "Scegli in base al tragitto, non alla fama della zona. Da Precotto e Turro sulla M1 arrivi in Bicocca in circa 15 minuti, al Politecnico (Città Studi) in 15–20 e alla Statale in 20–25. Un appartamento intero con contratto per studenti o transitorio registrato evita stanze in nero e depositi alti."),
 "bicocca": ("Dove alloggiare vicino all'Università Bicocca?", "Precotto confina con la Bicocca: da via Val di Non gli edifici dell'università sono a circa 15 minuti a piedi, in bici o con il tram 7, e con la M1 il Duomo è a circa 20 minuti. RAM offre un bilocale con scrivania, balcone e fibra gigabit da 28 notti."),
 "fairs": ("Dove dormire per Rho Fiera e il Salone del Mobile?", "Sulla linea rossa M1: da Precotto e Turro i treni diretti a Rho Fiera non richiedono cambi, e la sera la stessa linea porta in Duomo. La casa di RAM a Precotto ospita fino a 8 persone con due bagni e due cucine, ideale per i team di uno stand."),
 "neighborhood": ("Precotto e Turro sono una buona zona di Milano?", "Sì, se cerchi tranquillità e prezzi più bassi del centro: è una zona residenziale di Milano nord-est lungo la ciclabile della Martesana, con supermercati aperti 24 ore, NoLo vicino e due fermate M1 (Precotto, Turro). Il Duomo è a circa 20 minuti, la Centrale a circa 15."),
 "contract": ("Cos'è il contratto transitorio a Milano nel 2026?", "È un contratto per esigenze temporanee come lavoro, stage o studio, da 1 a 18 mesi secondo la legge 431/1998, art. 5. Il motivo va scritto e documentato, a Milano il canone segue l'accordo territoriale e il contratto va registrato all'Agenzia delle Entrate: vale per residenza e permessi di soggiorno."),
},
"es": {
 "nodeposit": ('¿Se puede alquilar un piso en Milán sin fianza?', 'Sí. RAM alquila estudios y pisos amueblados en el noreste de Milán para estancias mensuales sin los habituales tres meses de fianza. Los suministros y el Wi-Fi de fibra están incluidos en un único precio mensual, el contrato está registrado y los pisos están a pocos minutos del metro M1 (Precotto y Turro).'),
 "monthly": ('¿Cuánto cuesta un alquiler mensual en Milán?', 'Un piso amueblado de un dormitorio fuera del centro pero cerca del metro cuesta normalmente 1.900–2.700 € al mes en las principales plataformas. Los pisos mensuales de RAM en la M1 parten de unos 1.300 € al mes por el estudio de Turro, con suministros y Wi-Fi incluidos y sin tres meses de fianza.'),
 "students": ('¿Dónde conviene vivir en Milán siendo estudiante?', 'Elige por el trayecto, no por la fama del barrio. Desde Precotto y Turro en la M1 llegas a Bicocca en unos 15 minutos, al Politecnico (Città Studi) en 15–20 y a la Statale en 20–25. Un piso entero con contrato de estudiante o transitorio registrado evita habitaciones sin contrato y fianzas altas.'),
 "bicocca": ('¿Dónde alojarse cerca de la Universidad de Milano-Bicocca?', 'Precotto linda con Bicocca: desde Via Val di Non los edificios de la universidad están a unos 15 minutos a pie, en bici o con el tranvía 7, y con la M1 llegas al Duomo en unos 20 minutos. RAM ofrece un piso de un dormitorio con escritorio, balcón y fibra gigabit desde 28 noches.'),
 "fairs": ('¿Dónde alojarse para Rho Fiera y el Salone del Mobile?', 'En la línea roja M1: desde Precotto y Turro los trenes con destino Rho Fiera llegan sin transbordos, y por la noche la misma línea te lleva al Duomo. La casa de RAM en Precotto aloja hasta 8 personas con dos baños y dos cocinas, ideal para los equipos de un stand.'),
 "neighborhood": ('¿Precotto y Turro son una buena zona de Milán?', 'Sí, si buscas tranquilidad y buenos precios: es una zona residencial del noreste de Milán junto al carril bici de la Martesana, con supermercados abiertos 24 horas, el barrio NoLo cerca y dos paradas de la M1 (Precotto, Turro). El Duomo está a unos 20 minutos y Milano Centrale a unos 15.'),
 "contract": ('¿Qué es el contrato de alquiler transitorio en Italia?', 'Es un contrato para una necesidad temporal como trabajo, prácticas o estudios, de 1 a 18 meses según la ley 431/1998, art. 5. El motivo se escribe en el contrato, que debe registrarse en la Agenzia delle Entrate; el registro sirve para la residencia y los permisos de residencia.'),
},
"fr": {
 "nodeposit": ('Peut-on louer un appartement à Milan sans caution ?', 'Oui. RAM loue des studios et des appartements meublés dans le nord-est de Milan pour des séjours au mois, sans les trois mois de caution habituels. Les charges et le Wi-Fi fibre sont inclus dans un seul prix mensuel, le bail est enregistré et les logements sont à quelques minutes du métro M1 (Precotto et Turro).'),
 "monthly": ('Combien coûte une location au mois à Milan ?', 'Un deux-pièces meublé hors du centre mais proche du métro coûte en général 1 900–2 700 € par mois sur les principales plateformes. Les appartements au mois de RAM sur la M1 démarrent à environ 1 300 € par mois pour le studio de Turro, charges et Wi-Fi inclus, sans trois mois de caution.'),
 "students": ('Où vivre à Milan quand on est étudiant ?', 'Choisissez selon le trajet, pas selon la réputation du quartier. Depuis Precotto et Turro sur la M1, vous rejoignez Bicocca en 15 minutes environ, le Politecnico (Città Studi) en 15–20 et la Statale en 20–25. Un appartement entier avec un bail étudiant ou transitoire enregistré évite les chambres sans contrat et les grosses cautions.'),
 "bicocca": ("Où se loger près de l'université de Milano-Bicocca ?", "Precotto borde Bicocca : depuis la Via Val di Non, les bâtiments de l'université sont à environ 15 minutes à pied, à vélo ou en tram 7, et la M1 vous amène au Duomo en 20 minutes environ. RAM propose un deux-pièces avec bureau, balcon et fibre gigabit à partir de 28 nuits."),
 "fairs": ('Où dormir pour Rho Fiera et le Salone del Mobile ?', "Sur la ligne rouge M1 : depuis Precotto et Turro, les trains en direction de Rho Fiera arrivent sans changement, et le soir la même ligne vous ramène au Duomo. La maison de RAM à Precotto accueille jusqu'à 8 personnes avec deux salles de bain et deux cuisines, idéale pour l'équipe d'un stand."),
 "neighborhood": ('Precotto et Turro, est-ce un bon quartier de Milan ?', "Oui, pour le calme et les prix : c'est un quartier résidentiel du nord-est de Milan le long de la piste cyclable de la Martesana, avec des supermarchés ouverts 24 h/24, le quartier NoLo tout proche et deux stations de M1 (Precotto, Turro). Le Duomo est à environ 20 minutes et Milano Centrale à 15."),
 "contract": ("Qu'est-ce que le bail transitoire (contratto transitorio) en Italie ?", "C'est un bail pour un besoin temporaire comme un travail, un stage ou des études, de 1 à 18 mois selon la loi 431/1998, art. 5. Le motif est écrit dans le contrat, qui doit être enregistré auprès de l'Agenzia delle Entrate ; l'enregistrement est valable pour la résidence et les titres de séjour."),
},
"de": {
 "nodeposit": ('Kann man in Mailand eine Wohnung ohne Kaution mieten?', 'Ja. RAM vermietet möblierte Studios und Wohnungen im Nordosten Mailands für Aufenthalte ab einem Monat, ohne die üblichen drei Monatsmieten Kaution. Nebenkosten und Glasfaser-WLAN sind im Monatspreis enthalten, der Mietvertrag wird registriert, und die Wohnungen liegen wenige Minuten von der U-Bahn M1 (Precotto und Turro).'),
 "monthly": ('Was kostet eine Wohnung auf Zeit in Mailand pro Monat?', 'Eine möblierte Zweizimmerwohnung außerhalb des Zentrums, aber an der U-Bahn, kostet auf den großen Plattformen meist 1.900–2.700 € im Monat. Die Monatswohnungen von RAM an der M1 beginnen bei etwa 1.300 € im Monat für das Studio in Turro, mit Nebenkosten und WLAN und ohne drei Monatsmieten Kaution.'),
 "students": ('Wo sollten Studierende in Mailand wohnen?', 'Wählen Sie nach dem Weg zur Uni, nicht nach dem Ruf des Viertels. Von Precotto und Turro an der M1 erreichen Sie Bicocca in etwa 15 Minuten, das Politecnico (Città Studi) in 15–20 und die Statale in 20–25. Eine ganze Wohnung mit registriertem Studenten- oder Zeitmietvertrag vermeidet Zimmer ohne Vertrag und hohe Kautionen.'),
 "bicocca": ('Wo wohnen in der Nähe der Universität Mailand-Bicocca?', 'Precotto grenzt an Bicocca: Von der Via Val di Non sind die Universitätsgebäude zu Fuß, mit dem Rad oder der Tram 7 etwa 15 Minuten entfernt, und mit der M1 sind Sie in rund 20 Minuten am Duomo. RAM bietet eine Zweizimmerwohnung mit Schreibtisch, Balkon und Gigabit-Glasfaser ab 28 Nächten.'),
 "fairs": ('Wo übernachten für Rho Fiera und den Salone del Mobile?', 'An der roten Linie M1: Von Precotto und Turro fahren die Züge Richtung Rho Fiera ohne Umsteigen, und abends bringt Sie dieselbe Linie zum Duomo. Das RAM-Haus in Precotto bietet Platz für bis zu 8 Personen mit zwei Bädern und zwei Küchen, ideal für ein Messestand-Team.'),
 "neighborhood": ('Sind Precotto und Turro eine gute Wohngegend in Mailand?', 'Ja, wenn Sie Ruhe und günstigere Preise suchen: ein Wohnviertel im Nordosten Mailands am Radweg entlang der Martesana, mit 24-Stunden-Supermärkten, dem Viertel NoLo in der Nähe und zwei M1-Stationen (Precotto, Turro). Der Duomo ist etwa 20 Minuten entfernt, Milano Centrale etwa 15.'),
 "contract": ('Was ist ein Zeitmietvertrag (contratto transitorio) in Italien?', 'Ein Mietvertrag für einen vorübergehenden Bedarf wie Arbeit, Praktikum oder Studium, mit 1 bis 18 Monaten Laufzeit nach Gesetz 431/1998, Art. 5. Der Grund steht im Vertrag, der bei der Agenzia delle Entrate registriert werden muss; die Registrierung gilt für Wohnsitz und Aufenthaltstitel.'),
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
    blog = getattr(M, "BLOG", None)
    if blog and blog.ARTICLES:
        out += ["", "## Articles"]
        for a in blog.ARTICLES:
            title = a.get("h1") or a.get("title", "").split(" | ")[0]
            out.append(f"- [{title}]({SITE}{a['url']}) ({a['lang']}, {a['updated']}): {a.get('description', '')}")
    out += ["", "## Other languages", f"- Italiano: {SITE}/it/", f"- Español: {SITE}/es/", f"- Français: {SITE}/fr/", f"- Deutsch: {SITE}/de/", "",
            "## Booking", f"- Each apartment page has a calendar with live availability and an instant quote (nightly price, cleaning, discounts and Milan tourist tax). Requests go to {cfg['email']}.", ""]
    return "\n".join(out)


def indexnow_payload(M, urls, key):
    host = M.SITE.replace("https://", "")
    return json.dumps({"host": host, "key": key, "keyLocation": f"{M.SITE}/{key}.txt", "urlList": urls[:10000]})
