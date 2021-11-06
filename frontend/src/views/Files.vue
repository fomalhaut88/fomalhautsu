<template>
  <div class="files px-2">
    <h2 class="text-center"><Icon type="copy" /> Files</h2>

    <table v-if="filesFiltered && filesFiltered.length">
      <tr>
        <th>File</th>
        <th>Size</th>
        <th>Direct URL</th>
        <th>Share</th>
      </tr>
      <tr v-for="file in filesFiltered" :key="file.id">
        <td>
          <a :href="getDirectURL(file.url)" download>
            <Icon type="download" :fixed-width="true" />
          </a>
          {{ getName(file.url) }}
        </td>
        <td>{{ getPrettySize(file.size) }}</td>
        <td>
          <a :href="getDirectURL(file.url)" download>
            {{ getDirectURL(file.url) }}
          </a>
        </td>
        <td class="text-center">
          <a href="#" @click="clickShare(file)">
            <Icon type="copy" :fixed-width="true" />
          </a>
        </td>
      </tr>
    </table>

    <div class="text-center" v-if="!filesFiltered">
      <Spinner size="lg" />
    </div>

    <Modal ref="shareModal" wrapper-class="px-3 pb-1" :close-button="true">
      <div class="py-2">
        {{ shareMessage }}
      </div>
    </Modal>
  </div>
</template>

<script>
  import prettyBytes from 'pretty-bytes'

  export default {
    data() {
      return {
        files: null,
        shareMessage: "",
      }
    },
    computed: {
      filesFiltered() {
        if (this.files) {
          if (this.$route.params.name) {
            return this.files.filter(file => {
              return this.getName(file.url) == this.$route.params.name
            })
          } else {
            return this.files
          }
        } else {
          return null
        }
      },
    },
    methods: {
      getName(url) {
        const parts = url.split('/')
        return parts[parts.length - 1]
      },

      getDirectURL(url) {
        // return 'http://localhost:8000' + url
        return url
      },

      getPrettySize(size) {
        return prettyBytes(size)
      },

      clickShare(file) {
        const name = this.getName(file.url)
        this.shareMessage = `URL of the file '${name}' has been copied to the clipboard.`
        const fileURL = `${window.location.origin}/files/${name}`
        navigator.clipboard.writeText(fileURL).then(() => {
          this.$refs.shareModal.show()
        })
      },
    },
    mounted() {
      this.$api.files.get({
        secret: this.$route.query.secret
      }).then(response => {
        this.files = response.body
      })
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .files {
    font-size: 1.125rem;

    & > table {
      display: table;
      margin: 0 auto;
      max-width: 100%;

      border: 2px solid color('grey');
      border-collapse: collapse;

      td, th {
        padding: 1rem;
        border: 2px solid color('grey');
        word-wrap: break-word;
        word-break: break-all;
        table-layout: fixed;
      }
    }
  }
</style>
