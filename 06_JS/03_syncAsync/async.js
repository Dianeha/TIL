// JS: Non-Blocking
function sleep_3s () {
    setTimeout(() => {console.log('Wake Up!')}, 3000);
}

console.log('시작')
sleep_3s()
console.log('끝')

// 그럼 어떤 함수/작업들이 Non blocking 한가요?

/*
지금 당장 해결할 수 없고
결과도 확신 할 수 없는 모든 일

*/