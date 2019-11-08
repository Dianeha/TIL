// KEY - VALUE: json(javaScript Object Notation) JS의 Object처럼 표기하는 방법
// JSON으로 표현된 데이터의 타입은 무조건 string

const rawJson = `{  // 
    "name": "Diane",
    "job": Developer,
}`

//parsing : 구문분석
const parseData = JSON.parse(rawJson) // 키밸류 형태로 바꿔줌

// serializing : 공용어로 번역(직렬화) string으로 만든다
const backToJSON = JSON.stringify(parseData)