<template>
  <div class="AppHeader layout-header">
    <router-link class="navlink" :to="{ path: '/app/createStn' }" >CREATE STN</router-link>
    <router-link class="navlink" :to="{ path: '/app/receivedStn' }" >RECEIVE STN</router-link>
  </div>
</template>
<script>
import {
  QToolbar,
  QToolbarTitle,
  QLayout
} from 'quasar'

export default {
  components: {
    QToolbar,
    QToolbarTitle,
    QLayout
  },
  data () {
    return {
      name: 'AppHeader',
      headerWelcomeName: ''
    }
  }
}
</script>

<style>
</style>
