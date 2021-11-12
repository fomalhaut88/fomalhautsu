<template>
  <div id="article" class="article px-2 pt-1">
    <div v-if="article">
      <router-link to="/blog">Back to list of articles</router-link>
      <h2 class="text-center">{{ article.title }}</h2>
      <div class="text-muted text-center">{{ article.date }}</div>
      <div class="text" v-html="getText()"></div>
    </div>
    <div class="text-center py-2" v-else>
      <Spinner size="lg" />
    </div>
  </div>
</template>

<script>
  import { inlineUpmathToMathjax } from '@/utils'

  export default {
    data() {
      return {
        article: null,
      }
    },
    methods: {
      getText() {
        return inlineUpmathToMathjax(
          this.$md.render(this.article.text)
        )
      },
      updateMathjax() {
        this.$nextTick(
          () => {
            window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub])
          }
        )
      },
    },
    mounted() {
      this.$api.blogArticles.get({
        id: this.$route.params.id
      }).then(response => {
        this.article = response.body
        this.updateMathjax()
      })
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .article {
    .text {
      word-wrap: break-word;
      width: 100%;

      ::v-deep {
        img {
          display: block;
          margin: 0 auto;
          max-width: 100%;
        }

        table {
          margin: 0 auto;
          max-width: 100%;

          border: 2px solid color('grey');
          border-collapse: collapse;

          th {
            background-color: color('grey');
          }

          td, th {
            padding: 0.5rem;
            border: 2px solid color('grey');
            word-wrap: break-word;
            word-break: break-all;
            table-layout: fixed;
          }
        }

        pre {
          padding: 1rem;
          line-height: 1.5;
        }

        code {
          padding: 0.25rem;
        }

        pre, code {
          background-color: color('grey');
        }
      }
    }
  }
</style>
