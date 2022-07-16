<template>
  <div>
    <TitleLine title="Blog" :path="['home', 'blog']" />
    <div class="container">
      Some text
    </div>
  </div>
</template>

<script>
  import TitleLine from '@/components/TitleLine.vue'

  export default {
    components: {
      TitleLine,
    },
  }
</script>
