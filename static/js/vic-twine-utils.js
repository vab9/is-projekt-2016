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
