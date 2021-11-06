export default class Api {
  constructor(resource) {
    this.images = resource('images{/id}')
    this.files = resource('files{/id}')
    this.blogTags = resource('blog-tags{/id}')
    this.blogArticles = resource('blog-articles{/id}')
    this.projects = resource('projects{/id}')
    this.contacts = resource('contacts{/id}')
  }
}
