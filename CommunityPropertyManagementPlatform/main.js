import Vue from 'vue'
import App from './App'

import store from './store'  
Vue.prototype.$store = store  

Vue.config.productionTip = false

App.mpType = 'app'

import cuCustom from './colorui/components/cu-custom.vue'
Vue.component('cu-custom',cuCustom)

const baseUrl = "http://yb0125.natapp1.cc";

Vue.prototype.global_baseUrl = baseUrl

const app = new Vue({
    ...App
})
app.$mount()
