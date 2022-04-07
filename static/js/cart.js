$(function () {
    $("[name='amount']").change(function () {
        for (let i = 0; i < $("[name='amount']").length; i++) {
            if ($("[name='amount']")[i] == $(this)[0]) {
                $("[name='price']")[i].value = $(this).val() * $("#orginal_price").val()
            }
        }

        $("#amount_form").submit();
    })

    var cnt2 = 0
    $("[name='item_selector']").each(function () {
        if ($(this)[0].checked) {
            cnt2++;
        }

        if (cnt2 == $("[name='item_selector']").length) {
            $("#item_all_selector")[0].checked = true;
        } else {
            $("#item_all_selector")[0].checked = false;
        }

        $(this).change(function () {
            if (!$(this)[0].checked) {
                $("#item_all_selector")[0].checked = false;
            }
        })
    });

    var cnt = 0
    for (let i = 0; i < $("[name='amount']").length; i++) {
        if ($("[name='item_selector']")[i].checked) {
            $("[name='price']")[i].value = $("[name='amount']")[i].value * $("#orginal_price").val();
        } else {
            $("[name='price']")[i].value = 0;
        }

        cnt += parseInt($("[name='price']")[i].value);
    };
    $("[name='total_price']").val(cnt);
    $("[name='total_point']").val(`${cnt / $("#return_point").val()}원 적립 예정`);

    $("[name='checked_form']").each(function () {
        $(this).find("input").change(function () {
            $(this).parent()[0].submit()
        })
    })

    $("#item_all_selector").change(function () {
        if ($(this)[0].checked) {
            $("[name='item_selector']").each(function () {
                $(this)[0].checked = true;
                $("[name='item_all_bool']").val("True");
            });
        } else {
            $("[name='item_selector']").each(function () {
                $(this)[0].checked = false;
                $("[name='item_all_bool']").val("False");
            });
        }
        $("#item_all_form").submit();
    })

    $("#item_delete").on('submit', function () {
        if (confirm("해당 상품을 장바구니에서 제거하시겠습니까?")) {
            return true;
        }
        return false;
    })
})