<template>
  <div class="menu" @click.self="hide()" :class="{hidden: !isShown, active: isActive}">
    <div class="menu-container" :class="{active: isActive}">
      <div class="p-2">
        <div v-for="item in items" :key="item.title" class="menu-item py-2 pl-2 pr-5">
          <router-link :to="item.link" @click.native="hide()">
            <Icon :type="item.icon" :fixed-width="true" />
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
            title: 'Blog',
            link: '/blog',
            icon: 'blog',
          },
          {
            title: 'Projects',
            link: '/projects',
            icon: 'code',
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
      background-color: rgb(0, 0, 0, 0.875);
    }

    .menu-container {
      background-color: white;
      display: inline-block;
      position: absolute;
      right: -100%;
      height: 100%;
      transition: 0.25s;

      &.active {
        right: 0;
      }

      .menu-item a {
        font-size: 1.0rem;
        text-decoration: none;
        text-transform: uppercase;
        user-select: none;
        -webkit-tap-highlight-color:rgba(0, 0, 0, 0);
        color: color('dark');

        &:hover {
          color: color('primary');
        }
      }
    }
  }
</style>
