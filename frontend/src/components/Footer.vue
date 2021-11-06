<template>
  <div class="footer py-2">
    <div :class="wrapperClass">
      <slot></slot>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      wrapperClass: {
        type: String,
        default: "",
      },
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .footer {
    background-color: color('dark');
    color: color('light');
    position: absolute;
    bottom: 0;
    width: 100%;
    text-align: center;
    margin: 0;
  }
</style>
