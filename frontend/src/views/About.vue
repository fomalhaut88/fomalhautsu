<template>
  <div class="about px-2">
    <h2 class="text-center"><Icon type="info-circle" /> About</h2>

    <img alt="Alexander Khlebushchev" src="../assets/me.jpg" class="pr-2">

    <p>
      Welcome to my personal website, dear visitor. My name is Alexander Khlebushchev.
    </p>

    <p>
      I developed this site to have my own virtual space to publish my thoughts, programming snippets, cribs, files and a lot other stuff, so it is a kind of workshop where I am not limited in the way to present what I want.
      I appreciate your feedback to make this source better for visitors, so do not hesitate to message me with your comments and suggestions (see <router-link to="/contacts">Contacts</router-link>).
      Maybe I will add the opportunity to leave comments for articles in my blog or something else, though according to the past experience visitors rarely post something...
      Also I duplicate some content on other platforms like Github and Medium.
    </p>

    <p>
      This website helps me to be more responsible in front of my projects, to finalize them carefully. And sometimes writing articles is like "the rubber duck" method that makes me understand the topic better.
    </p>

    <p>
      Here you will find nothing about my personality, because I am deeply convinced that only what the person does matters, neither who he is nor what happened in his life.
      So I do not share the pictures of me and my life, I do not discuss about politics and religion, I do not tell about situations in my everyday life. My private life is not public.
    </p>

    <p>
      As far as I am Russian by nationality some content is in Russian.
      But I have not implemented the localization on the website because it is almost useless and consuming to support.
      If you find I am wrong in it, please, tell me, I will not ignore it.
    </p>
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
