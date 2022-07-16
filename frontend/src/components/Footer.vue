<template>
  <div class="footer py-2">
    &copy; Alexander Khlebushchev 2015 - {{ getYear() }}
  </div>
</template>

<script>
  export default {
    methods: {
      getYear() {
        return new Date().getFullYear()
      },
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .footer {
    background-color: color('bg-primary');
    color: color('muted');
    position: absolute;
    bottom: 0;
    width: 100%;
    text-align: center;
    margin: 0;

    font-family: 'Halvar Breit Rg';
    font-style: normal;
    font-weight: 400;
    font-size: 1rem;
  }
</style>
