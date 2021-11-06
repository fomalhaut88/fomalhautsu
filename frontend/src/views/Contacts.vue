<template>
  <div class="contacts">
    <h2 class="text-center"><Icon type="users" /> Contacts</h2>

    <div class="px-2">
      <p>
        You can find, follow and contact me by any of the sources below:
      </p>

      <div v-if="contacts">
        <div v-for="contact in contacts" :key="contact.id" class="py-1">
          <a :href="contact.url" target="blank">
            <Icon :full-type="contact.icon" :fixed-width="true" />
            {{ contact.name }}: {{ contact.value }}
          </a>
        </div>
      </div>

      <div v-else class="text-center">
        <Spinner size="lg" />
      </div>
    </div>
  </div>
</template>


<script>
  export default {
    data() {
      return {
        contacts: null,
      }
    },
    mounted() {
      this.$api.contacts.get().then(response => {
        this.contacts = response.body
      })
    },
  }
</script>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .contacts {
    font-size: 1.125rem;

    & > div {
      display: table;
      margin: 0 auto;
    }
  }
</style>
