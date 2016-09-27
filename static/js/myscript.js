// functions & small media can be loaded at beginning
// scripts interacting with individual passages must be called
// on the respective passages

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


// add specific class to all tw-links for CSS insertion
// $("tw-link").addClass("btn btn-primary");
