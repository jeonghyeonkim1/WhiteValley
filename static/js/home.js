$(function () {
    $("#greet h1").hide();
    $("#greet button").hide();
    $("#greet").animate({ opacity: 1 }, 'slow', function () {
        $("#greet h1").show();
        var $typing = $("#typing");
        var text = $typing.text();
        $typing.html("");
        var chars = text.split("");
        chars.forEach(function (item) {
            item = (item == " ") ? "&nbsp" : item;

            $("<span></span>").html(item).appendTo($typing);
        });
        var $caret = $("<span></span>").attr("id", "caret").css({
            width: "0.4em",
        }).appendTo($typing);
        var delayStart = 600;
        var speed = 120;
        $typing.children(":not(#caret)").hide().each(function (index) {
            var delay = delayStart + speed * index;

            $(this).delay(delay).show(10);
        });
    });
    $("#greet button").delay(5000).fadeIn("slow");
    $("#greet button").click(function () {
        $("#greet").animate({ opacity: 0 }, 'slow', function () {
            $("#greet").hide();
        });
    })
})