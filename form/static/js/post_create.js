
$(document).ready(function(){
    $("#id_post-body").select(function(e){
        var start = e.target.selectionStart;
        var end = e.target.selectionEnd;
        var value = e.target.value.substr(start, end - start);
        var entitys = $('.entity');
        for (var i in entitys) {
            var entity = entitys[i];
            var input = $('input', entity);
            if (input.length === 0) continue;
            if (input[0].value == '') {
                $(entity).removeClass('d-none');
                $('.pos', entity).val(start);
                $('.text', entity).val(value);
                break;

            }
        }

    });
    //
    // $('#id_post-body').on('blur', function (e) {
    //     if (e.relatedTarget === null || e.relatedTarget.id !== 'mybutton')
    //         $('#id_post-body').prop({'disabled': true})
    // })



    // $("input").select(function(e){
    //     // $("#mybutton").prop({"disabled":false});
    //     if(window.getSelection)
    //         txt = window.getSelection().toString();
    //     else if(document.getSelection)
    //         txt = document.getSelection();
    //     else if(document.selection)
    //         txt = document.selection.createRange().text;
    //     $('.text').val(txt)
    // });

    // $('input').on('blur', function (e) {
    //     // if (e.relatedTarget === null || e.relatedTarget.id !== 'mybutton')
    //     //     $('#mybutton').prop({'disabled': true})
        
    // })

    

});