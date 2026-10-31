<?php
// Registro eventi anonimo del sito: niente cookie, niente IP, niente user agent salvati. Una riga CSV per evento, fuori dalla cartella pubblica.
header('Cache-Control: no-store');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(204); exit; }
if (preg_match('/bot|crawl|spider|slurp|headless|lighthouse|preview/i', $_SERVER['HTTP_USER_AGENT'] ?? '')) { http_response_code(204); exit; }
$j = json_decode(substr(file_get_contents('php://input'), 0, 2000), true);
$ok = ['view','read','link','out','cal','cal_nav','dates','guests','quote','booking_request','form_submit','gallery'];
if (!is_array($j) || !in_array($j['e'] ?? '', $ok, true)) { http_response_code(204); exit; }
$clean = function($v, $n) { return substr(preg_replace('/[^A-Za-z0-9\/\-_.:%]/', '', (string)$v), 0, $n); };
$p = $clean($j['p'] ?? '', 160); if ($p === '' || $p[0] !== '/') { http_response_code(204); exit; }
$row = [gmdate('Y-m-d H:i'), $j['e'], $p, $clean($j['l'] ?? '', 160), $clean($j['s'] ?? '', 40), (int)($j['v'] ?? 0)];
$dir = dirname($_SERVER['DOCUMENT_ROOT']) . '/ram-events';
if (!is_dir($dir)) { @mkdir($dir, 0750, true); }
$fh = @fopen($dir . '/' . gmdate('Y-m') . '.csv', 'a');
if ($fh) { flock($fh, LOCK_EX); fputcsv($fh, $row); flock($fh, LOCK_UN); fclose($fh); }
http_response_code(204);
