<?php
// Totali aggregati del registro eventi (solo conteggi per giorno, evento, pagina, etichetta e provenienza): li legge il punteggio settimanale
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Robots-Tag: noindex');
$days = max(1, min(120, (int)($_GET['days'] ?? 35)));
$since = gmdate('Y-m-d', time() - $days * 86400);
$dir = dirname($_SERVER['DOCUMENT_ROOT']) . '/ram-events';
$agg = [];
foreach (glob($dir . '/*.csv') ?: [] as $f) {
  if (basename($f, '.csv') < substr($since, 0, 7)) continue;
  $fh = fopen($f, 'r');
  while (($r = fgetcsv($fh)) !== false) {
    if (count($r) < 6 || substr($r[0], 0, 10) < $since) continue;
    $k = substr($r[0], 0, 10) . "\t" . $r[1] . "\t" . $r[2] . "\t" . $r[3] . "\t" . $r[4];
    if (!isset($agg[$k])) $agg[$k] = [0, 0];
    $agg[$k][0]++; $agg[$k][1] += (int)$r[5];
  }
  fclose($fh);
}
$rows = [];
foreach ($agg as $k => $v) { [$d, $e, $p, $l, $s] = explode("\t", $k); $rows[] = ['day'=>$d,'e'=>$e,'p'=>$p,'l'=>$l,'s'=>$s,'n'=>$v[0],'v'=>$v[1]]; }
echo json_encode(['since'=>$since,'rows'=>$rows]);
