/* 
    Javascript는 event-driven (이벤트 기반)
    특정 이벤트(click, network request ...)가 발생하면
    무엇을 할지(함수) 미리 등록해서 사용한다.
    button.addEventListener('click', function() {...})
*/

// 함수의 실행 순서

function a () {
    console.log('a');
}

function b () {
    a();
    console.log('b');
}

function c () {
    a();
    b();
    console.log('c');
}

c(); //aabc