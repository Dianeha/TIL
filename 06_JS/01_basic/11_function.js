/* python 
    def adder1(x, y):
        return x + y
*/

function adder1(x, y) { // 선언식(= 이 없으므로 ; 쓰지 않음)
    return x + y;
}
    
const adder2 = function(x, y) { // 할당식 ; 붙음
    return x + y;
};

/* python Lambda 표현식
    adder3 = lambda x, y: x + y
*/

// ES6+ Arrow Function
// 1. function 을 지운다
// 2. ()와 {} 사이에 => 를 넣는다
const adder3 = (x, y) => {
    return x + y;
};