/**
 * Functions to add dropdown caret at the end of navigation menu item with children
 * and code to remove white between navigation menu and header image.
 */
var screenReaderText = {"expand":"expand child menu","collapse":"collapse child menu"};


(function($){
    /**
      * Add Carate-down at the end of menu item, if the menu item has children
      */
    function initMainNavigation( container ) {
        // Add dropdown toggle that displays child menu items.
        var dropdownToggle = $( '<button />', {
            'class': 'dropdown-toggle',
            'aria-expanded': false
        } ).append( $( '<span />', {
            'class': 'screen-reader-text',
            text: screenReaderText.expand
        } ) );

        container.find( '.menu-item-has-children > a' ).after( dropdownToggle );

        // Toggle buttons and submenu items with active children menu items.
        container.find( '.current-menu-ancestor > button' ).addClass( 'toggled-on' );
        container.find( '.current-menu-ancestor > .sub-menu' ).addClass( 'toggled-on' );

        // Add menu items with submenus to aria-haspopup="true".
        container.find( '.menu-item-has-children' ).attr( 'aria-haspopup', 'true' );

        container.find( '.dropdown-toggle' ).click( function( e ) {
            var _this            = $( this ),
                screenReaderSpan = _this.find( '.screen-reader-text' );

            e.preventDefault();
            _this.toggleClass( 'toggled-on' );
            _this.next( '.children, .sub-menu' ).toggleClass( 'toggled-on' );

            // jscs:disable
            _this.attr( 'aria-expanded', _this.attr( 'aria-expanded' ) === 'false' ? 'true' : 'false' );
            // jscs:enable
            screenReaderSpan.text( screenReaderSpan.text() === screenReaderText.expand ? screenReaderText.collapse : screenReaderText.expand );
        } );
    }
    initMainNavigation( $( '.main-navigation' ) );

    /**
      * Remove white space between menu and header image.
      */
    var setHeight = function (h) {	
    	height = h;
    	$("#cc_spacer").css("height", height + "px");
	}

	$(window).resize(function(){
		setHeight($("#navigation_menu").height());
	});

	$(window).ready(function(){
		setHeight($("#navigation_menu").height());
	});
})(jQuery);


NProgress.start();
NProgress.set(0.4);
//Increment
var interval = setInterval(function () {
    NProgress.inc();
}, 1000);
$(document).ready(function () {
    NProgress.done();
    clearInterval(interval);
});


/** 侧边栏回到顶部 */
var rocket = $('#rocket');

$(window).on('scroll', debounce(slideTopSet, 300));

function debounce(func, wait) {
    var timeout;
    return function() {
        clearTimeout(timeout);
        timeout = setTimeout(func, wait);
    };
};
function slideTopSet() {
    var top = $(document).scrollTop();

    if (top > 200) {
        rocket.addClass('show');
    } else {
        rocket.removeClass('show');
    }
}
$(document).on('click', '#rocket', function(event) {
    rocket.addClass('move');
    $('body, html').animate({
        scrollTop: 0
    }, 800);
});
$(document).on('animationEnd', function() {
    setTimeout(function() {
        rocket.removeClass('move');
    }, 400);

});
$(document).on('webkitAnimationEnd', function() {
    setTimeout(function() {
        rocket.removeClass('move');
    }, 400);
});
