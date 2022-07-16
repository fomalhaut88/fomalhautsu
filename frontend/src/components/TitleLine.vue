<template>
  <div class="title-line">
    <div class="container">
      <div class="path-line">
        <div v-if="path">
          <span v-for="(item, idx) in path" :key="idx">
            /
            <a href="/" :class="(idx != path.length - 1) ? 'muted' : ''">{{ item }}</a>
          </span>
        </div>
      </div>
      <div class="title py-4">
        <span>{{ title }}</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      title: String,
      path: Array,
    },
    computed: {
      pathLine() {
        return this.path ? this.path.join(" / ") : ""
      },
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .title-line {
    background-color: color("bg-primary");

    .path-line {
      font-family: 'Halvar Breit Rg';
      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      text-transform: capitalize;
      border-bottom: 1px solid color("muted");
      color: color("muted");

      a.muted {
        color: color("muted");
      }
    }

    .title > span {
      text-transform: uppercase;
      padding-bottom: 0.25rem;
      border-bottom: 5px solid color("secondary");
      font-size: 48px;
      font-family: 'Halvar Breit Rg';
      font-style: normal;
      font-weight: 500;
    }
  }
</style>
