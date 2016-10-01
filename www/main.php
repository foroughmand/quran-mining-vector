<?php include('include.php'); ?>
  <script type='text/javascript' src='nav.js'></script>
</head>
<body>

<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
	نمایش سوره: <input type="text" value="<?php echo $sura ?>" name="sura" size="4" >
	<input type="submit" value=" نمایش "> &nbsp;
</form>
<a href='main.php'>نمایش آیات</a> <a href='table.php'>نمایش جدولی</a> <a href='tablet.php'>نمایش جدولی ترانهاده</a>

<div class="container">

<div id="wrap">
    <div id="header">
        <!--div id="logo">Start Slowly Scrolling Down<br /> This Page!</div-->
        <div id="navWrap">
            <div id="nav">
		    تعداد قطعات
                <ul>
                </ul>    
                <br class="clearLeft" />
            </div>
        </div>
    </div>
</div>

<article>
<?php
	showSura($sura); 
?>
</article>


</div>

<div class="footer">
	Quran text provided by: <a href="http://tanzil.net/">Tanzil.net<a>
</div>
</body>
