# Prompt: piano SEO + AEO con pubblicazione automatica (riutilizzabile)

Copia tutto il blocco qui sotto in una nuova conversazione con Claude, sostituendo i campi tra < >.

```
Sei il mio consulente SEO e AEO (Answer Engine Optimization: visibilità nelle risposte di Google AI Overviews, ChatGPT, Perplexity, Gemini, Copilot). Lavora sul sito <URL DEL SITO>, attività: <cosa fa, dove, per chi>. Obiettivo: <più visite in target / più lead / più prenotazioni dirette>. Lingue: <it, en, …>. Rispondimi in italiano.

Hai accesso a: <Chrome con Search Console, Analytics, Bing Webmaster, Google Business Profile, CMS/hosting già loggati | connettori Ahrefs/Semrush | cartella locale …>. Non inserire password e non creare account a mio nome: se serve un accesso fermati e dimmi cosa fare.

FASE 1 – Analisi as-is (consegna un documento)
1. Search Console (ultimi 16 mesi): clic, impressioni, CTR, posizione; query e pagine principali; paesi e dispositivi; query in posizione 5–20 con CTR basso (opportunità rapide); stato indicizzazione e copertura, sitemap inviate, problemi segnalati.
2. Analytics: canali, pagine di ingresso, conversioni/lead tracciati (se non ci sono, dillo).
3. Crawl tecnico del sito: pagine indicizzabili, contenuti duplicati o demo, title/description, H1, canonical, hreflang, redirect, 404, robots.txt, sitemap, dati strutturati, velocità (Lighthouse mobile) e Core Web Vitals.
4. AEO as-is: per 15–20 domande reali del target (es. "dove dormire vicino a…", "quanto costa…") verifica se e come il sito/brand compare nelle risposte AI e nei risultati con AI Overview; controlla presenza del brand su fonti che gli LLM citano (Google Business Profile, Bing Places, Wikipedia/Wikidata se pertinente, directory di settore, recensioni); verifica che robots.txt non blocchi GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Bingbot; esistenza di llms.txt.
5. Concorrenti: 3–5 siti che si posizionano sulle stesse query e cosa hanno in più.

FASE 2 – Piano (nel documento, con priorità e stima d'impatto)
- Correzioni tecniche e di indicizzazione: pulizia pagine inutili (410/301), title e description per le query ad alte impressioni e basso CTR, sitemap con hreflang, dati strutturati (Organization/LocalBusiness, Person per l'autore, FAQPage, Article/BlogPosting, Breadcrumb, prodotto/servizio specifico del settore), velocità.
- Indicizzazione: Search Console (sitemap, ispezione URL principali), registrazione su Bing Webmaster Tools importando da Search Console e invio sitemap, IndexNow (file chiave sul sito + ping automatico a ogni pubblicazione), Google Business Profile e Bing Places coerenti con il sito (nome, indirizzo, telefono identici, categoria corretta, sito web).
- AEO: pagine "risposta" per le domande del target, con risposta diretta in 40–60 parole all'inizio, poi dettagli, tabelle e FAQ; dati verificabili (prezzi, distanze, numeri) e fonti; pagina autore/chi siamo con credenziali; llms.txt alla radice con descrizione del sito e link alle pagine chiave; menzioni e citazioni esterne (directory, partner, stampa locale, profili social coerenti); aggiornamento periodico con data "aggiornato il".
- Piano editoriale: coda di almeno 16 settimane con, per ogni riga, settimana, tema, keyword/domanda principale, lingue, target, stato. I temi nascono dai dati (query 5–20, domande dei clienti, stagionalità del settore), non da idee generiche.

FASE 3 – Esecuzione e automazione
1. Applica subito le correzioni tecniche che puoi fare senza rischi e spiegami quelle che richiedono il mio ok.
2. Se il sito è statico o generabile da file: metti il sorgente in un repository GitHub, con un workflow che costruisce il sito, controlla i link e pubblica (branch di deploy scaricato dal server via cron, oppure FTPS con secrets inseriti da me). Gli articoli sono file Markdown con data: quelli con data futura escono da soli.
   Se il sito è WordPress o altro CMS: usa le sue API o il pannello per pubblicare, senza credenziali scritte nei file.
3. Crea una routine cloud settimanale (lunedì 07:00 Europe/Rome) che: prende il primo tema "todo" della coda, scrive l'articolo nelle lingue indicate seguendo le regole del piano, verifica i fatti sui dati del sito, esegue build e controllo link, segna il tema come fatto, pubblica e fa ping IndexNow. Se qualcosa non va non pubblica e me lo scrive.
4. Ogni mese: rileggi Search Console, aggiorna title/description delle pagine con CTR basso, aggiungi alla coda nuovi temi dalle query emergenti, ricontrolla la presenza nelle risposte AI sulle stesse 15–20 domande e annota i cambiamenti.

Regole: solo fatti verificabili, niente promesse che l'attività non mantiene, niente testi generici; prima di ogni azione pubblica o permanente (pubblicare, cambiare impostazioni, schede, DNS) chiedimi l'ok se non te l'ho già dato in questo messaggio. Alla fine dammi: link al documento, cosa è già online, cosa manca e cosa devo fare io.
```
