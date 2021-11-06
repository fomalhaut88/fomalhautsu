<template>
  <div class="modal" @click.self="hide()"
       :class="{hidden: !isShown, active: isActive}">
    <div class="modal-container" :class="getContainerClass()">
      <div class="modal-close pt-1 pr-2" v-if="closeButton">
        <a href="#" @click="hide()"><Icon type="times"/></a>
      </div>
      <slot></slot>
    </div>
  </div>
</template>

<script>
  export default {
    props: {
      closeButton: {
        type: Boolean,
        default: false,
      },
      wrapperClass: {
        type: String,
        default: "",
      },
    },
    data() {
      return {
        isShown: false,
        isActive: false,
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

      getContainerClass() {
        let result = this.wrapperClass
        if (this.isActive) {
          result += ' active'
        }
        return result
      },
    },
    mounted() {
      document.addEventListener("keydown", (e) => {
        if (e.keyCode == 27) {
          this.hide()
        }
    })
}
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .modal {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    transition: 0.25s;

    text-align: center;

    &.active {
      background-color: rgb(0, 0, 0, 0.875);
    }

    .modal-container {
      position: relative;
      background-color: white;
      display: inline-block;
      box-sizing: border-box;
      margin: 1rem;
      width: calc(100% - 2rem);
      opacity: 0.0;
      transition: 0.25s;
      transform: translateY(max(50vh - 50%, 0px));

      @media (min-width: $media-min-width) {
        width: 50%;
      }

      &.active {
        opacity: 1.0;
      }

      .modal-close {
        position: absolute;
        right: 0;

        a {
          color: color('dark');

          &:hover {
            color: color('primary');
          }
        }
      }
    }
  }
</style>
