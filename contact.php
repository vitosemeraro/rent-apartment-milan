<?php
// Modulo contatti e richieste di prenotazione RAM: invia a hello@ (inoltrata a Gmail) e reindirizza alla pagina di ringraziamento
$to = 'hello@rent-apartment-milan.com';
$thanks = ['en'=>'/thank-you/','it'=>'/it/grazie/','es'=>'/es/gracias/','fr'=>'/fr/merci/','de'=>'/de/danke/'];
$names = ['mm'=>'Casa comfort Precotto (MM)','pa'=>'Design Precotto (PA)','turro'=>'Monolocale Turro','vdn'=>'Bilocale Val di Non'];
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: /', true, 303); exit; }
if (!empty($_POST['website'])) { header('Location: /', true, 303); exit; } // honeypot anti-spam
$f = function($k, $n = 2000) { return trim(mb_substr(strip_tags($_POST[$k] ?? ''), 0, $n)); };
$lang = array_key_exists($f('lang', 2), $thanks) ? $f('lang', 2) : 'en';
$email = filter_var($f('email', 200), FILTER_VALIDATE_EMAIL);
$booking = $f('kind', 10) === 'booking';
$name = str_replace(["\r", "\n"], ' ', $f('name', 120));
if (!$email || $name === '' || (!$booking && $f('message') === '')) { header('Location: ' . ($lang === 'en' ? '/contact/' : "/$lang/"), true, 303); exit; }
$apt = $f('apt', 20); $aptName = $names[$apt] ?? ($apt ?: '-');
$in = $f('checkin', 12) ?: $f('checkin_ns', 12); $out = $f('checkout', 12) ?: $f('checkout_ns', 12);
$guests = $booking ? ($f('adults', 2) . ' adulti + ' . $f('children', 2) . ' bambini') : $f('guests', 3);
$body = ($booking ? "RICHIESTA DI PRENOTAZIONE" : "Nuova richiesta") . " dal sito rent-apartment-milan.com\n\n"
  . "Nome: $name\nEmail: $email\nLingua: $lang\nAppartamento: $aptName\nArrivo: $in\nPartenza: $out\nOspiti: $guests"
  . ($booking ? "\n\nPreventivo mostrato all'ospite:\n" . str_replace(' | ', "\n", $f('quote', 1500)) : "\nMotivo: " . $f('reason', 80))
  . "\n\nMessaggio:\n" . ($f('message') ?: '-') . "\n\nRispondi direttamente a questa email per scrivere all'ospite.\nIP: " . ($_SERVER['REMOTE_ADDR'] ?? '');
// Filtro anti-spam: niente JavaScript, link commerciali o frasi tipiche dei venditori -> oggetto diverso, così il filtro Gmail non lo mette tra le richieste importanti
$msg = strtolower($f('message'));
$spam = $f('js', 1) !== '1' || preg_match('/unsubscribe|opt out|opt-out|seo services|lead gen|free trial|backlink|our agency|web design|marketing services/', $msg) || preg_match_all('#https?://#', $msg) >= 2 || (!$booking && ($in === '' || $out === ''));
$subject = ($spam ? '[RAM possibile spam] ' : '[RAM richiesta] ') . ($booking ? "Prenotazione $aptName " : '') . "$name $in" . ($out ? " - $out" : '');
$headers = "From: RAM sito <$to>\r\nReply-To: $name <$email>\r\nContent-Type: text/plain; charset=UTF-8";
@mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $headers, "-f$to");
header('Location: ' . $thanks[$lang], true, 303);
