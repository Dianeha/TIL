$(document).ready(function() {
    'use strict';
    
    paper.install(window);
    paper.setup(document.getElementById('mainCanvas'));

    //TODO
    
    // 1. 중앙에 원 하나
    // var c = Shape.Circle(200, 200, 50);
    // c.fillColor = 'green';

    // 2. 바둑판식 원배열
    // var c;
    // for(var x=25; x<400; x+=50) {
    //     for(var y=25; y<400; y+=50) {
    //         c = Shape.Circle(x, y, 20);
    //         c.fillColor = 'green';
    //     }
    // }

    var c = Shape.Circle(200, 200, 80);

    // 3. 사용자 입력 받아 해당 자리에 원생성
    var tool = new Tool(); // 객체를 만들어서
    tool.onMouseDown = function(event) { // 이벤트 핸들러를 연결, 해당 이벤트가 발생해야지만
        var c = Shape.Circle(event.point, 20); // 하위의 코드가 실행됨
        c.fillColor = 'green';
    };

    paper.view.draw();
})