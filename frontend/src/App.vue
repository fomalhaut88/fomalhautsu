<template>
  <div id="app">
    <Navbar wrapper-class="container">
      <template #brand>
        <router-link to="/">
          <div class="brand">
            <div class="logo"><img alt="Logo" src="./assets/logo.svg" height="32" width="32"></div>
            <div class="title px-1">Alexander Khlebushchev</div>
          </div>
        </router-link>
      </template>
      <template #end>
        <a href="#" class="end px-2" @click="$refs.menu.show()">
          <Icon type="bars" />
        </a>
      </template>
    </Navbar>

    <Menu ref="menu" />

    <div class="router-view"
         :class="{container: $router.currentRoute.name != 'Home'}">
      <router-view />
    </div>

    <Footer wrapper-class="container">
      &copy; Alexander Khlebushchev 2015 - {{ getYear() }}
    </Footer>
  </div>
</template>

<script>
  import Navbar from '@/components/Navbar.vue'
  import Footer from '@/components/Footer.vue'
  import Menu from '@/components/Menu.vue'

  export default {
    components: {
      Navbar,
      Footer,
      Menu,
    },
    methods: {
      getYear() {
        return new Date().getFullYear()
      },

      updateBodyClass() {
        if (this.$router.currentRoute.name == 'Home') {
          document.body.className = 'home'
        } else {
          document.body.className = ''
        }
      },
    },
    watch:{
      $route () {
        this.updateBodyClass()
      }
    },
    created() {
      this.updateBodyClass()
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  #app {
    .navbar {
      a {
        user-select: none;
        -webkit-tap-highlight-color:rgba(0, 0, 0, 0);
      }

      .brand {
        .logo {
          display: inline-block;
          height: 32px;
          float: left;
        }

        .title {
          display: inline-block;
          height: 32px;
          line-height: 32px;
          float: clear;
          color: color('light');
          text-transform: uppercase;
          transition: 0.25s;

          &:hover {
            color: color('primary');
          }
        }
      }

      .end {
        color: color('light');
        line-height: 32px;

        &:hover {
          color: color('primary');
        }
      }
    }
  }
</style>
