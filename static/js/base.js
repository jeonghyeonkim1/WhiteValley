$(function () {
    // collapse 창
    $("#nav_collapse").slideUp(0);

    shopping_collapse = 0;
    cs_collapse = 0;
    $("#nav_shopping").on('click', function () {
        $("#nav_collapse h1").text("SHOPPING");
        $("#nav_collapse ul").html(
            "<li class='nav-item'><a href='#' class='nav-link text-decoration-none text-white'>커스텀주문</a></li>\
            <li class='nav-item'><a href='#' class='nav-link text-decoration-none text-white'>완성품</a></li>\
            <li class='nav-item'><a href='#' class='nav-link text-decoration-none text-white'>깔맞춤</a></li>\
            <li class='nav-item'><a href='#' class='nav-link text-decoration-none text-white'>포토후기</a></li>"
        );

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
        $("#nav_collapse ul").html(
            "<li class='nav-item'><a href='#' class='nav-link text-decoration-none text-white'>공지사항</a></li>\
            <li class='nav-item'><a href='#' class='nav-link text-decoration-none text-white'>이벤트</a></li>\
            <li class='nav-item'><a href='#' class='nav-link text-decoration-none text-white'>1:1문의</a></li>\
            <li class='nav-item'><a href='#' class='nav-link text-decoration-none text-white'>FAQ</a></li>"
        );

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
})