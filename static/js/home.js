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
    
    $(window).scroll(function () {
        if ($("#scrollspyHeading1").offset().top > window.pageYOffset) {
            $("#contents_nav li").css('backgroundColor', '#262626')
            $("#contents_nav li a").css('color', '#fff')
            $("#introduce").css('backgroundColor', '#fff')
            $("#introduce").children()[0].style.color = "#262626"
        } else if ($("#scrollspyHeading2").offset().top > window.pageYOffset) {
            $("#contents_nav li").css('backgroundColor', '#262626')
            $("#contents_nav li a").css('color', '#fff')
            $("#event").css('backgroundColor', '#fff')
            $("#event").children()[0].style.color = "#262626"
        } else if ($("#scrollspyHeading3").offset().top > window.pageYOffset) {
            $("#contents_nav li").css('backgroundColor', '#262626')
            $("#contents_nav li a").css('color', '#fff')
            $("#best").css('backgroundColor', '#fff')
            $("#best").children()[0].style.color = "#262626"
        } else if ($("#scrollspyHeading4").offset().top > window.pageYOffset) {
            $("#contents_nav li").css('backgroundColor', '#262626')
            $("#contents_nav li a").css('color', '#fff')
            $("#notice").css('backgroundColor', '#fff')
            $("#notice").children()[0].style.color = "#262626"
        } else if ($("#scrollspyHeading5").offset().top > window.pageYOffset) {
            $("#contents_nav li").css('backgroundColor', '#262626')
            $("#contents_nav li a").css('color', '#fff')
            $("#roadmap").css('backgroundColor', '#fff')
            $("#roadmap").children()[0].style.color = "#262626"
        }
    })

    $("#best_btn button").click(function () {
        $("#best_btn button").css("border", "3px solid #fff").css("backgroundColor", "#262626").css("color", "#fff");
        $("#best_btn button").each(function () {
            this.disabled = false;
        })
        $(this).css("border", "3px solid #262626").css("backgroundColor", "#fff").css("color", "#262626");
        $(this)[0].disabled = true;

        if ($(this).text() == "BEST 코디") {
            $("#best_img")[0].src = "http://maybnous.com/file_data/seulgikim/2019/01/29/f34ca27ff87662feaf085171f7511a6a.jpg"
        } else if ($(this).text() == "BEST 깔맞춤") {
            $("#best_img")[0].src = "https://image.hmall.com/static/2/3/41/27/2127413260_0.jpg?RS=600x600&AR=0"
        } else if ($(this).text() == "BEST 포토후기") {
            $("#best_img")[0].src = "https://i.pinimg.com/236x/2d/7b/90/2d7b90bd27f9fd3066da2f601af4a4c6.jpg"
        } else if ($(this).text() == "이달의 판매왕") {
            $("#best_img")[0].src = "https://i.pinimg.com/736x/b1/6a/a6/b16aa66215b70e2d925a6ee4877cfa39.jpg"
        }
    })
})