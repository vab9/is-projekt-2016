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
    console.log("trying to read spielstand from db and write to localStorage");
    //
    // maybe not use userid if we want to load somewhere else?!
    //
    var get_url = '/loadgame/' + data.userid;
    var request = $.get(get_url);
    request.done(function(dt, textStatus, jqXHR) {
        // OK 200
        // add to local storage
        // DOUBLE CHECK THIS!!!
        console.log(dt);
        var k = dt[0];
        var v = dt[1];
        window.localStorage.setItem(k, v);
        return true;
    }).fail(function(jqXHR, textStatus, errorThrown) {
        // GET FAILED
        return false;
    });
}

function speicherstandSchreiben(keyName, keyValue) {
    console.log("trying to write spielstand to db");
    if (keyName.startsWith('(Saved Game Filename')) {
        return;
    }
    // read username or userid
    var re = /\)\s(.+)$/;
    var username = keyName.match(re)[1];

    // send of post request to save the game
    // var post_url = '/savegame'
    var data = {};
    data['username'] = username;
    data['savegame-key'] = keyName;
    data['savegame-value'] = keyValue;

    var posting = $.ajax({
              url: '/savegame',
              type: "POST",
              contentType:"applicaton/json",
              dataType:"json",
              data: JSON.stringify(data)
    });
    posting.done(function(dt, textStatus, jqXHR) {
        console.log('saved: ');
        console.log(dt);
    });

}


$(function() {
    // rewrite original setItem function to check for twine savegame
    var originalSetItem = localStorage.setItem;
    window.localStorage.setItem = function(keyName, keyValue) {
        if (keyName.startsWith('(Saved Game')) {
            speicherstandSchreiben(keyName, keyValue);
        }
        originalSetItem.apply(this, arguments);
    };

});
