var fullHeight = function() {

		$('#nav-div').css('height', $(window).height());
		$(window).resize(function(){
			$('#nav-div').css('height', $(window).height());
		});

	};
	fullHeight();

var burgerMenu = function() {

		$('.nav-toggle-js').on('click', function(event){
			event.preventDefault();
			var $this = $(this);

			if ($('body').hasClass('panel')) {
				$this.removeClass('active');
				$('body').removeClass('panel');
			} else {
				$this.addClass('active');
				$('body').addClass('panel');
			}
		});
	};
	burgerMenu();

var mobileMenuOutsideClick = function() {

		$(document).click(function (e) {
	    var container = $("#nav-div, .nav-toggle-js");
	    if (!container.is(e.target) && container.has(e.target).length === 0) {

	    	if ( $('body').hasClass('panel') ) {

    			$('body').removeClass('panel');
    			$('.nav-toggle-js').removeClass('active');

	    	}

	    }
		});

		$(window).scroll(function(){
			if ( $('body').hasClass('panel') ) {

    			$('body').removeClass('panel');
    			$('.nav-toggle-js').removeClass('active');

	    	}
		});

	};
	mobileMenuOutsideClick();
