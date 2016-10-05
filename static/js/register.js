"use strict";

function setTwineVariable(name, value) {
    // get state Object
    var _harlowe_state = window.harlowe.State;
    if (typeof(name) === 'undefined' || name === '' || typeof(value) === 'undefined') {
        // then cannot set variable
        return;
    } else if (name[0] === '$') {
        // remove leading $ if present
        name = name.slice(1, name.length);
    }
    _harlowe_state.variables[name] = value;
}

function getTwineVariable(name) {
    // get state Object
    var _harlowe_state = window.harlowe.State;
    if (typeof(name) === typeof(undefined) || name === '') {
        return;
    } else if (name[0] === '$') {
        name = name.slice(1, name.length);
    }
    return _harlowe_state.variables[name];

}

$(function() {
    $("#registrationForm").submit(function(event){
        event.preventDefault();
        if ($("#registrationForm")[0].checkValidity()) {
            var $form = $('#registrationForm');
            var data = $form.serializeArray();
            var action_url = $form.attr('action');
            var posting = $.post(action_url, data);
            posting.done(function(dt, textStatus, jqXHR){
                console.log("successfully posted to database");
                $('.registration-success').clone().appendTo($('#alert-placeholder'));
                $('.registration-success').addClass('in');

                // save variables to twine from db data
                for (var key in dt) {
                    setTwineVariable(key, dt[key]);
                }

                // disable submit button
                $('#confirmButton').prop('disabled', true);
                $('#zurueckButton').prop('disabled', true);
                $('#weiterButton').prop('disabled', false);

            }).fail(function(jqXHR, textStatus, errorThrown){
                console.log("positng to database failed, god damn: " + errorThrown);
                var err = "(" + errorThrown + ")";
                $('.registration-failure').clone().append(err).appendTo('#alert-placeholder');
                $('.registration-failure').addClass('in');
            });
        } else {
            $('.registration-failure').clone().appendTo('#alert-placeholder');
            $('.registration-failure').addClass('in');
        }
        $('#alert-placeholder').show();
    });
});
