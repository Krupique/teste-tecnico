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
                
                
                strlHtml = '<div class="row" id="last-comment">';
                strlHtml += '<div class="col-1"><img src="../static/assets/user.png" width="50px"></div>';
                strlHtml += '<div class="col-11">';
                strlHtml += '<div class="row">';
                strlHtml += `<div class="col-3 comment-name"><p>${data.name}</p></div>`;
                strlHtml += `<div class="col-4 comment-date"><span><i class="fas fa-clock"></i>Agora</span></div>`;
                strlHtml += `<div class="col-12 comment-comment"><p>${data.comment}</p></div>`;
                strlHtml += '</div>';
                strlHtml += '</div>';
                strlHtml += '</div>';
                strlHtml += '<hr/>';

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

                paginationNumber += 20;

                var strlHtml = ''
                list_comments.forEach(e => {

                    strlHtml += '<div class="row">';
                    strlHtml += '<div class="col-1"><img src="../static/assets/user.png" width="50px"></div>';
                    strlHtml += '<div class="col-11">';
                    strlHtml += '<div class="row">';
                    strlHtml += `<div class="col-3 comment-name"><p>${e.fields.name}</p></div>`;
                    strlHtml += `<div class="col-4 comment-date"><span><i class="fas fa-clock"></i>${e.fields.created_at}</span></div>`;
                    strlHtml += `<div class="col-12 comment-comment"><p>${e.fields.comment}</p></div>`;
                    strlHtml += '</div>';
                    strlHtml += '</div>';
                    strlHtml += '</div>';
                    strlHtml += '<hr/>';
                });

                $('#list-comments').html(strlHtml);
                
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        });
    });
});