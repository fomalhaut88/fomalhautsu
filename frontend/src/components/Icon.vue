<template>
  <span :class="getClass()"></span>
</template>

<script>
  export default {
    props: {
      type: String,
      size: String,
      fixedWidth: {
        type: Boolean,
        default: false,
      },
      spin: {
        type: Boolean,
        default: false,
      },
      pref: {
        type: String,
        default: 'fa',
      },
      fullType: String,
    },
    methods: {
      getClass() {
        const result = []

        if (this.fullType) {
          const arr = this.fullType.split(' ')
          result.push(arr[0])
          result.push(arr[1])
        }
        else {
          result.push(this.pref)
          result.push(`fa-${this.type}`)
        }

        if (this.size) {
          result.push(`fa-${this.size}`)
        }
        if (this.fixedWidth) {
          result.push('fa-fw')
        }
        if (this.spin) {
          result.push('fa-spin')
        }

        return result
      },
    },
  }
</script>
