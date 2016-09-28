var mytextsizer=new fluidtextresizer({
    controlsdiv: "", //id of special div containing your resize controls. Enter "" if not defined
    targets: ["tw-passage"], //target elements to resize text within: ["selector1", "selector2", etc]
    levels: 3, //number of levels users can magnify (or shrink) text
    persist: "session", //enter "session" or "none"
    animate: 200 //animation duration of text resize. Enter 0 to disable
});
