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

    
    var cnt = 0
    $("[name='amount']").change(function () {
        for (let i = 0; i < $("[name='amount']").length; i++) {
            if ($("[name='amount']")[i] == $(this)[0]) {
                $("[name='price']")[i].value = $(this).val() * $("#orginal_price").val()
            }
        }

        $("#amount_form").submit();
    })
    
    for (let i = 0; i < $("[name='amount']").length; i++) {
        $("[name='price']")[i].value = $("[name='amount']")[i].value * $("#orginal_price").val()
        if ($("[name='item_selector']")[0].checked) {
            cnt += parseInt($("[name='price']")[i].value)
        }
    }
    $("[name='total_price']").val(cnt)
    $("[name='total_point']").val(cnt/$("#return_point").val())
})