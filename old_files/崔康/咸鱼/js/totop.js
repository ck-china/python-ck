$(function(){
	$(window).scroll(function(){
		var nowTop = $(document).scrollTop();
		if (nowTop > 300) {
			$('.zhiding').fadeIn();
		}
		else{
			$('.zhiding').fadeOut();
		}
			})
		$('.zhiding').click(function(){
			$('html,body').animate({scrollTop: 0});
		});
})