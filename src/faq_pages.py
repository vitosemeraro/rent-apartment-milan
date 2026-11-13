# FAQ (3-4 domande) con markup FAQPage sulle guide principali: senza deposito, affitti mensili, studenti.
# Solo fatti già presenti nel sito: prezzi da pricing.json via [[turro]]/[[vdn]], soggiorni minimi da pricing.json,
# contratti e costi dalle guide. Il markup viene unito alla risposta diretta di aeo.py in un solo FAQPage.
FAQ = {
"it": {
 "nodeposit": [
  ("Quanto costa un appartamento senza deposito con RAM?", "Il monolocale di Turro costa [[turro]] € al mese e il bilocale di via Val di Non [[vdn]] € al mese, con luce, gas, riscaldamento, acqua e Wi-Fi inclusi. Non ci sono tre mensilità di deposito né costi di agenzia."),
  ("Come si paga se non c'è deposito?", "Le modalità di pagamento vengono concordate nel contratto, che è registrato all'Agenzia delle Entrate. Non blocchi tre mesi di canone in anticipo."),
  ("Il contratto senza deposito vale per la residenza?", "Sì. Per soggiorni oltre i 30 giorni firmiamo un <a href=\"[[path:contract]]\">contratto transitorio</a> o per studenti e lo registriamo all'Agenzia delle Entrate: vale per residenza e permesso di soggiorno."),
  ("Affittate stanze senza deposito?", "No, solo appartamenti interi: monolocali e bilocali con cucina e bagno tutti tuoi, per una o due persone."),
  ("Quanto deposito può chiedere per legge un proprietario a Milano?", "Al massimo tre mensilità del canone: lo stabilisce l'articolo 11 della legge 392/1978, che vale in tutta Italia. Il deposito matura interessi legali e va restituito a fine contratto. Su un canone di 1.500 € al mese vuol dire fino a 4.500 € bloccati prima di entrare."),
 ],
 "monthly": [
  ("Qual è il soggiorno minimo per un affitto mensile?", "28 notti per il bilocale di via Val di Non e 30 notti per il monolocale di Turro. Il bilocale comfort di Precotto si affitta anche per soggiorni brevi, da 2 notti."),
  ("Cosa è incluso nel canone mensile?", "Luce, gas, riscaldamento, acqua e Wi-Fi in fibra sono inclusi. Si aggiunge solo la pulizia finale, indicata nella tabella dei prezzi."),
  ("Con un affitto mensile si paga la tassa di soggiorno?", "No. La tassa di soggiorno del Comune di Milano vale per i soggiorni sotto i 30 notti e non è dovuta per i contratti mensili."),
  ("Con quanto anticipo conviene cercare casa?", "Inizia 4–8 settimane prima dell'arrivo. Settembre, gennaio e febbraio sono i mesi più richiesti per università e fiere."),
 ],
 "students": [
  ("Quanto dura il contratto per studenti universitari?", "Da 6 a 36 mesi, per chi è iscritto a un'università in un comune diverso da quello di residenza. Per un semestre o l'Erasmus si usa il <a href=\"[[path:contract]]\">contratto transitorio</a> con motivo di studio documentato."),
  ("Le utenze sono incluse nell'affitto per studenti?", "Con RAM sì: luce, gas, riscaldamento, acqua e Wi-Fi sono nel canone. Altrove Wi-Fi, riscaldamento e utenze possono pesare 150–250 € al mese."),
  ("Posso dividere l'appartamento con un compagno di corso?", "Sì. Il monolocale di Turro e il bilocale di via Val di Non ospitano fino a 2 persone, e sono appartamenti interi che non condividi con altri."),
  ("Quanto costa un alloggio per studenti con RAM?", "Il monolocale di Turro costa [[turro]] € al mese e il bilocale di via Val di Non [[vdn]] € al mese, utenze incluse e senza tre mesi di deposito."),
 ],
},
"en": {
 "nodeposit": [
  ("How much does a no-deposit apartment cost with RAM?", "The Turro studio costs €[[turro]] per month and the Via Val di Non one-bedroom flat €[[vdn]] per month, with electricity, gas, heating, water and Wi-Fi included. There is no three-month deposit and no agency fee."),
  ("How do I pay if there is no deposit?", "Payment terms are agreed in the contract, which is registered with the Agenzia delle Entrate. You don't block three months' rent up front."),
  ("Is a no-deposit lease valid for residence?", "Yes. For stays over 30 days we sign a <a href=\"[[path:contract]]\">transitional</a> or student lease and register it with the Agenzia delle Entrate: it is valid for residence and permits."),
  ("Do you rent rooms with no deposit?", "No, only whole apartments: studios and one-bedroom flats with your own kitchen and bathroom, for one or two people."),
 ],
 "monthly": [
  ("What is the minimum stay for a monthly rental?", "28 nights for the Via Val di Non flat and 30 nights for the Turro studio. The comfort flat in Precotto is also rented for short stays, from 2 nights."),
  ("What is included in the monthly price?", "Electricity, gas, heating, water and fibre Wi-Fi are included. Only the final cleaning is added, as shown in the price table."),
  ("Do I pay the tourist tax on a monthly stay?", "No. The City of Milan tourist tax applies to stays of less than 30 nights and is not due for monthly contracts."),
  ("How far in advance should I look for a flat?", "Start 4–8 weeks before arrival. September, January and February are the busiest months because of universities and trade fairs."),
 ],
 "students": [
  ("How long is a student lease in Italy?", "6 to 36 months, for students enrolled at a university in a different municipality from their residence. For a semester or Erasmus a <a href=\"[[path:contract]]\">transitional lease</a> with a documented study reason is used."),
  ("Are bills included in student rentals?", "With RAM, yes: electricity, gas, heating, water and Wi-Fi are in the rent. Elsewhere Wi-Fi, heating and utilities can add €150–250 per month."),
  ("Can I share the apartment with a classmate?", "Yes. The Turro studio and the Via Val di Non flat host up to 2 people, and they are whole apartments you don't share with anyone else."),
  ("How much does student accommodation cost with RAM?", "The Turro studio costs €[[turro]] per month and the Via Val di Non flat €[[vdn]] per month, bills included and with no three-month deposit."),
 ],
},
"es": {
 "nodeposit": [
  ("¿Cuánto cuesta un piso sin fianza con RAM?", "El estudio de Turro cuesta [[turro]] € al mes y el piso de Via Val di Non [[vdn]] € al mes, con luz, gas, calefacción, agua y Wi-Fi incluidos. No hay tres meses de fianza ni gastos de agencia."),
  ("¿Cómo se paga si no hay fianza?", "Las condiciones de pago se acuerdan en el contrato, que se registra en la Agenzia delle Entrate. No inmovilizas tres meses de alquiler por adelantado."),
  ("¿El contrato sin fianza sirve para la residencia?", "Sí. Para estancias de más de 30 días firmamos un <a href=\"[[path:contract]]\">contrato transitorio</a> o de estudiante y lo registramos en la Agenzia delle Entrate: sirve para la residencia y los permisos."),
  ("¿Alquiláis habitaciones sin fianza?", "No, solo pisos enteros: estudios y pisos de un dormitorio con cocina y baño propios, para una o dos personas."),
 ],
 "monthly": [
  ("¿Cuál es la estancia mínima de un alquiler mensual?", "28 noches para el piso de Via Val di Non y 30 noches para el estudio de Turro. El piso confort de Precotto también se alquila para estancias cortas, desde 2 noches."),
  ("¿Qué incluye el precio mensual?", "Luz, gas, calefacción, agua y Wi-Fi de fibra están incluidos. Solo se añade la limpieza final, indicada en la tabla de precios."),
  ("¿Se paga la tasa turística en una estancia mensual?", "No. La tasa turística del Ayuntamiento de Milán se aplica a estancias de menos de 30 noches y no se paga en los contratos mensuales."),
  ("¿Con cuánta antelación conviene buscar piso?", "Empieza 4–8 semanas antes de llegar. Septiembre, enero y febrero son los meses con más demanda por universidades y ferias."),
 ],
 "students": [
  ("¿Cuánto dura el contrato para estudiantes universitarios?", "De 6 a 36 meses, para quien está matriculado en una universidad de un municipio distinto al de residencia. Para un semestre o el Erasmus se usa el <a href=\"[[path:contract]]\">contrato transitorio</a> con motivo de estudio documentado."),
  ("¿Los suministros están incluidos en el alquiler para estudiantes?", "Con RAM, sí: luz, gas, calefacción, agua y Wi-Fi están en el alquiler. En otros pisos el Wi-Fi, la calefacción y los suministros pueden sumar 150–250 € al mes."),
  ("¿Puedo compartir el piso con un compañero de clase?", "Sí. El estudio de Turro y el piso de Via Val di Non alojan hasta 2 personas, y son pisos enteros que no compartes con nadie más."),
  ("¿Cuánto cuesta un alojamiento para estudiantes con RAM?", "El estudio de Turro cuesta [[turro]] € al mes y el piso de Via Val di Non [[vdn]] € al mes, suministros incluidos y sin tres meses de fianza."),
 ],
},
"fr": {
 "nodeposit": [
  ("Combien coûte un appartement sans caution chez RAM ?", "Le studio de Turro coûte [[turro]] € par mois et le deux-pièces de la Via Val di Non [[vdn]] € par mois, électricité, gaz, chauffage, eau et Wi-Fi compris. Pas de caution de trois mois ni de frais d'agence."),
  ("Comment paie-t-on s'il n'y a pas de caution ?", "Les modalités de paiement sont fixées dans le bail, qui est enregistré auprès de l'Agenzia delle Entrate. Vous ne bloquez pas trois mois de loyer à l'avance."),
  ("Le bail sans caution est-il valable pour la résidence ?", "Oui. Pour les séjours de plus de 30 jours, nous signons un <a href=\"[[path:contract]]\">bail transitoire</a> ou étudiant et l'enregistrons auprès de l'Agenzia delle Entrate : il est valable pour la résidence et les titres de séjour."),
  ("Louez-vous des chambres sans caution ?", "Non, uniquement des appartements entiers : studios et deux-pièces avec cuisine et salle de bains privées, pour une ou deux personnes."),
 ],
 "monthly": [
  ("Quelle est la durée minimale d'une location au mois ?", "28 nuits pour le deux-pièces de la Via Val di Non et 30 nuits pour le studio de Turro. L'appartement confort de Precotto se loue aussi pour de courts séjours, à partir de 2 nuits."),
  ("Que comprend le prix mensuel ?", "L'électricité, le gaz, le chauffage, l'eau et le Wi-Fi fibre sont compris. Seul le ménage final s'ajoute, comme indiqué dans le tableau des prix."),
  ("Paie-t-on la taxe de séjour pour un séjour au mois ?", "Non. La taxe de séjour de la Ville de Milan s'applique aux séjours de moins de 30 nuits et n'est pas due pour les baux mensuels."),
  ("Combien de temps à l'avance chercher un logement ?", "Commencez 4 à 8 semaines avant l'arrivée. Septembre, janvier et février sont les mois les plus demandés à cause des universités et des salons."),
 ],
 "students": [
  ("Quelle est la durée d'un bail étudiant en Italie ?", "De 6 à 36 mois, pour les étudiants inscrits dans une université d'une autre commune que celle de leur résidence. Pour un semestre ou Erasmus, on utilise le <a href=\"[[path:contract]]\">bail transitoire</a> avec un motif d'études justifié."),
  ("Les charges sont-elles comprises dans les locations étudiantes ?", "Chez RAM, oui : électricité, gaz, chauffage, eau et Wi-Fi sont dans le loyer. Ailleurs, le Wi-Fi, le chauffage et les charges peuvent ajouter 150 à 250 € par mois."),
  ("Puis-je partager l'appartement avec un camarade de cours ?", "Oui. Le studio de Turro et le deux-pièces de la Via Val di Non accueillent jusqu'à 2 personnes, et ce sont des appartements entiers que vous ne partagez avec personne d'autre."),
  ("Combien coûte un logement étudiant chez RAM ?", "Le studio de Turro coûte [[turro]] € par mois et le deux-pièces de la Via Val di Non [[vdn]] € par mois, charges comprises et sans caution de trois mois."),
 ],
},
"de": {
 "nodeposit": [
  ("Was kostet eine Wohnung ohne Kaution bei RAM?", "Das Studio in Turro kostet [[turro]] € im Monat und die Zweizimmerwohnung in der Via Val di Non [[vdn]] € im Monat, inklusive Strom, Gas, Heizung, Wasser und WLAN. Es gibt keine drei Monatsmieten Kaution und keine Maklergebühr."),
  ("Wie zahle ich, wenn es keine Kaution gibt?", "Die Zahlungsbedingungen werden im Mietvertrag festgelegt, der bei der Agenzia delle Entrate registriert wird. Sie binden keine drei Monatsmieten im Voraus."),
  ("Gilt der Vertrag ohne Kaution für die Wohnsitzanmeldung?", "Ja. Für Aufenthalte über 30 Tage schließen wir einen <a href=\"[[path:contract]]\">Zeitmietvertrag</a> oder Studentenmietvertrag ab und registrieren ihn bei der Agenzia delle Entrate: Er gilt für Wohnsitz und Aufenthaltstitel."),
  ("Vermieten Sie Zimmer ohne Kaution?", "Nein, nur ganze Wohnungen: Studios und Zweizimmerwohnungen mit eigener Küche und eigenem Bad, für eine oder zwei Personen."),
 ],
 "monthly": [
  ("Wie lang ist der Mindestaufenthalt bei einer Monatsmiete?", "28 Nächte für die Wohnung in der Via Val di Non und 30 Nächte für das Studio in Turro. Die Komfortwohnung in Precotto wird auch für kurze Aufenthalte ab 2 Nächten vermietet."),
  ("Was ist im Monatspreis enthalten?", "Strom, Gas, Heizung, Wasser und Glasfaser-WLAN sind enthalten. Hinzu kommt nur die Endreinigung, die in der Preistabelle steht."),
  ("Zahlt man bei einer Monatsmiete Kurtaxe?", "Nein. Die Kurtaxe der Stadt Mailand gilt für Aufenthalte unter 30 Nächten und fällt bei Monatsverträgen nicht an."),
  ("Wie früh sollte man mit der Wohnungssuche beginnen?", "Beginnen Sie 4–8 Wochen vor der Ankunft. September, Januar und Februar sind wegen Universitäten und Messen am gefragtesten."),
 ],
 "students": [
  ("Wie lange läuft ein Studentenmietvertrag in Italien?", "6 bis 36 Monate, für Studierende, die an einer Universität in einer anderen Gemeinde als ihrem Wohnort eingeschrieben sind. Für ein Semester oder Erasmus wird ein <a href=\"[[path:contract]]\">Zeitmietvertrag</a> mit nachgewiesenem Studienzweck verwendet."),
  ("Sind die Nebenkosten bei Studentenwohnungen inklusive?", "Bei RAM ja: Strom, Gas, Heizung, Wasser und WLAN sind in der Miete enthalten. Anderswo können WLAN, Heizung und Nebenkosten 150–250 € im Monat ausmachen."),
  ("Kann ich die Wohnung mit einem Kommilitonen teilen?", "Ja. Das Studio in Turro und die Wohnung in der Via Val di Non bieten Platz für bis zu 2 Personen, und es sind ganze Wohnungen, die Sie mit niemandem sonst teilen."),
  ("Was kostet eine Studentenwohnung bei RAM?", "Das Studio in Turro kostet [[turro]] € im Monat und die Wohnung in der Via Val di Non [[vdn]] € im Monat, Nebenkosten inklusive und ohne drei Monatsmieten Kaution."),
 ],
},
}
