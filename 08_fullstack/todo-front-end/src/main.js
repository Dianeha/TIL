import Vue from 'vue'
import App from './App.vue'

import router from './router' // './router/index.js'와 같음. 자동으로 index인 이름의 파일을 가져온다.
import store from './store' // from './store/index.js'

import VueSession from 'vue-session' // 발급받은(지금은 Django로부터) Token을 SessionStorage에 저장하는 것을 도와줌.

Vue.config.productionTip = false;
Vue.use(VueSession); // Vue 에게 VueSession 이라는 Middleware 등록

new Vue({
  router, // 'router': router의 줄임. router/index.js 에서 계약하고 나서의 본격적인 일 시작.
  store,  // store/index.js 에서 계약하고 나서, 본격적인 일 여기서 시작.
  render: h => h(App)
}).$mount('#app')
