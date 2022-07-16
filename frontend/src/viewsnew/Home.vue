<template>
  <div>
    <!-- <TitleLine title="Home" :path="['home', 'about']" /> -->
    <AboutLine />
    <div class="container">
      Some text
    </div>
  </div>
</template>

<script>
  import AboutLine from '@/components/AboutLine.vue'

  export default {
    components: {
      AboutLine,
    },
  }
</script>
