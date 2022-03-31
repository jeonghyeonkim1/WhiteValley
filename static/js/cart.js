$(function () {
    $(".item_all_selector").click(function () {
        if ($(".item_all_selector")[0].checked) {
            $(".item_selector")[0].checked = true;
        } else {
            $(".item_selector")[0].checked = false;
        }

        $(".item_selector").each(function () {
            if ($(".item_all_selector")[0].checked) {
                $(this)[0].checked = true;
            } else {
                $(this)[0].checked = false;
            }
        })
    })
})