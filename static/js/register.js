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

function speicherstandLaden(data) {
    // return true if speicherstand added to localstorage
    var get_url = '/loadgame/' + data['userid'];
    var request = $.get(get_url);
    request.done(function(dt, textStatus, jqXHR) {
        // OK 200
        // add to local storage
        // DOUBLE CHECK THIS!!!
        var k = dt[0];
        var v = dt[1];
        window.localStorage.setItem(k, v);
        return true;
    }).fail(function(jqXHR, textStatus, errorThrown) {
        // GET FAILED
        return false;
    });
}

// function speicherstandSchreiben()

function showCustomAlert(alertObj, msg='') {
    alertObj.clone().append(msg).appendTo($('#alert-placeholder'));
    alertObj.addClass('in');
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
