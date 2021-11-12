<template>
  <div class="blog px-2">
    <h2 class="text-center"><Icon type="blog" /> Blog</h2>

    <div class="tags" v-if="tags">
      <div v-for="tag in tags"
           :key="tag.id"
           :class="{active: tag.isActive}"
           @click="tagClick(tag)"
           class="px-1 mr-1 mb-1">
        {{ tag.name }}
      </div>
    </div>

    <div class="articles py-3" v-if="articles">
      <div v-for="(article, idx) in getShownArticles()" :key="article.id"
           class="mb-3"
           :class="{'padding-right': (idx + 1) % 2, 'padding-left': idx % 2}">

        <div class="div-img py-1">
          <img :src="article.image_url" v-if="article.image_url">
          <img src="../assets/article-default.png" v-else>
        </div>

        <div class="div-about py-1">
          <h2 class="display-inline">
            <router-link :to="getArticleURL(article)">
              {{ article.title }}
            </router-link>
          </h2>
          <div class="date text-muted">{{ article.date }}</div>
          <p>
            {{ shortText(article) }}...
            <router-link :to="getArticleURL(article)" class="text-nowrap">
              read more
            </router-link>
          </p>
        </div>

      </div>
    </div>

    <div class="text-center" v-else>
      <Spinner size="lg" />
    </div>
  </div>
</template>

<script>
  import cyrillicToTranslit from 'cyrillic-to-translit-js'
  import { haveIntersection, removeUpmathSpecs, toCebabCase } from '@/utils'

  export default {
    data() {
      return {
        articles: null,
        tags: null,
      }
    },
    methods: {
      tagClick(tag) {
        tag.isActive = !tag.isActive
        this.$forceUpdate()
      },
      shortText(article) {
        return removeUpmathSpecs(article.preview_text)
      },
      isShown(article) {
        const activeTags = this.getActiveTags()
        return !activeTags.length || haveIntersection(activeTags, article.tags)
      },
      getArticleURL(article) {
        const urlTransliteratied = cyrillicToTranslit().transform(article.title)
        const urlTitle = toCebabCase(urlTransliteratied)
        return `/blog/${article.id}/${urlTitle}`
      },
      getActiveTags() {
        if (this.tags) {
          return this.tags.filter(tag => tag.isActive).map(tag => tag.id)
        } else {
          return []
        }
      },
      getShownArticles() {
        return this.articles.filter(article => this.isShown(article))
      },
    },
    mounted() {
      this.$api.blogArticles.get().then(response => {
        this.articles = response.body
      })
      this.$api.blogTags.get().then(response => {
        this.tags = response.body
      })
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .blog {
    .tags {
      & > div {
        display: inline-block;
        cursor: pointer;
        user-select: none;
        -webkit-tap-highlight-color:rgba(0, 0, 0, 0);
        border: 2px solid color('link');
        border-radius: 5px;
        color: color('dark');
        font-weight: bold;
        transition: 0.25s;

        &:hover {
          border-color: color('primary');
        }

        &.active {
          color: color('light');
          background-color: color('link');

          &:hover {
            background-color: color('primary');
          }
        }
      }
    }

    .articles {
      & > div {
        border-bottom: 2px solid color('grey');

        &.padding-left {
          @media (min-width: $media-min-width) {
            padding-left: 7%;
          }
        }

        &.padding-right {
          @media (min-width: $media-min-width) {
            padding-right: 7%;
          }
        }

        @media (min-width: $media-min-width) {
          display: flex;
        }

        .div-img {
          @media (min-width: $media-min-width) {
            width: 20%;
          }

          img {
            width: 100%;
            height: 100%;
            object-fit: cover;
          }
        }

        .div-about {
          @media (min-width: $media-min-width) {
            padding-left: 1rem;
            width: 80%;
          }

          .date {
            font-size: 0.875rem;
          }
        }
      }
    }
  }
</style>
