// audio laden
var keinAnschluss = new Audio("res/kein_anschluss.mp3");

// elemente verstecken
$('.angerufen').hide();

// register shrink and enlarge Buttons
$('.shrink').click(shrinkText);
$('.enlarge').click(enlargeText);
// bernd anrufen funktion
$('.anrufen').click(berndAnrufen);


function berndAnrufen() {
    keinAnschluss.play();
    $('.anrufen').hide();
    $('.angerufen').show();
    // setTimeout($('.versteckt').show(), 6000);    
}

function shrinkText() {
    console.log("shrinkText clicked");
    // document.body.style.fontSize = "10";
    $('tw-passage').css("font-size", "-=5%");
    $('tw-passage').css("line-height", "-=5%");
}

function enlargeText() {
   console.log("enlarge clicked"); 
    $('tw-passage').css("font-size", "+=5%");
    $('tw-passage').css("line-height", "+=5%");
   // document.body.style.fontSize = "24";
   
   // $('body').css("font-size", "3em");

   // var passage = document.getElementsByTagName("tw-passage");
   
   // passage.style.color = "red";

}


// add specific class to all tw-links for CSS insertion
// $("tw-link").addClass("btn btn-primary");


// ===============================
// TO GET USER INPUT FROM TEXT BOX
// ===============================
// if (typeof window.customScripts == "undefined") {
//     window.customScripts = {
//         submitName: function(inputName) {
//             //Get the value of the textbox at time of click
//             var newName = $("input[name='" + inputName + "']")[0].value;
//             //Find the hook node based on name and set the text inside
//             $("tw-hook[name*='" + inputName + "']").text(newName);
//             //Log the Change
//             console.log(inputName + " changed.")
//         }
//     }; 
// };
