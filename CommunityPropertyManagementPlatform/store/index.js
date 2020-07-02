import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)


const store = new Vuex.Store({  
    state: {  
        globalLogin: false, 
        token: null,  
        globalUserInfo: {},  
    },  
    mutations: {  
        login(state, provider) {  
            // console.log(state)  
            // console.log(provider) 
        },  
        logout(state) {  
             
        },
		setToken(state, provider) {
			state.token = provider;
		},
		setGlobalUserInfo(state, provider) {
			state.globalUserInfo = provider;
		},
    }  
})

export default store