<template>
  <div class="login-form">
    <div v-if="isLoading" class="spinner-border" role="status">
      <span class="sr-only">Loading</span>
    </div>

    <form v-else class="login-input" @submit.prevent="login">
    <div v-if="errors.length" class="error-list alert alert-danger">
        <h4>아래의 오류를 해결해 주세요</h4>
        <ul>
            <li v-for="(error, idx) in errors" :key="idx">{{ error }}</li>
        </ul>
    </div>
      <div class="form-group">
        <label for="username">ID</label>
        <input
          v-model="credentials.username"
          type="text"
          class="form-control"
          id="username"
          placeholder="아이디를 입력해주세요"
        />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input
          v-model="credentials.password"
          type="password"
          class="form-control"
          id="password"
          placeholder="비밀번호를 입력해주세요"
        />
      </div>
      <button class="btn btn-primary">로그인</button>
    </form>
  </div>
</template>

<script>
import router from '../router'; // '../router/index.js' 의 줄임
const axios = require('axios');

export default {
  name: "LoginForm",
  data() {
    return {
      // 1. id/password 에 해당하는 data
      credentials: {
        username: '',
        password: '',
      },
      isAuthenticated: false, // 인증여부
      isLoading: false,
      errors: []
    };
  },
  methods: {
    login() {
        this.isLoading = true;

        if (this.checkUserInput()) {
            console.log('django 서버로 데이터를 보냅니다.');
            axios.post('http://localhost:8000/api-token-auth/', this.credentials)
                .then(res => {
                  this.isLoading = false;
                  console.log(res.data.token);
                  this.$session.start(); // sessionStorage.session-id: sess: + Date.now()
                  this.$session.set('jwt', res.data.token);
                  
                  // dispatch => action 실행하는 메서드 (어느 컴포넌트에 있든지 간에 auth에 있는 login 함수를 실행)
                  this.$store.dispatch('login', res.data.token);

                  router.push('/');
                })
                .catch(err => {
                  if (!err.response) { // no response >> 서버 꺼졌을 때
                    this.errors.push('Network Error...')
                  } else if (err.response.status === 400) {
                    this.errors.push('Invalid username or password');
                  } else if (err.response.status === 500) {
                    this.errors.push('Internal Server error. Please try again later.');
                  } else {
                    this.errors.push('Some error occured');
                  }
                  this.isLoading = false;
                });
        } else {
            console.log('검증 실패. 다시 작성하세요!')
            this.isLoading = false;
        }        
    },
    checkUserInput() {
        this.errors = [];
        if (!this.credentials.username) this.errors.push("username을 입력하세요.") // js는 {}내 1줄이면 이렇게 줄일 수 있다.
        if (this.credentials.password.length < 8) this.errors.push("password는 8글자 이상입니다.")
        if (!this.errors.length) return true;    
    },
  }
};
</script>

<style>
</style>