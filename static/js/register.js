"use strict";

function showCustomAlert(alertObj, msg='') {
    var newObj = alertObj.clone();
    newObj.append(msg).appendTo($('#alert-placeholder'));
    newObj.addClass('in');
    newObj.removeClass('registration-success registration-failure')
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
                var msg = jqXHR.status == 201 ? "Du hast dich erfolgreich registriert!" : "Du hast dich erfolgreich angemeldet!";
                showCustomAlert($('.registration-success'), msg);

                // save variables to twine from db data
                for (var key in dt) {
                    setTwineVariable(key, dt[key]);
                }

                // try to load savegame if player has already played
                if (jqXHR.status == 200) {
                    speicherstandLaden();
                    // moved this to vic-twine-utils
                    // showCustomAlert($('.registration-success'), 'Spielstand importiert!');
                }

                // disable submit button
                $('#confirmButton').prop('disabled', true);
                $('#zurueckButton').prop('disabled', true);
                $('#weiterButton').prop('disabled', false);

            }).fail(function(jqXHR, textStatus, errorThrown){
                var err = "(" + jqXHR.responseText + ")";
                showCustomAlert($('.registration-failure'), err);
            });
        } else {
            showCustomAlert($('.registration-failure'), '');
        }
        $('#alert-placeholder').show();
    });
});
