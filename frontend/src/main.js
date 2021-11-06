import Vue from 'vue'
import VueResource from 'vue-resource'
import MarkdownIt from 'markdown-it'
import hljs from 'highlight.js'

import 'highlight.js/styles/github.css'
import './assets/scss/main.scss'

Vue.use(VueResource)

import App from './App.vue'
import router from './router'
import Api from './api'

Vue.config.productionTip = false
Vue.http.options.root = process.env.VUE_APP_API_ROOT

import Icon from './components/Icon.vue'
import Spinner from './components/Spinner.vue'
import Modal from './components/Modal.vue'

Vue.component('Icon', Icon)
Vue.component('Spinner', Spinner)
Vue.component('Modal', Modal)

new Vue({
  router,
  render: h => h(App),
  beforeCreate() {
    Vue.prototype.$md = new MarkdownIt(
      {
        html: true,
        highlight: function (str, lang) {
          if (lang && hljs.getLanguage(lang)) {
            try {
              return hljs.highlight(str, {language: lang}).value
            } catch (__) {/**/}
          }
          return ""
        },
      }
    )

    Vue.prototype.$api = new Api(this.$resource)
  }
}).$mount('#app')
