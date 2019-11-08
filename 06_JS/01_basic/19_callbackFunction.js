function a(x, y) {
    console.log(x, y)
    return x + y;
}

function b(n) {
    return n++; // return 하고 나서 n += 1
    return ++n; // n += 1 하고 나서 return 
}

function c(f1, f2) {
    return f1(10, 10) + f2(99);
}

console.log(
    c(a, b)
    // c(b, a) => 인자 개수가 맞지 않아도 에러나지 않고 결과가 NaN가 나옴
)