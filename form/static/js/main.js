
$(document).ready(function(){
    $("textarea").select(function(){
        $("#mybutton").prop({"disabled":false});
    });

    $('textarea').on('blur', function (e) {
        if (e.relatedTarget === null || e.relatedTarget.id !== 'mybutton')
            $('#mybutton').prop({'disabled': true})
    })

});