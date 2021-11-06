<template>
  <div class="projects px-2">
    <h2 class="text-center"><Icon type="code" /> Projects</h2>

    <div v-if="projects">
      <div v-for="(project, idx) in projects" :key="project.id" class="pb-3">

        <div class="div-img" :style="{order: idx % 2 + 1}">
          <img :src="project.image_url">
        </div>

        <div class="div-about" :style="{order: (idx + 1) % 2 + 1}">
          <div class="px-2">
            <h3 class="display-inline">{{ project.title }}</h3>
            <p>{{ project.description }}</p>
            <table>
              <tr>
                <td>
                  <router-link :to="getArticleURL(project)" v-if="project.article">
                    <Icon type="book" />
                    Article
                  </router-link>
                </td>
                <td>
                  <a :href="project.source" target="blank" v-if="project.source">
                    <Icon type="code" />
                    Source
                  </a>
                </td>
                <td>
                  <a :href="project.website" target="blank" v-if="project.website">
                    <Icon type="globe" />
                    Website
                  </a>
                </td>
                <td>
                  <a href="#" v-if="project.downloads.length" @click="downloadsClick(project)">
                    <Icon type="download" />
                    Downloads
                  </a>
                </td>
              </tr>
            </table>
          </div>
        </div>

      </div>
    </div>

    <div class="text-center" v-else>
      <Spinner size="lg" />
    </div>

    <Modal ref="downloadsModal" wrapper-class="px-2 pb-2" :close-button="true">
      <div class="downloads-modal" v-if="currentProject">
        <h3>{{ currentProject.title }}</h3>

        <div v-if="currentFiles">
          <div v-if="currentFiles.length">
            <div v-for="file in currentFiles" :key="file.id">
              <a :href="file.url" download>
                <Icon type="download" :fixed-width="true" />
                {{ getDownloadName(file) }}
              </a>
            </div>
          </div>
          <div v-else>
            No allowed files to display.
          </div>
        </div>

        <div class="text-center" v-else>
          <Spinner size="lg" />
        </div>
      </div>
    </Modal>
  </div>
</template>

<script>
  import prettyBytes from 'pretty-bytes'
  import { toCebabCase } from '@/utils'

  export default {
    data() {
      return {
        projects: null,
        currentProject: null,
        currentFiles: null,
      }
    },
    methods: {
      downloadsClick(project) {
        this.currentProject = project
        this.requestDownloadFiles(project.downloads, () => {
          this.$refs.downloadsModal.show()
        })
      },

      getArticleURL(project) {
        return `/blog/${project.article}/${toCebabCase(project.title)}`
      },

      requestDownloadFiles(fileIdArray, callback) {
        // Collect promises to request files through API
        const promises = fileIdArray.map(fileId => {
          return new Promise((resolve, reject) => {
            this.$api.files.get({id: fileId}).then(response => {
              resolve(response.body)
            }).catch(response => {
              reject(response)
            })
          })
        })

        // Request file objects
        Promise.all(promises).then(files => {
          this.currentFiles = files
          callback()
        }).catch(() => {
          this.currentFiles = []
          callback()
        })
      },

      getDownloadName(file) {
        const parts = file.url.split('/')
        const name = parts[parts.length - 1]
        const sizeStr = prettyBytes(file.size)
        return `${name} (${sizeStr})`
      },
    },
    mounted() {
      this.$api.projects.get().then(response => {
        this.projects = response.body
      })
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .projects {
    & > div {
      & > div {
        @media (min-width: $media-min-width) {
          display: flex;
        }

        .div-img {
          @media (min-width: $media-min-width) {
            width: 30%;
          }

          img {
            width: 100%;
          }
        }

        .div-about {
          @media (min-width: $media-min-width) {
            width: 70%;
          }

          table {
            font-size: 1.125rem;
            width: 100%;
            text-align: center;
          }
        }
      }
    }

    .downloads-modal {
      font-size: 1.125rem;
      line-height: 2;
    }
  }
</style>
