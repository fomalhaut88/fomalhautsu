<template>
  <Icon type="spinner" :fixed-width="true" :spin="true" :size="size" />
</template>

<script>
  export default {
    props: {
      size: String,
    }
  }
</script>
