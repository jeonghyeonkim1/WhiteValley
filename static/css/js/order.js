var colorPicker;

function showModal() {
    $(".modal-window").show();
    colorPicker.color.hsl = { h: 0, s: 0, l: 100 };
}       

function hideModal() {
    $(".modal-window").hide();
}    


$(document).ready(function(){

    colorPicker = new iro.ColorPicker("#picker", {
        width: 200,
      });

    let canvas = document.getElementById("Canvas")
    var img = new Image();
    img.src = "https://i.ibb.co/0JMMtF1/shortw.png"
    let ctx;
    ctx = canvas.getContext("2d");

    img.onload = function(){
        ctx.drawImage(img, 0, 0,400,400);
    };


});








