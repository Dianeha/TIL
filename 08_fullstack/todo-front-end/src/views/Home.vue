<template>
  <div class="home">
    <h1>This is Home</h1>
    <TodoList />
  </div>
</template>

<script>
import router from '../router';
import TodoList from '../components/TodoList'


export default {
  name: 'home',
  components: {
    TodoList,
  },
  methods: {
    isLoggedIn () {
      this.$session.start();
      if (!this.$session.has('jwt')) { // login 안했으면 (== 'jwt'가 없으면)
        router.push('/login');
      }
    }
  },
  created () {
    this.isLoggedIn()
  },
}
</script>
