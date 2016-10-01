<?php include('include.php'); ?>
<script>
$(function() {
	$('td').css('width', '4px');
});
</script>
</head>
<body>

<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
	نمایش سوره: <input type="text" value="<?php echo $sura ?>" name="sura" size="4" >
	<input type="submit" value=" نمایش "> &nbsp;
</form>
<a href='main.php'>نمایش آیات</a> <a href='table.php'>نمایش جدولی</a> <a href='tablet.php'>نمایش جدولی ترانهاده</a>

<table>
<?php
		$suraName = getSuraData($sura, 'name');
		$suraText = getSuraContents($sura);
		$ayaNum = 1;
		
		foreach ($suraText as $aya)
		{
			if ($ayaNum == 1 && $sura !=1 && $sura !=9)
				$aya = preg_replace('/^(([^ ]+ ){4})/u', '', $aya);
			$aya = preg_replace('/ ([ۖ-۩])/u', '<span class="sign">&nbsp;$1</span>', $aya);
			
			//echo "<div class=aya id='aye-$ayaNum'><span class=ayaNum>$ayaNum. </span>$aya</div>";
			echo "<tr><td>$ayaNum";
			foreach ($MST[$sura] as $k => $slices) {
				echo "<td class='div-";
				for ($i=0; $i<count($slices)-1; $i++) {
					if ($slices[$i] <=$ayaNum-1 && $ayaNum-1 < $slices[$i+1]) {
						echo "$i";
					}
				}
				echo "'>";
				//for ($i=0; $i<count($slices)-1; $i++) {
				//	echo "".$slices[$i]. " ";
				//}
			}
			$ayaNum++;
		}
?>
</table>

</body>
