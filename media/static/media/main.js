var fullHeight = function() {

		$('#nav-div').css('height', $(window).height());
		$(window).resize(function(){
			$('#nav-div').css('height', $(window).height());
		});

	};
	fullHeight();


// var burgerMenu = function() {
//
// 		$('#nav-icon').on('click', function(event){
// 			event.preventDefault();
// 			var $this = $(this);
//
// 			if ($('nav').hasClass('panel')) {
// 				$this.removeClass('active');
// 				$this.toggleClass('open');
// 				$('nav').removeClass('panel');
// 			} else {
// 				$this.addClass('active');
// 				// $this.toggleClass('open');
// 				$('nav').addClass('panel');
// 			}
// 		});
// 	};
// 	burgerMenu();

// var mobileMenuOutsideClick = function() {
//
// 		$(document).click(function (e) {
// 	    var container = $("#nav-div, .nav-toggle-js");
// 	    if (!container.is(e.target) && container.has(e.target).length === 0) {
//
// 	    	if ( $('body').hasClass('panel') ) {
//
//     			$('body').removeClass('panel');
//     			$('.nav-toggle-js').removeClass('active');
//
// 	    	}
//
// 	    }
// 		});

		// $(window).scroll(function(){
		// 	if ( $('body').hasClass('panel') ) {
		//
    	// 		$('body').removeClass('panel');
    	// 		$('.nav-toggle-js').removeClass('active');
		//
	    // 	}
		// });

	// };
	// mobileMenuOutsideClick();
