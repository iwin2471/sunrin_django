const Two = { template: '<p>home page</p>' }
const t = { template: '<p>3 page</p>' }
const four = { template: '<p>four page</p>' }

const routes = {
  '/google/2': Two,
  '/google/3': t,
  '/google/4': four,
}

new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname
  },
  computed: {
    ViewComponent () {
      return routes[this.currentRoute] || NotFound
    }
  },
  render (h) { return h(this.ViewComponent) }
})
