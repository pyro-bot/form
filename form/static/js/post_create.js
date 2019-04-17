
$(document).ready(function(){
    $("input").select(function(e){
        // $("#mybutton").prop({"disabled":false});
        if(window.getSelection)
            txt = window.getSelection().toString();
        else if(document.getSelection)
            txt = document.getSelection();
        else if(document.selection)
            txt = document.selection.createRange().text;
        $('.text').val(txt)
    });

    // $('input').on('blur', function (e) {
    //     // if (e.relatedTarget === null || e.relatedTarget.id !== 'mybutton')
    //     //     $('#mybutton').prop({'disabled': true})
        
    // })

    

});