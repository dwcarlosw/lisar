
$(document).ready(function() {
    //get csrf token. Taken from docs https://docs.djangoproject.com/en/dev/ref/contrib/csrf/
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});



$(function() {

    window.addEventListener( 'load', initCommentSubmit, false );
    function initCommentSubmit(){
        add_comment_submit = document.getElementsByClassName("add-comment");
        for(var i=0; i<add_comment_submit.length; ++i){
            add_comment_submit[i].addEventListener("click", create_comment, false );
        }
    }
})

function create_comment(e) {
    var id = e.target.id.split("-")[1];
    var new_comment_id = "new_comment-"+id;

    var jqxhr = $.ajax({
        type: 'POST',
        url: comment_create_url,
        data: JSON.stringify( get_comment_data(new_comment_id) ),
        contentType: 'application/json; charset=utf-8',
        dataType:'json'
    });

    jqxhr.done(function(data) {
        $('#comment-'+id).html(data['text']);
//        alert(data['text']);
    });

    jqxhr.fail(function(data) {
        alert(data['responseText']);
    });
};

function get_comment_data ( new_comment_id ) {
    return {'name':"anna",
            'text':$('#'+new_comment_id).val()
            };
};


//$(function() {
//
//    comment_create_url = '{% url "add-comment" %}';
//    window.addEventListener( 'load', initCommentSubmit, false );
//    function initCommentSubmit(){
//        add_comment_submit = document.getElementsByClassName("add-comment");
//        comment_create_url = '{% url "add-comment" %}';
//        for(var i=0; i<add_comment_submit.length; ++i){
//            add_comment_submit[i].addEventListener("click", create_comment, false );
//        }
//    //    add_comment_submit.addEventListener("click", create_comment, false );
//
//    }
//    function create_comment(e) {
//        alert(JSON.stringify(get_comment_data()));
//        //return;
//        var jqxhr = $.ajax({
//            type: 'POST',
//            url: comment_create_url,
//            data: JSON.stringify( get_comment_data() ),
//            contentType: 'application/json; charset=utf-8',
//            dataType:'json'
//        });
//
//        jqxhr.done(function(data) {//var id = data.id;
//        });
//
//        jqxhr.fail(function(data) {
//        });
//    };
//
//    function get_comment_data () {
//        return {'name':"anna",
//                'text':"something"
//            };
//    };
//
//})





