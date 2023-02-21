
/*----------------------------------------*/
/* 22. Cart Plus Minus Button
/*----------------------------------------*/
$(".cart-plus-minus").append('<div class="dec qtybutton"><i class="fa fa-angle-down"></i></div><div class="inc qtybutton"><i class="fa fa-angle-up"></i></div>');
$(".qtybutton").on("click", function() {
    var $button = $(this);
    var oldValue = $button.parent().find("input").val();
    if ($button.hasClass('inc')) {
       var newVal = parseFloat(oldValue) + 1;
    } else {
        // Don't allow decrementing below zero
       if (oldValue > 0) {
         var newVal = parseFloat(oldValue) - 1;
         } else {
         newVal = 0;
       }
       }
    $button.parent().find("input").val(newVal);
   });


	 

	 
$('.addToCartBtn').click(function (e){
	e.preventDefault(); 
	console.log("AJAX FORM SUBMITTION");
  var product_id = $('#prdct_id').val();
	console.log(' Product ID: ' + product_id )
	var product_qty = $('#prdct_qty').val();
	console.log(' Product QTY: '+ product_qty)	
	
	var token= $('input[name=csrfmiddlewaretoken]').val();

	

	$.ajax({
		method:"POST",
		url: "/add-to-cart",
		data : {
			'product_id': product_id,
			'product_qty': product_qty,
			csrfmiddlewaretoken: token,

		},
		success:function (response) {
			console.log('SUBMIT')

		}
		
	});

});






/*----------------------------------------*/
/* 23. Single Prduct Carousel Activision
/*----------------------------------------*/
 	$(".sp-carousel-active").owlCarousel({
 		loop: true,
 		nav: false,
 		dots: false,
 		autoplay: false,
 		autoplayTimeout: 5000,
 		navText: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-left"></i>'],
 		item: 4,
 		responsive: {
 			0: {
 					items: 1
 			},
 			480: {
 					items: 2
 			},
 			768: {
 					items: 2
 			},
 			992: {
 					items: 3
 			},
 			1200: {
 					items: 4
 			}
 		}
 	});
/*----------------------------------------*/
/* 24. Star Rating Js
/*----------------------------------------*/
    $(function() {
          $('.star-rating').barrating({
            theme: 'fontawesome-stars'
        });
    });
/*----------------------------------------*/
/* 25. Zoom Product Venobox
/*----------------------------------------*/
    $('.venobox').venobox({
        spinner:'wave',
        spinColor:'#cb9a00',
    });
/*----------------------------------------*/
/* 26. WOW
/*----------------------------------------*/
    new WOW().init();
(jQuery);
/*----------------------------------------------------------------------------------------------------*/
/*------------------------------------------> The End <-----------------------------------------------*/
/*----------------------------------------------------------------------------------------------------*/