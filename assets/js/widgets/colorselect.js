var colorSelect = (function($) {
    var _$elm;
    var _id;
    var _choices;

    function init(id, choices) {
        _id = id;
        _choices = choices;
        _$elm = $("#"+_id);

        renderChoices();
        attachEvents();
    }

    function renderChoices() {
        var color, name;
        var currentColor = _$elm.val();
        for (i in _choices) {
            color = _choices[i][0];
            name = _choices[i][1];

            $colorBox = $("<div title='" + name + "' class='color-choice'></div>");
            $colorBox.css({
                'border-color': '#'+color,
                'background-color': '#'+color
            });
        
            if (currentColor && color == currentColor) {
                $colorBox.addClass('selected');
            }

            _$elm.before($colorBox);
            $colorBox.data("name", name); 
        }
    }

    function attachEvents() {
        var $colorChoices = $(".color-choice");
        $colorChoices.hover(function() {
            $(this).css('border-color', '');
        }, function() {
            $(this).css('border-color', $(this).css('background-color'));
        }).mouseleave();

        $colorChoices.click(function() {
            var $this = $(this);

            // This might return 'rgb' CSS format, so convert it to hex if
            // necesssary
            var color = $this.css('background-color');
            hex = rgb2hex(color).toUpperCase();
            _$elm.val(hex.replace(/^#/g, ""));

            $(".color-choice").removeClass("selected");
            $this.addClass("selected");
        });
    }

    function rgb2hex(rgbVal){
     rgb = rgbVal.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
     if (!rgb) return rgbVal;
     return "#" +
      ("0" + parseInt(rgb[1],10).toString(16)).slice(-2) +
      ("0" + parseInt(rgb[2],10).toString(16)).slice(-2) +
      ("0" + parseInt(rgb[3],10).toString(16)).slice(-2);
    }

    return {
        init: init
    }
})(django.jQuery);
