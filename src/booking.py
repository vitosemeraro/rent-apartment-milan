# Modulo di prenotazione diretta per ogni appartamento: calendario con disponibilità iCal, ospiti, preventivo
import json, html

S = {
"en": {"title": "Book directly", "pick": "Select check-in and check-out", "in": "Check-in", "out": "Check-out", "adults": "Adults", "kids": "Children (under 18)",
       "nights": "nights", "night": "night", "extra": "Extra guests", "clean": "Cleaning", "disc": "Discount", "tax": "Milan tourist tax",
       "total": "Estimated total", "min": "Minimum stay: {n} nights", "busy": "Some nights in this range are not available", "name": "Name", "email": "Email",
       "msg": "Message (optional)", "send": "Request booking", "note": "No payment now: I'll confirm availability and send you the payment details by email.",
       "privacy": "I agree to the <a href=\"{p}\">privacy policy</a>.", "loading": "Loading availability…", "free": "available", "taken": "booked",
       "months": ["January","February","March","April","May","June","July","August","September","October","November","December"], "days": ["Mo","Tu","We","Th","Fr","Sa","Su"],
       "monthly_hint": "Monthly discount applied from 28 nights.", "prev": "Previous month", "next": "Next month"},
"it": {"title": "Prenota direttamente", "pick": "Scegli arrivo e partenza", "in": "Arrivo", "out": "Partenza", "adults": "Adulti", "kids": "Bambini (under 18)",
       "nights": "notti", "night": "notte", "extra": "Ospiti extra", "clean": "Pulizie", "disc": "Sconto", "tax": "Tassa di soggiorno Milano",
       "total": "Totale stimato", "min": "Soggiorno minimo: {n} notti", "busy": "Alcune notti in questo periodo non sono disponibili", "name": "Nome", "email": "Email",
       "msg": "Messaggio (facoltativo)", "send": "Richiedi la prenotazione", "note": "Nessun pagamento ora: ti confermo la disponibilità e ti mando via email i dati per il pagamento.",
       "privacy": "Accetto l'<a href=\"{p}\">informativa privacy</a>.", "loading": "Carico la disponibilità…", "free": "libero", "taken": "occupato",
       "months": ["Gennaio","Febbraio","Marzo","Aprile","Maggio","Giugno","Luglio","Agosto","Settembre","Ottobre","Novembre","Dicembre"], "days": ["Lu","Ma","Me","Gi","Ve","Sa","Do"],
       "monthly_hint": "Sconto mensile applicato da 28 notti.", "prev": "Mese precedente", "next": "Mese successivo"},
"es": {"title": "Reserva directa", "pick": "Elige llegada y salida", "in": "Llegada", "out": "Salida", "adults": "Adultos", "kids": "Niños (menores de 18)",
       "nights": "noches", "night": "noche", "extra": "Huéspedes extra", "clean": "Limpieza", "disc": "Descuento", "tax": "Tasa turística de Milán",
       "total": "Total estimado", "min": "Estancia mínima: {n} noches", "busy": "Algunas noches de este periodo no están disponibles", "name": "Nombre", "email": "Email",
       "msg": "Mensaje (opcional)", "send": "Solicitar reserva", "note": "Sin pago ahora: confirmo la disponibilidad y te envío por email los datos de pago.",
       "privacy": "Acepto la <a href=\"{p}\">política de privacidad</a>.", "loading": "Cargando disponibilidad…", "free": "libre", "taken": "ocupado",
       "months": ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"], "days": ["Lu","Ma","Mi","Ju","Vi","Sá","Do"],
       "monthly_hint": "Descuento mensual desde 28 noches.", "prev": "Mes anterior", "next": "Mes siguiente"},
"fr": {"title": "Réserver en direct", "pick": "Choisissez arrivée et départ", "in": "Arrivée", "out": "Départ", "adults": "Adultes", "kids": "Enfants (moins de 18 ans)",
       "nights": "nuits", "night": "nuit", "extra": "Voyageurs supplémentaires", "clean": "Ménage", "disc": "Réduction", "tax": "Taxe de séjour Milan",
       "total": "Total estimé", "min": "Séjour minimum : {n} nuits", "busy": "Certaines nuits de cette période ne sont pas disponibles", "name": "Nom", "email": "E-mail",
       "msg": "Message (facultatif)", "send": "Demander la réservation", "note": "Aucun paiement maintenant : je confirme la disponibilité et vous envoie les modalités de paiement par e-mail.",
       "privacy": "J'accepte la <a href=\"{p}\">politique de confidentialité</a>.", "loading": "Chargement des disponibilités…", "free": "libre", "taken": "réservé",
       "months": ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Décembre"], "days": ["Lu","Ma","Me","Je","Ve","Sa","Di"],
       "monthly_hint": "Réduction mensuelle dès 28 nuits.", "prev": "Mois précédent", "next": "Mois suivant"},
"de": {"title": "Direkt buchen", "pick": "An- und Abreise wählen", "in": "Anreise", "out": "Abreise", "adults": "Erwachsene", "kids": "Kinder (unter 18)",
       "nights": "Nächte", "night": "Nacht", "extra": "Zusätzliche Gäste", "clean": "Reinigung", "disc": "Rabatt", "tax": "Kurtaxe Mailand",
       "total": "Geschätzter Gesamtpreis", "min": "Mindestaufenthalt: {n} Nächte", "busy": "Einige Nächte in diesem Zeitraum sind nicht verfügbar", "name": "Name", "email": "E-Mail",
       "msg": "Nachricht (optional)", "send": "Buchung anfragen", "note": "Jetzt keine Zahlung: Ich bestätige die Verfügbarkeit und sende Ihnen die Zahlungsdaten per E-Mail.",
       "privacy": "Ich akzeptiere die <a href=\"{p}\">Datenschutzerklärung</a>.", "loading": "Verfügbarkeit wird geladen…", "free": "frei", "taken": "belegt",
       "months": ["Januar","Februar","März","April","Mai","Juni","Juli","August","September","Oktober","November","Dezember"], "days": ["Mo","Di","Mi","Do","Fr","Sa","So"],
       "monthly_hint": "Monatsrabatt ab 28 Nächten.", "prev": "Voriger Monat", "next": "Nächster Monat"},
}

CSS = """.bk{display:grid;gap:12px;margin-top:6px}.bk h3{margin:0;font-size:1.15rem}.bk .cal{max-width:420px}
.cal-h{display:flex;align-items:center;justify-content:space-between;font-weight:700}
.cal-h button{background:#fff;border:1px solid var(--line);width:34px;height:34px;cursor:pointer;font-size:18px}
.cal-g{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;text-align:center;font-size:13px}
.cal-g b{font-weight:600;color:var(--mut);padding:4px 0}
.cal-g button{height:38px;border:0;background:#fff;cursor:pointer;font:inherit;color:var(--ink)}
.cal-g button:hover:not(:disabled){outline:2px solid var(--ink)}
.cal-g button:disabled{color:#b9b8b0;background:repeating-linear-gradient(135deg,#f4f3ee,#f4f3ee 4px,#ecebe4 4px,#ecebe4 8px);cursor:not-allowed;text-decoration:line-through}
.cal-g button.on{background:var(--acc);color:#fff}.cal-g button.in{background:#f6d3d8}
.bk .row2{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.bk label{display:grid;gap:4px;font-size:13px;font-weight:600}
.bk input,.bk select,.bk textarea{font:inherit;padding:10px;border:1px solid var(--line);background:#fff;color:var(--ink);width:100%}
.bk .sel{font-size:14px;background:var(--soft);padding:8px 10px}
.bk table{width:100%;font-size:14px;border-collapse:collapse}.bk td{padding:4px 0}.bk td:last-child{text-align:right}
.bk tr.tot td{border-top:1px solid var(--ink);font-weight:700;font-size:16px;padding-top:8px}
.bk .err{color:var(--acc);font-size:13px;min-height:1em}.bk .fine{font-size:12px;color:var(--mut)}
.bk .btn{width:100%;justify-content:center}.bk .btn:disabled{opacity:.45;cursor:not-allowed}"""

JS = r"""(function(){var f=document.querySelector('form.bk');if(!f)return;var C=JSON.parse(f.getAttribute('data-cfg')),T=C.t,P=C.p,TX=C.tax;
var busy={},today=new Date();today.setHours(0,0,0,0);var view=new Date(today.getFullYear(),today.getMonth(),1),a=null,b=null;
function k(d){return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
function add(d,n){var x=new Date(d);x.setDate(x.getDate()+n);return x}
function nightsFree(s,e){for(var d=new Date(s);d<e;d=add(d,1))if(busy[k(d)])return false;return true}
var box=f.querySelector('.cal'),sel=f.querySelector('.sel'),q=f.querySelector('.quote'),er=f.querySelector('.err'),btn=f.querySelector('button[type=submit]');
function month(m){var h='<div class="cal-g">'+T.days.map(function(x){return '<b>'+x+'</b>'}).join('');var first=new Date(m.getFullYear(),m.getMonth(),1),off=(first.getDay()+6)%7;
for(var i=0;i<off;i++)h+='<span></span>';for(var d=new Date(first);d.getMonth()==m.getMonth();d=add(d,1)){var key=k(d),dis=d<today,cls='';
if(!dis){if(a&&!b&&d>a){dis=!nightsFree(a,d)}else{dis=!!busy[key]}}
if(a&&k(a)==key||b&&k(b)==key)cls='on';else if(a&&b&&d>a&&d<b)cls='in';
h+='<button type="button" data-d="'+key+'" class="'+cls+'"'+(dis?' disabled':'')+' aria-label="'+key+(busy[key]?' '+T.taken:'')+'">'+d.getDate()+'</button>'}return h+'</div>'}
function draw(){var m2=new Date(view.getFullYear(),view.getMonth()+1,1);box.innerHTML='<div class="cal-h"><button type="button" data-n="-1" aria-label="'+T.prev+'">‹</button><span>'+T.months[view.getMonth()]+' '+view.getFullYear()+'</span><button type="button" data-n="1" aria-label="'+T.next+'">›</button></div>'+month(view)+(window.innerWidth>1100?'':'');calc()}
box.addEventListener('click',function(e){var n=e.target.getAttribute('data-n');if(n){view=new Date(view.getFullYear(),view.getMonth()+(+n),1);if(view<new Date(today.getFullYear(),today.getMonth(),1))view=new Date(today.getFullYear(),today.getMonth(),1);draw();return}
var d=e.target.getAttribute('data-d');if(!d||e.target.disabled)return;var x=new Date(d+'T00:00:00');if(!a||b||x<=a){a=x;b=null}else{b=x}draw()});
function price(d){var s=k(d);for(var i=0;i<P.events.length;i++){var ev=P.events[i];if(s>=ev[0]&&s<ev[1])return ev[2]}var w=d.getDay();return (w==5||w==6)?P.weekend:P.base}
function eur(v){return '€ '+Math.round(v).toLocaleString('it-IT')}
function calc(){er.textContent='';sel.textContent=a?(T.in+': '+a.toLocaleDateString()+(b?' · '+T.out+': '+b.toLocaleDateString():'')):T.pick;
var ad=+f.adults.value,ch=+f.children.value,g=ad+ch;if(g>P.max_guests){f.children.value=Math.max(0,P.max_guests-ad);ch=+f.children.value;g=ad+ch}
if(!a||!b){q.innerHTML='';btn.disabled=true;return}var n=Math.round((b-a)/864e5);if(n<P.min_nights){er.textContent=T.min.replace('{n}',P.min_nights);q.innerHTML='';btn.disabled=true;return}
var nightsSum=0,extra=0,taxv=0;for(var i=0,d=new Date(a);i<n;i++,d=add(d,1)){nightsSum+=price(d);extra+=Math.max(0,g-P.extra_after)*P.extra_fee;if(i<TX.max&&n<30)taxv+=(TX.r[d.getFullYear()]||TX.r.def)*ad}
var disc=0;if(n>=28)disc=P.monthly;else if(n>=7)disc=P.weekly;else if(P.length[n])disc=P.length[n];var lead=Math.round((a-today)/864e5);if(P.lastminute&&lead<=P.lastminute_days)disc=Math.max(disc,P.lastminute);
var base=nightsSum+extra,dv=base*disc/100,tot=base-dv+P.cleaning+taxv;
var rows=[[n+' '+(n==1?T.night:T.nights),eur(nightsSum)]];if(extra)rows.push([T.extra,eur(extra)]);if(dv)rows.push([T.disc+' '+disc+'%','− '+eur(dv)]);rows.push([T.clean,eur(P.cleaning)]);if(n<30)rows.push([T.tax+' ('+ad+' × '+Math.min(n,TX.max)+')',eur(taxv)]);
q.innerHTML='<table>'+rows.map(function(r){return '<tr><td>'+r[0]+'</td><td>'+r[1]+'</td></tr>'}).join('')+'<tr class="tot"><td>'+T.total+'</td><td>'+eur(tot)+'</td></tr></table>';
f.checkin.value=k(a);f.checkout.value=k(b);f.quote.value=rows.map(function(r){return r[0]+': '+r[1]}).join(' | ')+' | TOTALE: '+eur(tot);btn.disabled=false}
f.adults.addEventListener('change',calc);f.children.addEventListener('change',calc);
fetch((location.hostname=='localhost'?'/test-avail.json?':'/availability.php?apt=')+C.apt).then(function(r){return r.json()}).then(function(j){(j.busy||[]).forEach(function(r){for(var d=new Date(r[0]+'T00:00:00'),e=new Date(r[1]+'T00:00:00');d<e;d=add(d,1))busy[k(d)]=1});draw()}).catch(draw);
box.innerHTML='<p class="fine">'+T.loading+'</p>'})();"""


def render(lang, lid, pricing, privacy_path, esc=html.escape):
    t = S[lang]; p = pricing[lid]
    cfg = {"apt": lid, "t": {k: t[k] for k in ("pick", "in", "out", "nights", "night", "extra", "clean", "disc", "tax", "total", "min", "taken", "months", "days", "prev", "next", "loading")},
           "p": p, "tax": {"r": {**{y: v for y, v in pricing["tourist_tax"].items() if y.isdigit()}, "def": pricing["tourist_tax"]["2027"]}, "max": pricing["tourist_tax"]["max_nights"]}}
    mg = p["max_guests"]
    ad = "".join(f'<option{" selected" if i == min(2, mg) else ""}>{i}</option>' for i in range(1, mg + 1))
    ch = "".join(f"<option>{i}</option>" for i in range(0, mg))
    return f"""<form class="bk" method="post" action="/contact.php" data-cfg='{esc(json.dumps(cfg, ensure_ascii=False), quote=True)}'>
<h3>{esc(t["title"])}</h3><input type="hidden" name="lang" value="{lang}"><input type="hidden" name="apt" value="{lid}"><input type="hidden" name="kind" value="booking">
<input type="hidden" name="checkin"><input type="hidden" name="checkout"><input type="hidden" name="quote"><label class="hp">Website<input name="website" tabindex="-1" autocomplete="off"></label>
<div class="cal" aria-live="polite"></div><div class="sel">{esc(t["pick"])}</div>
<noscript><div class="row2"><label>{t["in"]}<input type="date" name="checkin_ns"></label><label>{t["out"]}<input type="date" name="checkout_ns"></label></div></noscript>
<div class="row2"><label>{t["adults"]}<select name="adults">{ad}</select></label><label>{t["kids"]}<select name="children">{ch}</select></label></div>
<div class="quote"></div><div class="err" role="alert"></div>
<label>{t["name"]}<input name="name" required autocomplete="name"></label><label>{t["email"]}<input type="email" name="email" required autocomplete="email"></label>
<label>{t["msg"]}<textarea name="message" rows="2"></textarea></label>
<label style="display:flex;gap:8px;font-weight:400"><input type="checkbox" required style="width:auto"> <span>{t["privacy"].replace("{p}", privacy_path)}</span></label>
<button class="btn" type="submit" disabled data-evt="booking_request" data-label="{lid}">{esc(t["send"])}</button><p class="fine">{esc(t["note"])}</p></form>"""
