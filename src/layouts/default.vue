<template>
  <q-layout view="lHh Lpr lFf" class="layout-padding">
    <app-header></app-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-database.js"></script>
<script>
import AppHeader from '../pages/appHeader.vue'

export default {
  name: 'LayoutDefault',
  components: {
    AppHeader
  },
  data () {
    return {}
  },
  created () {
    var that = this
    firebase.auth().onAuthStateChanged(function(user) {
      if (user) {
        console.log("User logged in successfully")
      } else {
        that.$router.push('../../')
      }
    })
  },
  methods: {

  }
}
</script>

<style>
</style>
