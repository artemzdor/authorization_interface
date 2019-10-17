import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import Router from '@/router'

Vue.use(Vuex)

let responseLgin = (response) => {
  if (response.data.status === 200) {
    document.cookie = `session=${response.data.session}; max-age=${response.data.tm / 1000}`
    Router.push('lk')
  } else {
    alert('Что-то пошло не так', err)
  }
}

export default new Vuex.Store({
  state: {
    getGlobalLocation: window.location.origin
  },
  mutations: {

  },
  actions: {
    login (context, dataForSend) {
      console.log(window.location.origin)
      return axios({
        method: 'POST',
        url: `${this.state.getGlobalLocation}/api/login`,
        data: dataForSend
      })
      .then(ress => {
        responseLgin(ress)
      })
      .catch(err => {
        alert('Логин не удался', err)
      })
    },
    registration (context, dataForSend) {
      console.log(window.location.origin)
      return axios({
        method: 'POST',
        url: `${this.state.getGlobalLocation}/api/registration`,
        data: dataForSend
      })
      .then(ress => {
        responseLgin(ress)
      })
      .catch(err => {
        alert('Логин не удался', err)
      })
    },
    changePassword (context, dataForSend) {
      return axios({
        method: 'POST',
        url: `${this.state.getGlobalLocation}/api/changepassword`,
        data: dataForSend
      })
    },
    logOut (context, dataForSend) {
      return axios({
        method: 'POST',
        url: `${this.state.getGlobalLocation}/api/logout`,
        data: dataForSend
      })
    }
  }
})
