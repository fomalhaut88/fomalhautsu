<template>
  <div class="cv px-2">
    <h2 class="text-center">CV</h2>
    <object :data="'/media/files/CV.pdf?secret=' + $route.query.secret" type="application/pdf"></object>
  </div>
</template>

<style lang="scss" scoped>
  .cv {
    & > object {
      display: table;
      margin: 0 auto;

      width: 700px;
      max-width: 100%;
      height: 960px;
      max-height: 80%;

      border: 1px solid #bbb;
    }
  }
</style>
