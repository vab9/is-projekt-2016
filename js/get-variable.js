"use strict";

function submitVariable(input) {
    //Get the value of the textbox at time of click
    var newVariable = $("input[name='" + input + "']")[0].value;
    //Find the hook node based on name and set the text inside
    $("tw-hook[name*='" + input + "']").text(newVariable);
    //Log the Change
    console.log(input + " changed to " + newVariable)
}
