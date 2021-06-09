import Vue from 'vue'
// import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import App from './App.vue'
import store from './store'
import router from './router'

// 캐로젤 삽질..
import VueGlide from 'vue-glide-js'
import 'vue-glide-js/dist/vue-glide.css'

// // Import Bootstrap an BootstrapVue CSS files (order is important)
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'

// // Make BootstrapVue available throughout your project
// Vue.use(BootstrapVue)
// // Optionally install the BootstrapVue icon components plugin
// Vue.use(IconsPlugin)
Vue.config.productionTip = false

// 카카오 로그인
// window.Kakao.init('35b881741ab48f0dfc83b0a540e11adf');

// 메인 페이지 캐로우젤
Vue.use(VueGlide)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')

