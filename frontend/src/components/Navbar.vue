<template>
  <div class="navbar py-2">
    <div :class="wrapperClass">
      <div class="brand px-2">
        <slot name="brand"></slot>
      </div>
      <div class="end px-2">
        <slot name="end"></slot>
      </div>
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

  .navbar {
    background-color: color('dark');
    color: color('light');
    top: 0;
    width: 100%;
    font-size: 1.0rem;

    & > div {
      display: flex;
      justify-content: space-between;
    }

    .brand, .end {
      white-space: nowrap;
    }
  }
</style>
