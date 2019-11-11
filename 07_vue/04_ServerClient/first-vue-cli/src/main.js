import Vue from 'vue';
import App from './App.vue'; // .vue 는 안써도 알아서 동작함

new Vue({
    // el: '#app',
    // method(함수 in 객체) 정의할 때, () => {} 금지이지만, 유일하게 여기서만 쓴다.
    render: h => h(App),
}).$mount('#app') // .$mount('#app') === el: '#app' 같은 역할. 주로 전자를 쓴다.