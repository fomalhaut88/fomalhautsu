<template>
  <div class="navbar">
    <div class="container">
      <div class="burger">
        <a href="#" @click="$root.$emit('menu-show')">
          <Icon type="bars" />
        </a>
      </div>

      <div>
        <router-link to="/"><img alt="Logo" src="@/assets/logo.svg" height="60" width="60"></router-link>
      </div>

      <div>
        <div class="languages">
          <a href="#">EN</a>
          <a href="#">RU</a>
          <a href="#">EO</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {}
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .navbar {
    background-color: color('bg-primary');
    color: color('light');
    top: 0;
    width: 100%;
    font-size: 1.0rem;

    & > div {
      display: flex;
      justify-content: space-between;
      white-space: nowrap;

      a {
        color: color('light');
      }
    }

    .burger {
      padding: 16px 0;
      font-size: 32px;
    }

    .languages {
      display: flex;
      justify-content: space-between;
      padding: 16px 0;

      & > a {
        display: block;
        border: 1px solid color('light');
        padding: 0.125rem 0.5rem;
        margin-left: 1rem;
        font-size: 12px;
        font-weight: 600;
        font-style: normal;
      }
    }
  }

  /*.navbar {
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
  }*/
</style>
