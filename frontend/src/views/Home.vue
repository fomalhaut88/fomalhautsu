<template>
  <div class="home">
    <div class="container">
      <div class="div-img">
        <img src="../assets/home.png">
      </div>

      <div class="div-about">
        My name is Alexander.<br>
        <br>
        Welcome to my personal website.<br>
        <br>
        I am a mathematician and a software developer.<br>
        <br>
        Here you will find my<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;blog, projects, software, files, etc.<br>
        <br>
        I would be happy if<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;some of them may be interesting and useful in your life.<br>
        <br>
        Good luck!
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .home {
    & > div {
      @media (min-width: $media-min-width) {
        display: flex;
      }

      .div-img {
        width: 100%;

        @media (min-width: $media-min-width) {
          width: 50%;
        }

        img {
          display: inline-block;
          width: 100%;
        }
      }

      .div-about {
        width: 100%;
        color: color('light');
        text-align: center;
        font-size: 1.25rem;
        font-style: italic;
        font-family: Georgia, serif;
        line-height: 1.5;
        text-align: left;
        box-sizing: border-box;
        padding: 1rem;

        @media (min-width: $media-min-width) {
          width: 50%;
          padding-top: 8rem;
          padding-left: 4rem;
        }
      }
    }
  }
</style>
