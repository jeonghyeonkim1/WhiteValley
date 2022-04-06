$(function () {
    // collapse 창
    shopping_collapse = 0;
    cs_collapse = 0;
    $("#nav_shopping").on('click', function () {
        $("#nav_collapse h1").text("SHOPPING");
        $("#cs_links").hide();
        $("#shopping_links").show();

        if (cs_collapse == 0 && shopping_collapse == 0) {
            shopping_collapse += 1;
            $("#nav_collapse").slideDown();
        } else if (cs_collapse == 1 && shopping_collapse == 0) {
            cs_collapse -= 1;
            shopping_collapse += 1;
        } else if (cs_collapse == 0 && shopping_collapse == 1) {
            shopping_collapse -= 1;
            $("#nav_collapse").slideUp();
        }
    })
    $("#nav_cs").on('click', function () {
        $("#nav_collapse h1").text("CS");
        $("#shopping_links").hide();
        $("#cs_links").show();

        if (cs_collapse == 0 && shopping_collapse == 0) {
            cs_collapse += 1;
            $("#nav_collapse").slideDown();
        } else if (cs_collapse == 1 && shopping_collapse == 0) {
            cs_collapse -= 1;
            $("#nav_collapse").slideUp();
        } else if (cs_collapse == 0 && shopping_collapse == 1) {
            shopping_collapse -= 1;
            cs_collapse += 1;
        }
    })
    $("#collapse_exit").click(function () {
        $("#nav_collapse").slideUp();
        shopping_collapse = 0;
        cs_collapse = 0;
    })
    $(".navbar-toggler").click(function () {
        $("#nav_collapse").slideUp();
        shopping_collapse = 0;
        cs_collapse = 0;
    })

    // collpase 창 resize 시 slideup
    $(window).resize(function () {
        if (window.innerWidth < 991) {
            $("#nav_collapse").slideUp();
            shopping_collapse = 0;
            cs_collapse = 0;
        };
    });

    // logout
    $("#logout_btn").click(function () {
        if (confirm("로그아웃 하시겠습니까?")) {
            alert("로그아웃에 성공했습니다!")
            $("#logout_form").submit();
        }
    })
})