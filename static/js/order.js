
$(function(){
    $("#direct1").hide();
    $("#selbox").change(function(){
        if($("#selbox").val()=="d1"){
            $("#direct1").show();
        }else{
            $("#direct1").hide();
        }
    });
    $("#direct2").hide();
    $("#selbox").change(function(){
        if($("#selbox").val()=="d2"){
            $("#direct2").show();
        }else{
            $("#direct2").hide();
        }
    });
});








