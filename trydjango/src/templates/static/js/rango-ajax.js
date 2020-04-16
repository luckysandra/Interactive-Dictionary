$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/words/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});

$('#dislikes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/words/dislike_category/', {category_id: catid}, function(data){
               $('#dislike_count').html(data);
               $('#dislikes').hide();
    });
});