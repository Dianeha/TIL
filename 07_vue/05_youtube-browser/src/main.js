import Vue from 'vue';
import App from './App';

new Vue({
    render: h => h(App), // render는 화면에 보여줌
}).$mount('#app') // 마운트. 부착