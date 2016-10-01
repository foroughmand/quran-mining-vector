<?php

	// Quran Metadata Sample Usage
	// By: Hamid Zarrabi-Zadeh
	// http://tanzil.net


	error_reporting(E_ALL & ~E_NOTICE & ~E_WARNING); 

	$sura = $_REQUEST['sura'];
	if (!isset($sura))
		$sura = 36;
	
	$quranFile = '../data/quran-simple.txt';   // quran file
	$metadataFile = '../data/quran-data.xml';  // quran metadata file

	initSuraData();   // initialize sura data array
	

	//------------------ General Functions ---------------------


	// initialize sura data array
	function initSuraData()
	{
		global $suraData, $metadataFile;
		$dataItems = Array("index", "start", "ayas", "name", "tname", "ename", "type", "rukus");

		$quranData = file_get_contents($metadataFile);
		$parser = xml_parser_create();
		xml_parse_into_struct($parser, $quranData, $values, $index);
		xml_parser_free($parser);

		for ($i=1; $i<=114; $i++) 
		{
			$j = $index['SURA'][$i-1];
			foreach ($dataItems as $item)
				$suraData[$i][$item] = $values[$j]['attributes'][strtoupper($item)]; 
		}
	}


	// return given property of a sura
	function getSuraData($sura, $property) 
	{
		global $suraData;
		return $suraData[$sura][$property]; 
	}


	// return contents of a sura 
	function getSuraContents($sura) 
	{
		global $quranFile;
		$startAya = getSuraData($sura, 'start');
		$endAya = $startAya+ getSuraData($sura, 'ayas');
		$quran = file($quranFile);
		$text = array_slice($quran, $startAya, $endAya- $startAya); 
		return $text;
	}


	//------------------ Display Functions ---------------------


	if ($sura < 1) $sura = 1; 
	if ($sura > 114) $sura = 114; 


	// show sura contents
	function showSura($sura)
	{
		$suraName = getSuraData($sura, 'name');
		$suraText = getSuraContents($sura);
		$showBismillah = true; // change to true to show Bismillahs
		$ayaNum = 1;
		
		echo "<div class=suraName>سورة $suraName</div>";
		foreach ($suraText as $aya)
		{
			// remove bismillahs, except for suras 1 and 9
			if (!$showBismillah && $ayaNum == 1 && $sura !=1 && $sura !=9)
				$aya = preg_replace('/^(([^ ]+ ){4})/u', '', $aya);
			// display waqf marks in different style
			$aya = preg_replace('/ ([ۖ-۩])/u', '<span class="sign">&nbsp;$1</span>', $aya);
			
			echo "<div class=aya id='aye-$ayaNum'><span class=ayaNum>$ayaNum. </span>$aya</div>";
			$ayaNum++;
		}
	}
	

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title> نمایش سوره <?php echo $sura ?> </title>

  <link rel="stylesheet" type="text/css" href="main.css">
  <script type='text/javascript' src='https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js'></script>
<script>
var sure = <?php echo $sura; ?>;
<?php
	$MST = array();
	$f = fopen("../data/aye-mst-2.dat", "r") or die('Invalid file');
	while (($l = fgets($f, 200000)) !== false) {
		$x = explode(" ", $l);
		$MST[$x[0]][$x[1]] = array_slice($x, 3);
		$MST_VALUE[$x[0]][$x[1]] = $x[2];
	}
	echo "var MST={";
	foreach ($MST as $s => $sMST) {
		echo "$s: [";
		foreach ($sMST as $a => $slices) {
			echo "[";
			foreach ($slices as $s)
				echo "$s,"; 
			echo "],";
		}
		echo "],";
	}
	echo "};";
	echo "var MSTvalue={";
	foreach ($MST_VALUE as $s => $sMST_VALUE) {
		echo "$s: [";
		foreach ($sMST_VALUE as $a => $v) {
			echo "$v, ";
		}
		echo "],";
	}
	echo "};";
	fclose($f);
?>
</script>

