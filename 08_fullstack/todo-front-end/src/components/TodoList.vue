<template>
  <div class="todo-list">
    <div v-for="todo in todos" :key="todo.id" class="card">
        <div class="card-body d-flex justify-content-between">
            <span>{{ todo.title }}</span>
        </div>
    </div>
  </div>
</template>

<script>
const axios = require('axios');
/* 
1. REQ 보내기
    1. GET
    2. http://127.0.0.1:8000/api/v1/users/my_todos/
    3. REQ.Header => Authorization: JWT [YOUR TOKEN HERE]
    (4. Body 에 내용 추가) POST와 PATCH 에 대해서만 실행


*/

export default {
    name: 'TodoList',
    data () {
        return {
            todos: []
        }
    },
    methods: {
        // isLoggedIn () {},
        getTodos() {
            this.$session.start();
            const token = this.$session.get('jwt');
            const options = {
                headers: {
                    Authorization: `JWT ${token}`
                },

            }
            axios.get('http://127.0.0.1:8000/api/v1/users/my_todos/', options)
                .then(res => this.todos = res.data.todo_set)
                .catch(err => console.log(err.response))
        }
    },
    created () {
        this.getTodos() // 시작할 때 todos 목록 뜨도록 함 (vue life cycle을 통해 특정 시점에 특정 명령을 하도록 할 수 있음)
    }
}
</script>

<style>

</style>