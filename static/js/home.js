$(function () {
    $("#greet h1").hide();
    $("#greet button").hide();
    $("#best_desc2").hide();
    $("#best_desc3").hide();
    $("#best_desc4").hide();
    $("#introduce").css('backgroundColor', '#fff')
    $("#introduce").children()[0].style.color = "#262626"

    // greeter
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
            $("#greet").css({zIndex: "-100"});
        });
    })
    
    // Home Navigator
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

    // BEST
    $("#best_btn button").click(function () {
        $("#best_btn button").css("border", "3px solid #fff").css("backgroundColor", "#262626").css("color", "#fff");
        $("#best_btn button").each(function () {
            this.disabled = false;
        })
        $(this).css("border", "3px solid #262626").css("backgroundColor", "#fff").css("color", "#262626");
        $(this)[0].disabled = true;

        if ($(this).text() == "BEST 코디") {
            $("#best_img").hide();
            $("#best_img img").attr("src", $("#best_cody_img").val())
            $("#best_img").fadeIn();
            $("#best_desc").children().each(function () {
                $(this).hide();
            })
            $("#best_desc1").fadeIn();

        } else if ($(this).text() == "BEST 깔맞춤") {
            $("#best_img").hide();
            $("#best_img img")[0].src = "https://image.hmall.com/static/2/3/41/27/2127413260_0.jpg?RS=600x600&AR=0"
            $("#best_img").fadeIn();
            $("#best_desc").children().each(function () {
                $(this).hide();
            })
            $("#best_desc2").fadeIn();
            
        } else if ($(this).text() == "BEST 포토후기") {
            $("#best_img").hide();
            $("#best_img img")[0].src = "https://i.pinimg.com/236x/2d/7b/90/2d7b90bd27f9fd3066da2f601af4a4c6.jpg"
            $("#best_img").fadeIn();
            $("#best_desc").children().each(function () {
                $(this).hide();
            })
            $("#best_desc3").fadeIn();
            
        } else if ($(this).text() == "이달의 판매왕") {
            $("#best_img").hide();
            $("#best_desc").children().each(function () {
                $(this).hide();
            })
            $("#best_desc4").fadeIn();
        }
    })

    // kakaomap
    function MapWalker(position){

        //커스텀 오버레이에 사용할 map walker 엘리먼트
        var content = document.createElement('div');
        var figure = document.createElement('div');
        var angleBack = document.createElement('div');

        //map walker를 구성하는 각 노드들의 class명을 지정 - style셋팅을 위해 필요
        content.className = 'MapWalker';
        figure.className = 'figure';
        angleBack.className = 'angleBack';

        content.appendChild(angleBack);
        content.appendChild(figure);

        //커스텀 오버레이 객체를 사용하여, map walker 아이콘을 생성
        var walker = new kakao.maps.CustomOverlay({
            position: position,
            content: content,
            yAnchor: 1
        });

        this.walker = walker;
        this.content = content;
    }

    //로드뷰의 pan(좌우 각도)값에 따라 map walker의 백그라운드 이미지를 변경 시키는 함수
    //background로 사용할 sprite 이미지에 따라 계산 식은 달라 질 수 있음
    MapWalker.prototype.setAngle = function(angle){

        var threshold = 22.5; //이미지가 변화되어야 되는(각도가 변해야되는) 임계 값
        for(var i=0; i<16; i++){ //각도에 따라 변화되는 앵글 이미지의 수가 16개
            if(angle > (threshold * i) && angle < (threshold * (i + 1))){
                //각도(pan)에 따라 아이콘의 class명을 변경
                var className = 'm' + i;
                this.content.className = this.content.className.split(' ')[0];
                this.content.className += (' ' + className);
                break;
            }
        }
    };

    //map walker의 위치를 변경시키는 함수
    MapWalker.prototype.setPosition = function(position){
        this.walker.setPosition(position);
    };

    //map walker를 지도위에 올리는 함수
    MapWalker.prototype.setMap = function(map){
        this.walker.setMap(map);
    };

    var mapCenter = new kakao.maps.LatLng(33.450701, 126.570667)
    var container = document.getElementById('map');
    var options = {
        center: mapCenter,
        level: 3
    };

    var map = new kakao.maps.Map(container, options);
    var mapTypeControl = new kakao.maps.MapTypeControl();
    map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);
    var zoomControl = new kakao.maps.ZoomControl();
    map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
    var imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_red.png',
    imageSize = new kakao.maps.Size(64, 69),
    imageOption = {offset: new kakao.maps.Point(27, 69)};
      
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imageOption),
        markerPosition = mapCenter;

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        position: markerPosition, 
        image: markerImage
    });
    marker.setMap(map);

    var content = '<div class="customoverlay">' +
        '  <a href="https://map.kakao.com/link/map/33.450701,126.570667" target="_blank">' +
        '    <span class="title">WHITE VALLEY</span>' +
        '  </a>' +
        '</div>';

    // 커스텀 오버레이가 표시될 위치입니다 
    var position = mapCenter;  

    // 커스텀 오버레이를 생성합니다
    var customOverlay = new kakao.maps.CustomOverlay({
        map: map,
        position: position,
        content: content,
        yAnchor: 1 
    });

    map.addOverlayMapTypeId(kakao.maps.MapTypeId.ROADVIEW);

var roadviewContainer = document.getElementById('roadview'); // 로드뷰를 표시할 div
var roadview = new kakao.maps.Roadview(roadviewContainer); // 로드뷰 객체
var roadviewClient = new kakao.maps.RoadviewClient(); // 좌표로부터 로드뷰 파노ID를 가져올 로드뷰 helper객체

    
// 지도의 중심좌표와 가까운 로드뷰의 panoId를 추출하여 로드뷰를 띄운다.
roadviewClient.getNearestPanoId(mapCenter, 50, function(panoId) {
    roadview.setPanoId(panoId, mapCenter); // panoId와 중심좌표를 통해 로드뷰 실행
});

var mapWalker = null;

// 로드뷰의 초기화 되었을때 map walker를 생성한다.
kakao.maps.event.addListener(roadview, 'init', function() {

    // map walker를 생성한다. 생성시 지도의 중심좌표를 넘긴다.
    mapWalker = new MapWalker(mapCenter);
    mapWalker.setMap(map); // map walker를 지도에 설정한다.

    // 로드뷰가 초기화 된 후, 추가 이벤트를 등록한다.
    // 로드뷰를 상,하,좌,우,줌인,줌아웃을 할 경우 발생한다.
    // 로드뷰를 조작할때 발생하는 값을 받아 map walker의 상태를 변경해 준다.
    kakao.maps.event.addListener(roadview, 'viewpoint_changed', function(){

        // 이벤트가 발생할 때마다 로드뷰의 viewpoint값을 읽어, map walker에 반영
        var viewpoint = roadview.getViewpoint();
        mapWalker.setAngle(viewpoint.pan);

    });

    // 로드뷰내의 화살표나 점프를 하였을 경우 발생한다.
    // position값이 바뀔 때마다 map walker의 상태를 변경해 준다.
    kakao.maps.event.addListener(roadview, 'position_changed', function(){

        // 이벤트가 발생할 때마다 로드뷰의 position값을 읽어, map walker에 반영 
        var position = roadview.getPosition();
        mapWalker.setPosition(position);
        map.setCenter(position);

    });
    });
})
