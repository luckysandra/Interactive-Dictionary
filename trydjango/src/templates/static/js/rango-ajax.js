$(document).ready(function(){
	$('.like').click(function(){
		var wid = $(this).attr("word-id");
		jQuery.get('like_category/', {word:wid}, function(data){
			$('#likes_' + wid).html(data);
		});
		$(this).hide();
	});

	$('.dislike').click(function(){
		var wid = $(this).attr("word-id");
		jQuery.get('dislike_category/', {word:wid}, function(data){
				$('#dislikes_' + wid).html(data);
		})
		$(this).hide();
	});
});
