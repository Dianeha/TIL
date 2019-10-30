// JS 함수
// 1. 선언형
function a (x, y) {
    return x + y;
}

// 2. 할당형
const b = function (x, y) {
    return x + y;
};

// 3. arrow function (기본적으로는 할당형)
const b = (x, y) => {
    return x + y;
};

// 3-1. 축약 1번 : 함수 블록내에 코드가 return 문 포함 한줄이라면 {}+return 생략 가능
const d = (x, y) => x + y;
// 3-2. 축약 2번 : 함수의 인자가 단 하나일 때 () 생략가능
const e = x => {
    return x ** 2;
};

// 인자가 1개고 return 포함 한줄일 때
const e = x => x ** 2;

// 3-3. 축약 3번 : 함수 인자가 하나도 없으면?
const e = () => { // () 써야함
    return False
}

const e = _ => { // _ 로 쓰기도함
    return False
}