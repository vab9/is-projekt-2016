"use strict";

$(function() {
    var request = $.get('/bestenliste');
    request.done(function(dt, textStatus, jqXHR) {
        console.log("bestenliste fetched!");
        var users = dt;
        for (var i = 0; i < users.length; i++) {
            addRow(users[i]);
        }
    });
});

function addRow(usr) {
    var tr = document.createElement('TR');
    var vorname_column = document.createElement('TD');
    vorname_column.appendChild(document.createTextNode(usr.vorname));
    var alter_column = document.createElement('TD');
    alter_column.appendChild(document.createTextNode(usr.alter));
    var score_column = document.createElement('TD');
    score_column.appendChild(document.createTextNode(usr.highscore));
    tr.appendChild(vorname_column);
    tr.appendChild(alter_column);
    tr.appendChild(score_column);
    $('tbody').append(tr);
}
