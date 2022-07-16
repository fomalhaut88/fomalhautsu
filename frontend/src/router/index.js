import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../viewsnew/Home.vue'
import About from '../views/About.vue'
import Blog from '../viewsnew/Blog.vue'
import Article from '../views/Article.vue'
import Projects from '../views/Projects.vue'
import Files from '../views/Files.vue'
import Contacts from '../views/Contacts.vue'
import CV from '../views/CV.vue'
import PageNotFound from '../views/PageNotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/blog',
    name: 'Blog',
    component: Blog,
  },
  {
    path: '/blog/:id/:url',
    name: 'Article',
    component: Article,
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects,
  },
  {
    path: '/files',
    name: 'Files',
    component: Files,
  },
  {
    path: '/files/:name',
    name: 'FilesName',
    component: Files,
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: Contacts,
  },
  {
    path: '/cv',
    name: 'CV',
    component: CV,
  },
  {
    path: '*',
    name: 'PageNotFound',
    component: PageNotFound,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
