var fullHeight = function() {

		$('#nav-div').css('height', $(window).height());
		$(window).resize(function(){
			$('#nav-div').css('height', $(window).height());
		});

	};
	fullHeight();


var bodyPanel = function () {
	$('.nav-toggle').click(function(){
		$(this).toggleClass('open');
		if ($('body').hasClass('panel')) {

 				$('body').removeClass('panel');
 			} else {

 				$('body').addClass('panel');
 			}
	});
}
bodyPanel();

var imageZoom = function () {
	$(".zoom").hover(function(){

		$(this).addClass('transition');
		},
		function(){

		$(this).removeClass('transition');
	});
}

imageZoom();
var fancy = function () {
$('[data-fancybox="images"]').fancybox({
  buttons : [
    'slideShow',
    'share',
    'zoom',
    'fullScreen',
    'close'
  ],
  thumbs : {
    autoStart : true
  }
});
}
fancy();