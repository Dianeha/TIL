// 1. input 태그 안의 값(value)을 잡는다.
const input = document.querySelector('#js-userinput').value; // '#' id , '.' class 

// 2. button 에  'click'이 일어났을 때, input에 Enter 키를 쳤을 때 1에서 잡은 값을 요청으로 보낸다.
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const resultArea = document.querySelector('#js-result-area');

// console.log(url)

button.addEventListener('click', () => {
    const inputValue = inputArea.value
    resultArea.innerHTML = inputValue
    searchAndPush(inputValue);
});

inputArea.addEventListener('keypress', (event) => {
    if (event.which === 13) {
        const inputValue = inputArea.value
        searchAndPush(inputValue);
        // inputValue 로 giphy 에 요청보내서 받기
    }
});

// 3. Giphy API 에서 넘겨준 Data를 index.html에서 보여준다.
const searchAndPush = (keyword) => {
    const imageCount = document.querySelector('#js-image-count').value;
    const API_KEY = 'XiMsf0tm40ypfjAPnTglDtUvRwdcWdMh'
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=${imageCount}&offset=0&rating=PG&lang=ko`;

    const AJAX = new XMLHttpRequest(); // 요청 준비
    AJAX.open('GET', url); // 요청 세팅
    AJAX.send(); // 요청 보내기

    AJAX.addEventListener('load', (answer) => { // 요청에 대한 응답을 기다렸다가 응답 오면
        const res = answer.target.response; 
        const giphyData = JSON.parse(res); // string 정보 가공해서
        const dataSet = giphyData.data;

        inputArea.value = null; // 기존 검색어를 비우는 코드
        resultArea.innerHTML = null; // 기존 것을 비우는 코드
        for (const data of dataSet) {
            pushToDOM(data.images.fixed_height.url);
        }
    });

    const pushToDOM = (imageUrl) => {
        const imageTag = document.createElement('img');
        imageTag.src = imageUrl;
        imageTag.alt = 'giphy-image';
        imageTag.classList.add('container-image');

        resultArea.appendChild(imageTag);
    };
    
}


