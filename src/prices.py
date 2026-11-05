# Pagina dati GEO/AEO "prezzi mensili per zona": numeri calcolati a ogni build da data/pricing.json.
# Segnaposto sostituiti in build.py: [[turro]] [[vdn]] canone mensile, [[mm]] prezzo/notte Precotto,
# [[date]] data di aggiornamento, [[path:<chiave>]] link interni, <!--PRICES--> e <!--SHORT--> tabelle.
D = {
"en": ("milan-monthly-rent-prices-by-area", {
 "nav": "Monthly rent prices by area", "kicker": "Data", "article": True, "img": ("valdinon", 5), "apts": ["turro", "vdn", "mm"],
 "title": "Monthly rent prices in Milan by area: RAM data",
 "desc": "Current monthly rent of RAM's furnished flats in Turro and Precotto (Milan, M1): bills and Wi-Fi included, cleaning and minimum stay, updated.",
 "h1": "Monthly rent prices in Milan by area",
 "lead": "Prices of RAM's furnished apartments in north-east Milan, calculated from the current rates. Updated [[date]].",
 "html": """<p><strong>A furnished studio in Turro (M1) costs from €[[turro]] a month with RAM, and a one-bedroom flat in Precotto near Bicocca from €[[vdn]] a month. Both prices include bills and gigabit Wi-Fi; the only extra is a one-off final cleaning. Stays start from 28–30 nights, with no three-month deposit.</strong></p>
<!--PRICES-->
<h2>How are these prices calculated?</h2><p>Each figure is the current nightly rate × 30 nights, minus the monthly discount of that apartment, rounded to the nearest €10. The rates are the same ones used by the booking calendar on each apartment page, so this table changes when the rates change.</p>
<h2>What does a short stay cost in Precotto?</h2><p>The flat for up to 8 guests in Precotto is rented for short and medium stays, priced per night:</p>
<!--SHORT-->
<h2>What is included and what is not?</h2><ul><li>Included in the monthly rent: electricity, gas, heating, water and gigabit Wi-Fi.</li><li>Paid once: the final cleaning shown in the table.</li><li>Not required: the usual three months' deposit and the agency fee (<a href="[[path:nodeposit]]">how renting without a deposit works</a>).</li></ul>
<p>For contracts, areas and practical tips read the <a href="[[path:monthly]]">guide to monthly rentals in Milan</a> and the <a href="[[path:neighborhood]]">Precotto and Turro neighbourhood guide</a>.</p>""",
 "faq": [
  ("How much is a monthly rent for a furnished studio in Milan with RAM?", "The studio in Turro, on the M1 red line, costs from €[[turro]] a month with bills and Wi-Fi included, plus a one-off final cleaning."),
  ("Is there a deposit?", "No three-month deposit is required. You pay the monthly rent and the final cleaning."),
  ("What is the minimum stay for monthly prices?", "30 nights for the studio in Turro and 28 nights for the one-bedroom in Val di Non (Precotto)."),
  ("How do I get the exact price for my dates?", "Use the calendar on the apartment page or <a href=\"[[path:contact]]\">send your dates</a>: the quote shows the total with no hidden costs."),
 ]}),
"it": ("prezzi-affitto-mensile-milano-per-zona", {
 "nav": "Prezzi mensili per zona", "kicker": "Dati", "article": True, "img": ("valdinon", 5), "apts": ["turro", "vdn", "mm"],
 "title": "Prezzi affitto mensile a Milano per zona: dati RAM",
 "desc": "Canone mensile attuale dei monolocali e bilocali arredati RAM a Turro e Precotto (Milano, M1): utenze e Wi-Fi inclusi, pulizia e soggiorno minimo.",
 "h1": "Prezzi dell'affitto mensile a Milano per zona",
 "lead": "I prezzi degli appartamenti arredati di RAM a Milano nord-est, calcolati dalle tariffe attuali. Aggiornati il [[date]].",
 "html": """<p><strong>Con RAM un monolocale arredato a Turro (M1) costa da [[turro]] € al mese e un bilocale a Precotto, vicino alla Bicocca, da [[vdn]] € al mese. In entrambi i prezzi sono incluse utenze e Wi-Fi in fibra; l'unico extra è la pulizia finale, una volta sola. Si parte da 28–30 notti, senza tre mesi di deposito.</strong></p>
<!--PRICES-->
<h2>Come sono calcolati questi prezzi?</h2><p>Ogni cifra è la tariffa attuale per notte × 30 notti, meno lo sconto mensile di quell'appartamento, arrotondata ai 10 €. Sono le stesse tariffe del calendario di prenotazione di ogni scheda: quando cambiano, cambia anche questa tabella.</p>
<h2>Quanto costa un soggiorno breve a Precotto?</h2><p>L'appartamento da 8 ospiti di Precotto si affitta per soggiorni brevi e medi, con prezzo a notte:</p>
<!--SHORT-->
<h2>Cosa è incluso e cosa no?</h2><ul><li>Inclusi nel canone: luce, gas, riscaldamento, acqua e Wi-Fi in fibra.</li><li>Una volta sola: la pulizia finale indicata in tabella.</li><li>Non richiesti: i soliti tre mesi di deposito e l'agenzia (<a href="[[path:nodeposit]]">come funziona l'affitto senza deposito</a>).</li></ul>
<p>Per contratti, zone e consigli pratici leggi la <a href="[[path:monthly]]">guida agli affitti mensili a Milano</a> e la <a href="[[path:neighborhood]]">guida al quartiere Precotto e Turro</a>.</p>""",
 "faq": [
  ("Quanto costa al mese un monolocale arredato a Milano con RAM?", "Il monolocale di Turro, sulla linea rossa M1, costa da [[turro]] € al mese con utenze e Wi-Fi inclusi, più la pulizia finale una volta sola."),
  ("Serve il deposito?", "Non servono i tre mesi di deposito. Paghi il canone mensile e la pulizia finale."),
  ("Qual è il soggiorno minimo per i prezzi mensili?", "30 notti per il monolocale di Turro e 28 notti per il bilocale di via Val di Non (Precotto)."),
  ("Come ottengo il prezzo esatto per le mie date?", "Usa il calendario nella scheda dell'appartamento o <a href=\"[[path:contact]]\">mandami le date</a>: il preventivo mostra il totale senza costi nascosti."),
 ]}),
"es": ("precios-alquiler-mensual-milan-por-zona", {
 "nav": "Precios mensuales por zona", "kicker": "Datos", "article": True, "img": ("valdinon", 5), "apts": ["turro", "vdn", "mm"],
 "title": "Precios de alquiler mensual en Milán por zona | RAM",
 "desc": "Alquiler mensual actual de los pisos amueblados de RAM en Turro y Precotto (Milán, M1): suministros y wifi incluidos, limpieza final y estancia mínima.",
 "h1": "Precios del alquiler mensual en Milán por zona",
 "lead": "Precios de los apartamentos amueblados de RAM en el noreste de Milán, calculados con las tarifas actuales. Actualizado el [[date]].",
 "html": """<p><strong>Con RAM un estudio amueblado en Turro (M1) cuesta desde [[turro]] € al mes y un piso de un dormitorio en Precotto, cerca de Bicocca, desde [[vdn]] € al mes. Ambos precios incluyen suministros y wifi; el único extra es la limpieza final, una sola vez. Estancias desde 28–30 noches, sin fianza de tres meses.</strong></p>
<!--PRICES-->
<h2>¿Cómo se calculan estos precios?</h2><p>Cada cifra es la tarifa actual por noche × 30 noches, menos el descuento mensual de ese apartamento, redondeada a 10 €. Son las mismas tarifas del calendario de reservas de cada ficha.</p>
<h2>¿Cuánto cuesta una estancia corta en Precotto?</h2><p>El piso para 8 huéspedes de Precotto se alquila para estancias cortas y medias, con precio por noche:</p>
<!--SHORT-->
<h2>¿Qué está incluido?</h2><ul><li>Incluidos: luz, gas, calefacción, agua y wifi.</li><li>Una sola vez: la limpieza final de la tabla.</li><li>No se piden: los tres meses de fianza ni la agencia (<a href="[[path:nodeposit]]">pisos sin fianza</a>).</li></ul>
<p>Más información en la <a href="[[path:monthly]]">guía de alquileres mensuales en Milán</a> y la <a href="[[path:neighborhood]]">guía del barrio</a>.</p>""",
 "faq": [
  ("¿Cuánto cuesta al mes un estudio amueblado en Milán con RAM?", "El estudio de Turro, en la línea roja M1, cuesta desde [[turro]] € al mes con suministros y wifi incluidos, más la limpieza final."),
  ("¿Hay que pagar fianza?", "No se piden tres meses de fianza. Pagas el alquiler mensual y la limpieza final."),
  ("¿Cuál es la estancia mínima?", "30 noches para el estudio de Turro y 28 noches para el piso de Val di Non (Precotto)."),
  ("¿Cómo obtengo el precio exacto?", "Usa el calendario de la ficha o <a href=\"[[path:contact]]\">envíame tus fechas</a>."),
 ]}),
"fr": ("prix-location-mensuelle-milan-par-quartier", {
 "nav": "Prix mensuels par quartier", "kicker": "Données", "article": True, "img": ("valdinon", 5), "apts": ["turro", "vdn", "mm"],
 "title": "Prix de location mensuelle à Milan par quartier | RAM",
 "desc": "Loyer mensuel actuel des logements meublés RAM à Turro et Precotto (Milan, M1) : charges et Wi-Fi inclus, ménage final et durée minimale de séjour.",
 "h1": "Prix de la location mensuelle à Milan par quartier",
 "lead": "Les prix des appartements meublés de RAM au nord-est de Milan, calculés à partir des tarifs actuels. Mis à jour le [[date]].",
 "html": """<p><strong>Avec RAM, un studio meublé à Turro (M1) coûte à partir de [[turro]] € par mois et un deux-pièces à Precotto, près de Bicocca, à partir de [[vdn]] € par mois. Les deux prix incluent les charges et le Wi-Fi ; seul le ménage final est en plus, une seule fois. Séjours à partir de 28–30 nuits, sans caution de trois mois.</strong></p>
<!--PRICES-->
<h2>Comment ces prix sont-ils calculés ?</h2><p>Chaque chiffre correspond au tarif actuel par nuit × 30 nuits, moins la remise mensuelle de l'appartement, arrondi à 10 €. Ce sont les tarifs du calendrier de réservation de chaque fiche.</p>
<h2>Combien coûte un court séjour à Precotto ?</h2><p>L'appartement pour 8 voyageurs à Precotto se loue pour des séjours courts et moyens, au prix par nuit :</p>
<!--SHORT-->
<h2>Qu'est-ce qui est inclus ?</h2><ul><li>Inclus : électricité, gaz, chauffage, eau et Wi-Fi.</li><li>Une seule fois : le ménage final indiqué.</li><li>Non demandés : trois mois de caution et frais d'agence (<a href="[[path:nodeposit]]">appartements sans caution</a>).</li></ul>
<p>Plus d'informations dans le <a href="[[path:monthly]]">guide des locations mensuelles à Milan</a> et le <a href="[[path:neighborhood]]">guide du quartier</a>.</p>""",
 "faq": [
  ("Combien coûte par mois un studio meublé à Milan avec RAM ?", "Le studio de Turro, sur la ligne rouge M1, coûte à partir de [[turro]] € par mois, charges et Wi-Fi inclus, plus le ménage final."),
  ("Faut-il une caution ?", "Pas de caution de trois mois. Vous payez le loyer mensuel et le ménage final."),
  ("Quelle est la durée minimale ?", "30 nuits pour le studio de Turro et 28 nuits pour le deux-pièces de Val di Non (Precotto)."),
  ("Comment obtenir le prix exact ?", "Utilisez le calendrier de la fiche ou <a href=\"[[path:contact]]\">envoyez-moi vos dates</a>."),
 ]}),
"de": ("monatsmiete-mailand-preise-nach-stadtteil", {
 "nav": "Monatspreise nach Stadtteil", "kicker": "Daten", "article": True, "img": ("valdinon", 5), "apts": ["turro", "vdn", "mm"],
 "title": "Monatsmiete in Mailand: Preise nach Stadtteil | RAM",
 "desc": "Aktuelle Monatsmiete der möblierten RAM-Wohnungen in Turro und Precotto (Mailand, M1): Nebenkosten und WLAN inklusive, Endreinigung, Mindestaufenthalt.",
 "h1": "Monatsmiete in Mailand nach Stadtteil",
 "lead": "Preise der möblierten RAM-Wohnungen im Nordosten Mailands, berechnet aus den aktuellen Tarifen. Stand: [[date]].",
 "html": """<p><strong>Bei RAM kostet ein möbliertes Studio in Turro (M1) ab [[turro]] € im Monat und eine Zwei-Zimmer-Wohnung in Precotto nahe Bicocca ab [[vdn]] € im Monat. Beide Preise enthalten Nebenkosten und WLAN; extra ist nur die einmalige Endreinigung. Aufenthalte ab 28–30 Nächten, ohne drei Monatsmieten Kaution.</strong></p>
<!--PRICES-->
<h2>Wie werden die Preise berechnet?</h2><p>Jeder Wert ist der aktuelle Nachtpreis × 30 Nächte, abzüglich des Monatsrabatts der Wohnung, auf 10 € gerundet. Es sind dieselben Tarife wie im Buchungskalender jeder Wohnung.</p>
<h2>Was kostet ein kurzer Aufenthalt in Precotto?</h2><p>Die Wohnung für bis zu 8 Gäste in Precotto wird für kurze und mittlere Aufenthalte vermietet, mit Preis pro Nacht:</p>
<!--SHORT-->
<h2>Was ist inklusive?</h2><ul><li>Inklusive: Strom, Gas, Heizung, Wasser und WLAN.</li><li>Einmalig: die Endreinigung aus der Tabelle.</li><li>Nicht verlangt: drei Monatsmieten Kaution und Maklergebühr (<a href="[[path:nodeposit]]">Wohnungen ohne Kaution</a>).</li></ul>
<p>Mehr im <a href="[[path:monthly]]">Ratgeber Monatsmiete in Mailand</a> und im <a href="[[path:neighborhood]]">Stadtteil-Ratgeber</a>.</p>""",
 "faq": [
  ("Was kostet ein möbliertes Studio in Mailand bei RAM im Monat?", "Das Studio in Turro an der roten Linie M1 kostet ab [[turro]] € im Monat inklusive Nebenkosten und WLAN, plus Endreinigung."),
  ("Muss ich eine Kaution zahlen?", "Keine drei Monatsmieten Kaution. Sie zahlen die Monatsmiete und die Endreinigung."),
  ("Wie lange ist der Mindestaufenthalt?", "30 Nächte für das Studio in Turro und 28 Nächte für die Wohnung in der Via Val di Non (Precotto)."),
  ("Wie erhalte ich den genauen Preis?", "Nutzen Sie den Kalender der Wohnung oder <a href=\"[[path:contact]]\">senden Sie mir Ihre Daten</a>."),
 ]}),
}

SHORT = {
 "en": (["Apartment", "Area", "Guests", "Nightly rate", "Weekend", "Discounts", "Final cleaning", "Minimum stay"], "from €{b}", "€{w}", "{wk}% weekly, {mo}% monthly", "€{c}", "{n} nights", "Rate for up to {x} guests; €{f} per night for each extra guest."),
 "it": (["Appartamento", "Zona", "Ospiti", "Prezzo a notte", "Weekend", "Sconti", "Pulizia finale", "Soggiorno minimo"], "da {b} €", "{w} €", "{wk}% settimanale, {mo}% mensile", "{c} €", "{n} notti", "Prezzo fino a {x} ospiti; {f} € a notte per ogni ospite in più."),
 "es": (["Apartamento", "Zona", "Huéspedes", "Precio por noche", "Fin de semana", "Descuentos", "Limpieza final", "Estancia mínima"], "desde {b} €", "{w} €", "{wk}% semanal, {mo}% mensual", "{c} €", "{n} noches", "Precio hasta {x} huéspedes; {f} € por noche por cada huésped adicional."),
 "fr": (["Appartement", "Quartier", "Voyageurs", "Prix par nuit", "Week-end", "Remises", "Ménage final", "Séjour minimum"], "à partir de {b} €", "{w} €", "{wk} % semaine, {mo} % mois", "{c} €", "{n} nuits", "Tarif jusqu'à {x} voyageurs ; {f} € par nuit par voyageur supplémentaire."),
 "de": (["Wohnung", "Stadtteil", "Gäste", "Preis pro Nacht", "Wochenende", "Rabatte", "Endreinigung", "Mindestaufenthalt"], "ab {b} €", "{w} €", "{wk} % Woche, {mo} % Monat", "{c} €", "{n} Nächte", "Preis bis {x} Gäste; {f} € pro Nacht für jeden weiteren Gast."),
}
