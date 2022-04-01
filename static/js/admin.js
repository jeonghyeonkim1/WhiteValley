$(function () {
    $("#site_info").hide();
    $("#site_manager button:first").css("backgroundColor", "#212529")
    $("#site_manager button:first").css("color", "#fff")
    $("#site_manager button:first")[0].disabled = true;
    $("#site_manager button:first").click(function () {
        $("#site_manager button:first").css("backgroundColor", "#212529")
        $("#site_manager button:first").css("color", "#fff")
        $("#site_manager button:first")[0].disabled = true;
        $("#site_manager button:last").css("backgroundColor", "#fff")
        $("#site_manager button:last").css("color", "#212529")
        $("#site_manager button:last")[0].disabled = false;
        $("#site_info").hide();
        $("#co_info").fadeIn();
    })
    $("#site_manager button:last").click(function () {
        $("#site_manager button:last").css("backgroundColor", "#212529")
        $("#site_manager button:last").css("color", "#fff")
        $("#site_manager button:last")[0].disabled = true;
        $("#site_manager button:first").css("backgroundColor", "#fff")
        $("#site_manager button:first").css("color", "#212529")
        $("#site_manager button:first")[0].disabled = false;
        $("#co_info").hide();
        $("#site_info").fadeIn();
    })
})