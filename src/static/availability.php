<?php
// Disponibilità dagli iCal Airbnb: restituisce solo gli intervalli occupati (niente dati degli ospiti). Cache 20 minuti.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=600');
// Gli URL iCal (con token privati) stanno fuori dal sito e fuori dal repository: /home/<utente>/ram-config/ics.json
$ics = json_decode(@file_get_contents(dirname($_SERVER['DOCUMENT_ROOT']) . '/ram-config/ics.json'), true) ?: [];
$id = $_GET['apt'] ?? '';
if (!isset($ics[$id])) { http_response_code(404); echo '{"busy":[]}'; exit; }
$cache = sys_get_temp_dir() . "/ram_ics_$id.json";
if (is_file($cache) && time() - filemtime($cache) < 1200) { readfile($cache); exit; }
$ctx = stream_context_create(['http' => ['timeout' => 8, 'header' => "User-Agent: RAM-site\r\n"]]);
$raw = @file_get_contents($ics[$id], false, $ctx);
if ($raw === false && function_exists('curl_init')) {
  $c = curl_init($ics[$id]); curl_setopt_array($c, [CURLOPT_RETURNTRANSFER => 1, CURLOPT_TIMEOUT => 8, CURLOPT_FOLLOWLOCATION => 1]);
  $raw = curl_exec($c); curl_close($c);
}
if (!$raw) { if (is_file($cache)) { readfile($cache); } else { echo '{"busy":[]}'; } exit; }
preg_match_all('/DTSTART;VALUE=DATE:(\d{8}).*?DTEND;VALUE=DATE:(\d{8})/s', $raw, $m, PREG_SET_ORDER);
$busy = [];
foreach ($m as $e) {
  $busy[] = [substr($e[1],0,4).'-'.substr($e[1],4,2).'-'.substr($e[1],6,2), substr($e[2],0,4).'-'.substr($e[2],4,2).'-'.substr($e[2],6,2)];
}
$out = json_encode(['busy' => $busy, 'updated' => date('c')]);
@file_put_contents($cache, $out);
echo $out;
