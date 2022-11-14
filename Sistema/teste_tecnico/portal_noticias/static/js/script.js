var paginationNumber = 20;

$(document).ready(function(){
    
    var btnInsertComment = $('#btn-insert');
    var ulComments = $('#list-comments');
    var btnLoadComments = ('#btn-loadComments');
    


    $(btnInsertComment).on('click', function(e){
        
        var data = {
            'name': $('#name').val(),
            'email': $('#email').val(),
            'comment': $('#comment').val(),
            'noticia': $('#id-noticia').val()
        };

        $.ajax({
            type: 'POST',
            url: 'postComment',
            data: data, 
            success: function (response) {
                console.log('Success');

                var strlHtml = '<div id="post-enviado">Seu comentário foi enviado com sucesso</div>';
                $('#form-comment').html(strlHtml);

                
                strlHtml = `<li id="last-comment" class="li-comment">${data.name} Now - ${data.comment}</li>`;
                $('#list-comments').prepend(strlHtml);

                
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        });

    });
    

    $(btnLoadComments).on('click', function(e){

        var data = {
            'noticia': $('#id-noticia').val(),
            'paginationNumber': paginationNumber
        };

        $.ajax({
            type: 'POST',
            url: 'loadComments',
            data: data, 
            success: function (response) {
                list_comments = JSON.parse(response.instance)
                
                console.log(list_comments);




                paginationNumber += 20;


                
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        });
    });
});