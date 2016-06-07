$('.angerufen').hide();
// bernd anrufen funktion
$('.anrufen').click(berndAnrufen); 

// audio laden
var keinAnschluss = new Audio("res/kein_anschluss.mp3");

function berndAnrufen() {
    keinAnschluss.play();
    $('.anrufen').hide();
    $('.angerufen').show();
    // setTimeout($('.versteckt').show(), 6000);
}
