// 핵심은 함수가 인자로 들어간다는 점

// ES5
var colors = ['red', 'blue', 'green']

for (var i=0; i < colors.length; i++) {
    console.log(colors[i]);
}

// ES6+

// 1. forEach 는 return이 없다
// 1. 
function logger(x) {
    console.log(x)
}

colors.forEach(logger) 

// 2. (1번과 동일)
colors.forEach(function logger(x) {
    console.log(x)
})

// ======================================================
// 2. Map
// python 에 map(int, iter) 와 비슷한 역할

// ES5
const numbers = [1,2,3];
const doubleNumbers = [];

for (let i=0; i < numbers.length; i++) {
    doubleNumbers.push(numbers[i]*2);
}

console.log(doubleNumbers)

// ES6+

const tripleNumbers = numbers.map(function(number) {
    return number * 3;
}) // numbers 의 요소 하나하나를 함수에 넣는다.

// const tripleNumbers = numbers.map((number) => {
//     return number * 3;
// })

console.log(tripleNumbers)

// ======================================================

// 3. filter 함수 : 
// callbackFunction의 조건에 해당하는 모든 요소가 있는 배열을 새로 생성



// ES5
const products = [
    {name: 'apple', type: 'fruit'},
    {name: 'c', type: 'vege'},
    {name: 'd', type: 'fruit'},
    {name: 'e', type: 'vege'},
];

const fruits = []
for (const product of products) {
    if (product.type === 'fruit') {
        fruits.push(product);
    }
}
console.log(fruits);

// ES6+
const vegetables = products.filter((product) => {
    return product.type === 'vege';
}) // return 이 True면 넣고 False는 안넣고

console.log(vegetables)