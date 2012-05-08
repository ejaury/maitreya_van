(function($) {
    $.fn.prepopulate_text = function(dependencies, maxLength) {
        /*
            Taken from Django prepopulate.js
            Depends on urlify.js
            Populates a selected field with the values of the dependent fields,
            URLifies and shortens the string. 
            dependencies - array of dependent fields id's 
            maxLength - maximum length of text
        */
        return this.each(function() {
            var field = $(this);

            field.data('_changed', false);
            field.change(function() {
                field.data('_changed', true);
            });

            var populate = function () {
                // Bail if the fields value has changed
                if (field.data('_changed') == true) return;
 
                var values = [];
                $.each(dependencies, function(i, field) {
                  var field_val = $(field).val();
                  if ($(field).val().length > 0 && field_val.length <= maxLength) {
                      values.push($(field).val());
                  } else {
                      values.push($(field).val().substr(0, maxLength));
                  }
                })
                field.val(values.join(' '));
            };

            $(dependencies.join(',')).keyup(populate).change(populate).focus(populate);
        });
    };
})(django.jQuery);
