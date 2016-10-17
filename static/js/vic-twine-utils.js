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

function speicherstandLaden() {
    console.log("trying to read spielstand from db and write to localStorage");
    //
    // maybe not use userid if we want to load somewhere else?!
    //
    var userid = getTwineVariable('userid');
    var get_url = '/loadgame/' + userid;
    var request = $.get(get_url);
    request.done(function(dt, textStatus, jqXHR) {
        console.log("request done");

        var k = dt['savegame-key'];
        var v = dt['savegame-value'];
        var score = dt['score'];

        setTwineVariable('score', score);
        window.localStorage.setItem(k, v);
        showCustomAlert($('.registration-success'), 'Spielstand importiert!');
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
    var score = getTwineVariable('score');

    // send of post request to save the game
    // var post_url = '/savegame'
    var data = {};
    data['username'] = username;
    data['savegame-key'] = keyName;
    data['savegame-value'] = keyValue;
    data['score'] = score;

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
        var btn = $('#speicherButton');
        btn.removeClass("btn-info").addClass('btn-success');
        btn.find('#speicher-glyph').removeClass('glyphicon-floppy-disk').addClass('glyphicon-floppy-saved');
        btn.find('#speicher-text').text(' Spiel gespeichert!');
    }).fail(function(jqXHR, textStatus, error) {
        console.log('saving to db failed!');
        var btn = $('#speicherButton');
        btn.removeClass("btn-info").addClass('btn-warning');
        btn.find('#speicher-glyph').removeClass('glyphicon-floppy-disk').addClass('glyphicon-floppy-remove');
        btn.find('#speicher-text').text(' Fehler beim Speichern!');
    });

}


$(function() {

    // Set Alert when leaving game
    window.onbeforeunload = function(e) {
      var dialogText = 'Achtung: Dein Spielstand geht verloren, wenn du die Seite verlässt, ohne vorher zu speichern!';
      e.returnValue = dialogText;
      return dialogText;
    };

    // Prevent forward and back buttons
    history.pushState(null, null, document.URL);
    window.addEventListener('popstate', function () {
        history.pushState(null, null, document.URL);
    });

    // rewrite original setItem function to check for twine savegame
    var originalSetItem = localStorage.setItem;
    window.localStorage.setItem = function(keyName, keyValue) {
        if (keyName.startsWith('(Saved Game')) {
            speicherstandSchreiben(keyName, keyValue);
        }
        originalSetItem.apply(this, arguments);
    };

});
