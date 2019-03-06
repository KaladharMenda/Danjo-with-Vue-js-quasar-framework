<template>
  <q-layout view="lHh Lpr lFf">
    <q-layout-header style="left: 0px;">
      <q-toolbar
        style="height: 57px;"
        color="primary"
        :inverted="$q.theme === 'ios'"
        class="backgroung_color"
      >
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
        >
          <q-icon name="menu" />
        </q-btn>

        <q-toolbar-title>
          <img src="statics/logo1.png" class="img_logo">
        </q-toolbar-title>
        <span class="textFont2"><b>{{$store.state.example.userName}}</b></span>
      </q-toolbar>
    </q-layout-header>

    <q-layout-drawer
      class ="backgroung_color"
      v-model="leftDrawerOpen"
      :content-class="$q.theme === 'mat' ? 'backgroung_color' : null"
    >
      <q-list
        no-border
        link
        inset-delimiter
      >
        <q-list-header>Essential Links</q-list-header>
        <q-item class="navlink" :to="{ path: '/admin/Usermanagement'}">
           <img src="statics/user.png" class="link-img">
           <div class="q-pl-lg navigation-text header_font header_text">User Management</div>
         </q-item>
        <q-item v-if="$store.state.example.userType != 'Admin'" class="navlink" :to="{ path: '/admin/studentreccords'}">
           <img src="statics/primary.png" class="link-img">
           <div class="q-pl-lg navigation-text header_font header_text">Student Data</div>
        </q-item>
        <q-item class="navlink" :to="{ path: '/admin/sessionexams'}">
           <img src="statics/primary.png" class="link-img">
           <div class="q-pl-lg navigation-text header_font header_text">Session Exams</div>
         </q-item>
         <q-item v-if="$store.state.example.userType != 'Admin'" class="navlink" :to="{ path: '/admin/Encode'}">
           <img src="statics/primary.png" class="link-img">
           <div class="q-pl-lg navigation-text header_font header_text">Encode</div>
         </q-item>
         <q-item v-if="$store.state.example.userType != 'Admin'" class="navlink" :to="{ path: '/admin/Decode'}">
           <img src="statics/primary.png" class="link-img">
           <div class="q-pl-lg navigation-text header_font header_text">Decode</div>
         </q-item>
         <q-item class="navlink" :to="{ path: '/admin/settings'}">
           <img src="statics/settings.png" class="link-img">
           <div class="q-pl-lg navigation-text header_font header_text">Settings</div>
         </q-item>
          <q-item class="navlink" @click.native="logout('logout')">
            <a href="#">
              <img src="statics/logout.png" class="link-img">
              <div class="q-pl-lg navigation-text header_font header_text" style="display: inline;">Logout</div>
            </a>
          </q-item>
        </q-list>
    </q-layout-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<script src="https://www.gstatic.com/firebasejs/5.2.0/firebase.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-database.js"></script>

<script>
export default {
  name: 'MyLayout',
  data () {
    return {
      leftDrawerOpen: this.$q.platform.is.desktop,
      userDetails: '',
      wareHouseId: ''
    }
  },
  mounted () {
    // var that = this
  },
  created () {
    let that = this
    firebase.auth().onAuthStateChanged(function(user) {
      if (!user) {
        that.$router.push('/')
      }
    })
   },
  methods: {
    logout (pageName) {
      var that = this
      console.log(pageName)
      if (pageName === 'logout') {
        firebase.auth().signOut().then(function() {
          that.$router.push('/')
          that.$store.dispatch('example/fetchAdminKey', false)
          localStorage.removeItem('usertype')
          localStorage.removeItem('username')
        }).catch(function(error) {
          console.log(error)
        })
      } else {
        that.collapseNav()
        this.$router.push(pageName)
      }
    }
  }
}
</script>

<style>
</style>
