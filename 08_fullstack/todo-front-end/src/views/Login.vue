<template>
  <div class="login">
      <h1>Login</h1>
      <loginForm></loginForm>
      <!-- <loginForm /> self closing 해도 가능-->
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm';
export default {
    name: 'Login',
    components: {
      LoginForm,
    }
}
</script>

<style>

</style>