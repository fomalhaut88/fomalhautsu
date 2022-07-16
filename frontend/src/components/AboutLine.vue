<template>
  <div class="about-line">
    <div class="container">
      <div class="half pt-5">
        <div class="div-title">ALEXANDER KHLEBUSHCHEV</div>
        <div class="div-secondary py-2">Personal website</div>
        <div class="div-buttons py-4">
          <a href="/" class="primary">PROJECTS</a>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <a href="/" class="default">BLOG</a>
        </div>
        <div class="div-quote">
          <p class="quote">There are two paths. The first one is familiar and convenient. But the other makes you alive.</p>
          <p class="author">&#8212; Me</p>
        </div>
      </div>
      <div class="half">
        <img src="@/assets/alexander-khlebushchev.png">
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  @import '@/assets/scss/base';

  .about-line {
    background-color: color("bg-primary");

    & > div {
      display: flex;
      justify-content: space-between;

      .half {
        width: 40%;

        & > img {
          width: 100%;
          display: block;
          margin: 0 auto;
        }

        .div-title {
          font-family: 'Halvar Breit Rg';
          font-style: normal;
          font-weight: 700;
          font-size: 48px;
          line-height: 58px;
          padding-bottom: 0.25rem;
          border-bottom: 5px solid color("secondary");
        }

        .div-secondary {
          font-family: 'Halvar Breit Rg';
          font-style: normal;
          font-weight: 400;
          font-size: 24px;
          color: color("muted");
        }

        .div-buttons {
          & > a {
            display: inline-block;
            width: 200px;
            text-align: center;
            color: color("light");
            font-family: 'Halvar Breit Rg';
            font-style: normal;
            font-weight: 500;
            font-size: 14px;
            line-height: 60px;

            &.primary {
              background-color: color("link");
              border: 2px solid color("link");
            }

            &.default {
              border: 2px solid color("light");
            }
          }
        }

        .div-quote {
          color: #B2B3B6;

          font-family: 'Manrope';
          font-style: normal;

          & > .quote {
            font-size: 20px;
            font-weight: 600;
          }

          & > .author {
            font-size: 14px;
            font-weight: 400;
            text-align: right;
          }
        }
      }
    }
  }
</style>
