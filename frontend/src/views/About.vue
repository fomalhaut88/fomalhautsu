<template>
  <div class="about px-2">
    <h2 class="text-center"><Icon type="info-circle" /> About</h2>

    <img alt="Alexander Khlebushchev" src="../assets/me.jpg" class="pr-2">

    <p>Dear visitor, welcome to my personal website. My name is Alexander Khlebushchev.</p>

    <p>I developed this website to have my own virtual space for publishing my thoughts, programming snippets, cribs, files and a lot of other stuff. Also I duplicate some content on other platforms like Github and Medium. Sometimes writing articles is like using "the rubber duck" method that makes me understand the topic better.</p>

    <p>I appreciate your feedback and try to reply to everyone, so do not hesitate to send me your comments and suggestions (see <router-link to="/contacts">Contacts</router-link>). Who knows, maybe you will be my partner in our future project.</p>
  </div>
</template>

<style lang="scss" scoped>
  .about {
    & > img {
      float: left;
      width: 300px;
      max-width: 50%;
    }
  }
</style>
