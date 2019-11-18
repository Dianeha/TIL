import Vue from 'vue'
import App from './App.vue'
import router from './router'
// './router/index.js'와 같음. 자동으로 index인 이름의 파일을 가져온다.

Vue.config.productionTip = false

new Vue({
  router, // 'router': router의 줄임. router/index.js 에서 계약하고 나서의 본격적인 일 시작.
  render: h => h(App)
}).$mount('#app')
