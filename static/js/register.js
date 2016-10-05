"use strict";

function setTwineVariable(name, value) {
    // get state Object
    var _harlow_state = window.harlowe.State;
    if (typeof(name) === 'undefined' || name === '' || typeof(value) === 'undefined') {
        // then cannot set variable
        return;
    } else if (name[0] === '$') {
        // remove leading $ if present
        name = name.slice(1, name.length);
    }
    _harlow_state.variables[name] = value;
}

$(function() {
    $("#registrationForm").submit(function(event){
        event.preventDefault();
        if ($("#registrationForm")[0].checkValidity()) {
            var $form = $('#registrationForm');
            var data = $form.serializeArray();
            var url = $form.attr('action');
            $.post('/register', data).done(function(){
                console.log("successfully posted to database");
                $('.registration-success').clone().appendTo($('#alert-placeholder'));
                $('.registration-success').addClass('in');

                // save variables to twine
                for (var element of data) {
                    setTwineVariable(element['name'], element['value'])
                }

            }).fail(function(){
                console.log("positng to database failed, god damn");
                $('.registration-failure').clone().appendTo('#alert-placeholder');
                $('.registration-failure').addClass('in');
            });
        } else {
            $('.registration-failure').clone().appendTo('#alert-placeholder');
            $('.registration-failure').addClass('in');
        }
        $('#alert-placeholder').show();
    });
});
