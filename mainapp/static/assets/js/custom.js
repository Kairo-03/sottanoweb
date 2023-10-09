$(document).ready(function () {
    "use strict";

    const path = window.location.pathname;
    let nav = document.querySelector("#mi-nav");
    let header = document.querySelector("#header__transparente");

    function setOpaqueBackground() {
        nav.style.backgroundColor = "rgba(255, 255, 255, 1)"; // Fondo blanco
        header.style.backgroundColor = "rgba(255, 255, 255, 1)"; // Fondo blanco
    }

    function setTransparentBackground() {
        nav.style.backgroundColor = "rgba(0, 0, 0, 0)"; // Transparente
        header.style.backgroundColor = "rgba(0, 0, 0, 0)"; // Transparente
    }

    function cambiarColorBotones(color) {
        let botones = document.querySelectorAll("#navbar-menu .smooth-menu a");
        for (let i = 0; i < botones.length; i++) {
            botones[i].style.color = color;
        }
    }

    // Comprobar si la ruta actual es servicios, login o register
    if (path.includes("/servicios") || path.includes("/login") || path.includes("/register")) {
        setOpaqueBackground();
        cambiarColorBotones("black");
    } else {
        window.addEventListener("scroll", function () {
            if (window.scrollY > 100) {
                setOpaqueBackground();
                cambiarColorBotones("black");
            } else {
                setTransparentBackground();
                cambiarColorBotones("white");
            }
        });
    }

    function cambiarColorBotones(color) {
        let botones = document.querySelectorAll("#navbar-menu .smooth-menu a");

        for (let i = 0; i < botones.length; i++) {
            botones[i].style.color = color;
        }
    }

		function prevSlide() {
			currentIndex = (currentIndex - 1 + items.length) % items.length;
			showSlide(currentIndex);
		}

		function nextSlide() {
			currentIndex = (currentIndex + 1) % items.length;
			showSlide(currentIndex);
		}

		// Asignar funciones a los botones
		document.querySelector('.carousel-control-prev').addEventListener('click', prevSlide);
		document.querySelector('.carousel-control-next').addEventListener('click', nextSlide);
	});

	/*=========== TABLE OF CONTENTS ===========
	1. Scroll To Top 
	2. Smooth Scroll spy
	3. Progress-bar
	4. owl carousel
	5. welcome animation support
	======================================*/

	// 1. Scroll To Top 
	$(window).on('scroll', function () {
		if ($(this).scrollTop() > 600) {
			$('.return-to-top').fadeIn();
		} else {
			$('.return-to-top').fadeOut();
		}
	});
	$('.return-to-top').on('click', function () {
		$('html, body').animate({
			scrollTop: 0
		}, 1500);
		return false;
	});



	// 2. Smooth Scroll spy

	$('.header-area').sticky({
		topSpacing: 0
	});

	//=============

	$('li.smooth-menu a').bind("click", function (event) {
		var anchor = $(this);
		var href = anchor.attr('href');
	
		// Comprueba si el enlace comienza con "#", lo que indica un enlace interno.
		if (href.startsWith("#")) {
			event.preventDefault();
			$('html, body').stop().animate({
				scrollTop: $(href).offset().top - 0
			}, 1200, 'swing');
			
		}
	});

	$('body').scrollspy({
		target: '.navbar-collapse',
		offset: 0
	});

	// 3. Progress-bar

	var dataToggleTooTip = $('[data-toggle="tooltip"]');
	var progressBar = $(".progress-bar");
	if (progressBar.length) {
		progressBar.appear(function () {
			dataToggleTooTip.tooltip({
				trigger: 'manual'
			}).tooltip('show');
			progressBar.each(function () {
				var each_bar_width = $(this).attr('aria-valuenow');
				$(this).width(each_bar_width + '%');
			});
		});
	}

	// 4. owl carousel

	// i. client (carousel)

	$('#client').owlCarousel({
		items: 7,
		loop: true,
		smartSpeed: 1000,
		autoplay: true,
		dots: false,
		autoplayHoverPause: true,
		responsive: {
			0: {
				items: 2
			},
			415: {
				items: 2
			},
			600: {
				items: 4

			},
			1199: {
				items: 4
			},
			1200: {
				items: 7
			}
		}
	});


	$('.play').on('click', function () {
		owl.trigger('play.owl.autoplay', [1000])
	})
	$('.stop').on('click', function () {
		owl.trigger('stop.owl.autoplay')
	})


	// 5. welcome animation support

	$(window).load(function () {
		$(".header-text h2,.header-text p").removeClass("animated fadeInUp").css({ 'opacity': '0' });
		$(".header-text a").removeClass("animated fadeInDown").css({ 'opacity': '0' });
	});

	$(window).load(function () {
		$(".header-text h2,.header-text p").addClass("animated fadeInUp").css({ 'opacity': '0' });
		$(".header-text a").addClass("animated fadeInDown").css({ 'opacity': '0' });
	});