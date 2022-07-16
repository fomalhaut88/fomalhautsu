<template>
  <div id="app">
    <Navbar />
    <Menu ref="menu" />
    <router-view />
    <Footer />
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
    mounted() {
      this.$root.$on('menu-show', () => {
        this.$refs['menu'].show()
      })
    },
  }
</script>
