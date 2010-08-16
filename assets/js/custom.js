function show_html_overlay(container_class) {
    // if the function argument is given to overlay,
    // it is assumed to be the onBeforeLoad event listener
    $("a[rel]").overlay({

      mask: 'darkred',
      effect: 'apple',

      onBeforeLoad: function() {

        // grab wrapper element inside content
        var wrap = this.getOverlay().find(container_class);

        // load the page specified in the trigger
        wrap.load(this.getTrigger().attr("href"));
      }
    });
}
  
function show_overlay(element_class) {
    //$(element_class).colorbox({ iframe: true, innerHeight:600, innerWidth:500});
    $(element_class).colorbox();
        $('.overlay_man').colorbox({ iframe: true, innerHeight:600, innerWidth:500});
}
