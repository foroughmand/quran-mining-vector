$(function() {
	var navul = $('#nav ul');
	for (var i=1; i<MST[sure].length; i++) {
		var li = $('<li><a href="#" class="smoothScroll">' + i + '</a></li>');
		li.click({k: i}, loadDivision);
                navul.append(li);
	}
    // Stick the #nav to the top of the window
    var nav = $('#nav');
    var navHomeY = nav.offset().top;
    var isFixed = false;
    var $w = $(window);
    $w.scroll(function() {
        var scrollTop = $w.scrollTop();
        var shouldBeFixed = scrollTop > navHomeY;
        if (shouldBeFixed && !isFixed) {
            nav.css({
                position: 'fixed',
                top: 0,
                left: nav.offset().left,
                width: nav.width()
            });
            isFixed = true;
        }
        else if (!shouldBeFixed && isFixed)
        {
            nav.css({
                position: 'static'
            });
            isFixed = false;
        }
    });
});
function loadDivision(event) {
	var k = event.data.k;
	var sl = MST[sure][k];
	console.log('lD', k, sl);
	for (var i=0; i<sl.length-1; i++)
		for (var j=sl[i]; j<sl[i+1]; j++) {
			$('#aye-'+(j+1)).removeAttr('class').addClass('aya div-'+(i+1));
		}
}

