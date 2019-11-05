// Card 만들기
function init() {
    const button = document.querySelector('#js-todo-button');
    const inputTag = document.querySelector('#js-todo-input');
    const reverseBtn = document.querySelector('#js-reverse-button');

    reverseBtn.addEventListener('click', () => {
        const todoArea = document.querySelector('#js-todo-area');
        const todos = Array.from(document.querySelectorAll('.js-card')); // class가 js-card인 카드들을 모두 뽑아냄, 배열로 만든다.

        while (todoArea.firstChild) {
            todoArea.removeChild(todoArea.firstChild);
        }

        todos.reverse().forEach((todo) => {
            todoArea.appendChild(todo);
        })
    })

    button.addEventListener('click', () => {
        const inputArea = document.querySelector('#js-todo-input');
        createTodoCard(inputArea.value);
        inputArea.value = null;
    });

    inputTag.addEventListener('keydown', (e) => {
        if (e.which === 13) { // enter 칠 때 카드 생성
            const inputArea = document.querySelector('#js-todo-input');
            createTodoCard(inputArea.value);
            inputArea.value = null;
        }
    });

    const createTodoCard = (content, completed = false) => {
        // completed: 디폴트값 설정하는 것, 두번째 인자 아무것도 안들어오면 기본적으로 False 들어감
        const cardArea = document.querySelector('#js-todo-area');

        const todo = document.createElement('div');
        todo.className = 'ui segment js-card';

        const wrapper = document.createElement('div');
        wrapper.className = 'ui checkbox';

        // check 박스를 만들고
        const checkBox = document.createElement('input');
        checkBox.type = 'checkbox';

        // 만들어진 체크박스에 이벤트리스너를 달아서 카드를 생성
        checkBox.addEventListener('click', () => {
            if (checkBox.checked) {
                todo.classList.add('secondary');
                label.classList.add('done');
            } else {
                todo.classList.remove('secondary');
                label.classList.remove('done');
            }
        }) // 클릭이 일어나면 뒤 함수를 실행해주세요

        const label = document.createElement('label');
        label.innerHTML = content;

        const deleteIcon = document.createElement('i');
        deleteIcon.className = 'icon close custom-icon';

        deleteIcon.addEventListener('click', () => {
            cardArea.removeChild(todo); // 아래에 있는 todo
        })

        wrapper.appendChild(checkBox);
        wrapper.appendChild(label);
        todo.appendChild(wrapper);
        todo.appendChild(deleteIcon);
        cardArea.appendChild(todo);
    };
}

init();
