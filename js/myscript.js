// functions & small media can be loaded at beginning
// scripts interacting with individual passages must be called
// on the respective passages

var keinAnschluss = new Audio("res/kein_anschluss.mp3");
// register shrink and enlarge Buttons

function shrinkText() {
    // console.log("shrinkText clicked");
    $('tw-passage').css("font-size", "-=5%");
    $('tw-passage').css("line-height", "-=5%");
}

function enlargeText() {
    // console.log("enlarge clicked"); 
    $('tw-passage').css("font-size", "+=5%");
    $('tw-passage').css("line-height", "+=5%");
}

function berndAnrufen() {
    keinAnschluss.play();
    $('.anrufen').hide();
    $('.angerufen').show();
    // setTimeout($('.versteckt').show(), 6000);
}


// add specific class to all tw-links for CSS insertion
// $("tw-link").addClass("btn btn-primary");


 ===============================
 TO GET USER INPUT FROM TEXT BOX
 ===============================
  if (typeof window.userInput == "undefined") {
     window.userInput = {
         submitName: function(inputName) {
             //Get the value of the textbox at time of click
             var newName = $("input[name='" + inputName + "']")[0].value;
             //Find the hook node based on name and set the text inside
             $("tw-hook[name*='" + inputName + "']").text(newName);
             //Log the Change
             console.log(inputName + " changed.")
         }
     }
  }
