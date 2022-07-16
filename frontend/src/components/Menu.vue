<template>
  <div class="menu" @click.self="hide()" :class="{hidden: !isShown, active: isActive}">
    <div class="menu-container" :class="{active: isActive}">
      <div class="p-2">
        <div class="px-5 py-3">
          <span class="title">MENU</span>
        </div>
        <div>&nbsp;</div>
        <div v-for="item in items" :key="item.title" class="menu-item py-2 px-5">
          <router-link :to="item.link" @click.native="hide()">
            {{ item.title }}
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        isShown: false,
        isActive: false,
        items: [
          {
            title: 'Projects',
            link: '/projects',
            icon: 'code',
          },
          {
            title: 'Blog',
            link: '/blog',
            icon: 'blog',
          },
          {
            title: 'Files',
            link: '/files',
            icon: 'copy',
          },
          {
            title: 'About',
            link: '/about',
            icon: 'info-circle',
          },
          {
            title: 'Contacts',
            link: '/contacts',
            icon: 'users',
          },
        ],
      }
    },
    methods: {
      show() {
        this.isShown = true
        setTimeout(() => {
          this.isActive = true
        }, 0)
      },

      hide() {
        this.isActive = false
        setTimeout(() => {
          this.isShown = false
        }, 250)
      },

      toggle() {
        if (this.isShown) {
          this.hide()
        }
        else {
          this.show()
        }
      },
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .menu {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    transition: 0.25s;

    &.active {
      background-color: rgb(0, 0, 0, 0.85);
    }

    .menu-container {
      background-color: color("bg-secondary");
      display: inline-block;
      position: absolute;
      left: -100%;
      height: 100%;
      transition: 0.25s;

      &.active {
        left: 0;
      }

      .menu-item a {
        text-decoration: none;
        /*text-transform: uppercase;*/
        user-select: none;
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        color: color('light');
        font-family: 'Halvar Breit Rg';
        font-style: normal;
        font-weight: 300;
        font-size: 32px;

        &:hover {
          color: color('primary');
        }
      }

      .title {
        color: color("light");
        font-family: 'Halvar Breit Rg';
        font-style: normal;
        font-weight: 500;
        font-size: 48px;
        padding-bottom: 0.25rem;
        border-bottom: 5px solid color("secondary");
      }
    }
  }
</style>
