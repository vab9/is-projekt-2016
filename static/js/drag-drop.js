"use strict";

function dragenter(ev) {
    ev.currentTarget.style.opacity = 0.4;
}

function dragleave(ev) {
    ev.currentTarget.style.opacity = 1.0;
}

function allowDrop(ev) {
    ev.preventDefault();
}

function dragstart(ev) {
    ev.dataTransfer.setData("id", ev.target.id);
    ev.dataTransfer.setData("text", ev.target.classList[1]);
}

function drop(ev) {
    dragleave(ev);
    ev.preventDefault();

    var element_id = ev.dataTransfer.getData("id");
    var classname = ev.dataTransfer.getData("text");

    if (ev.target.classList.contains(classname)) {
        // make sure we append to target and not a measure already inside it
        if (ev.target.classList.contains("target")) {
            ev.target.appendChild(document.getElementById(element_id));
        } else {
            ev.target.parentNode.appendChild(document.getElementById(element_id));
        }
    }

    // check if game complete
    var left_column = document.getElementById("left_column");
    if (left_column.childElementCount === 0) {
        var newSpan = document.createElement("span");
        var newChild = document.createTextNode("Super! Alle Maßnahmen wurden richtig zugeordnet!");
        newSpan.appendChild(newChild);
        left_column.appendChild(newSpan);

    }
}

console.log("drag-drop loaded");
