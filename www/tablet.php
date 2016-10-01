<?php include('include.php'); ?>
<script>
$(function() {
	$('td').css('height', '4px');
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
		echo "<tr>";
			$ayaNum = 1;
			
			foreach ($suraText as $aya)
			{
				echo "<td";
				echo ">$ayaNum";
				$ayaNum++;
			}

		foreach ($MST[$sura] as $k => $slices) {
			echo "<tr>";
			$ayaNum = 1;
			
			foreach ($suraText as $aya)
			{
				echo "<td class='div-";
				for ($i=0; $i<count($slices)-1; $i++) {
					if ($slices[$i] <=$ayaNum-1 && $ayaNum-1 < $slices[$i+1]) {
						echo "$i";
					}
				}
				echo "'>";
				$ayaNum++;
			}
		}

?>
</table>

</body>
