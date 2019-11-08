const numbers = [1, 2, 3, 4];

numbers[0] // 1
numbers[-1] // undefined >> index는 0 과 양의 정수만 써야합니다.
numbers.length; // 4

// 원본 파괴 methods
// const 로 선언했지만 = 을 이용한 재할당 아니고 methods는 가능하다
numbers.reverse();
numbers.push('a')
numbers.pop()
numbers.unshift('a') // 앞에 넣기 queue처럼
numbers.shift(); // 앞에서 빼기 return 'a'

// 원본 그대로 methods
numbers.includes(1) // True
numbers.indexOf(1) // 0
numbers.indexOf(100) // 없는 값의 index를 가져오라하면 -1을 줌

numbers.join() // "1,2,3" string
numbers.join('') // "123"
numbers.join('-') // "1-2-3"

