"use strict";

function showCustomAlert(alertObj, msg='') {
    var newObj = alertObj.clone();
    newObj.append(msg).appendTo($('#alert-placeholder'));
    newObj.addClass('in');
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
                var msg = 'score' in dt ? "Willkommen! Du wurdest erfolgreich registriert!" : "Willkommen zurück! Du wurdest erfolgreich angemeldet!";
                showCustomAlert($('.registration-success'), msg);

                // save variables to twine from db data
                for (var key in dt) {
                    setTwineVariable(key, dt[key]);
                }

                // try to load savegame if it exists
                if ('score' in dt && speicherstandLaden(dt)) {
                    showCustomAlert($('.registration-success'), 'Spielstand importiert!')
                }

                // disable submit button
                $('#confirmButton').prop('disabled', true);
                $('#zurueckButton').prop('disabled', true);
                $('#weiterButton').prop('disabled', false);

            }).fail(function(jqXHR, textStatus, errorThrown){
                console.log("positng to database failed, god damn: " + errorThrown);
                var err = "(" + errorThrown + ")";
                showCustomAlert($('.registration-failure'), err);
            });
        } else {
            showCustomAlert($('.registration-failure'), '');
        }
        $('#alert-placeholder').show();
    });
});
