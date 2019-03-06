<template>
  <div class="HEADER">
    <q-layout-header>
      <q-toolbar
        color="primary"
        :glossy="$q.theme === 'mat'"
        :inverted="$q.theme === 'ios'"
      >
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
          style="background: rgba(16,32,51,0.871) !important"
        >
          <q-icon name="menu" />
        </q-btn>

        <div class="row window-width">
          <div class="col-lg-8 col-md-6 col-sm-6 col-xs-6">
            <q-toolbar-title>
              <img src="statics/myntralogo.png" style="width:120px;">
            </q-toolbar-title>
          </div>
          <div class="col-lg-4 col-md-6 col-sm-6 col-xs-6" align="right">
            <div class="center-aligned q-pt-xs">
              <div style="display: inline-block;">
                <span class="desktop-only tab-only">{{userName}}</span>
                <q-popover
                  :anchor="anchor"
                  :self="self"
                >
                  <q-list link style="min-width: 150px">
                    <q-item
                      v-close-overlay
                    >
                      <q-item-main @click.native="logout('logout')" label="Logout" />
                    </q-item>
                  </q-list>
                </q-popover>
              </div>
            </div>
          </div>
        </div>
      </q-toolbar>
    </q-layout-header>

    <q-layout-drawer
      v-model="leftDrawerOpen"
      :content-class="$q.theme === 'mat' ? 'bg-grey-2' : null"
    >

      <q-list-header></q-list-header>

      <q-list
        no-border
        link
        inset-delimiter
      >
        <router-link class="navlink" :to="{ path: '/admin/createCartons'}">
          <q-item class="navlink">
            <img src="statics/team.png" class="link-img">
            <div class="q-pl-lg navigation-text">Create Carton</div>
          </q-item>
        </router-link>

        <router-link class="navlink" :to="{ path: '/admin/primarySort'}">
          <q-item class="navlink">
            <img src="statics/news.png" class="link-img">
            <div class="q-pl-lg navigation-text">Primary Sort</div>
          </q-item>
        </router-link>

        <router-link class="navlink" :to="{ path: '/admin/secondarySort'}">
          <q-item class="navlink">
            <img src="statics/quiz.png" class="link-img">
            <div class="q-pl-lg navigation-text">Secondary Sort</div>
          </q-item>
        </router-link>
        <router-link class="navlink" :to="{ path: '/admin/uploads'}">
         <q-item class="navlink">
           <img src="statics/group.png" class="link-img">
           <div class="q-pl-lg navigation-text">Uploads</div>
         </q-item>
       </router-link>

       <router-link class="navlink" :to="{ path: '/admin/putAway'}">
         <q-item class="navlink">
           <img src="statics/group.png" class="link-img">
           <div class="q-pl-lg navigation-text">Putaway</div>
         </q-item>
       </router-link>

       <router-link class="navlink" :to="{ path: '/admin/picking'}">
         <q-item class="navlink">
           <img src="statics/group.png" class="link-img">
           <div class="q-pl-lg navigation-text">Picking</div>
         </q-item>
       </router-link>

        <a href="javascript:void(0)" @click="logout('logout')">
          <q-item class="navlink">
            <img src="statics/logout.png" class="link-img">
            <div class="q-pl-lg navigation-text">Logout</div>
          </q-item>
        </a>

      </q-list>
    </q-layout-drawer>
  </div>
</template>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-database.js"></script>
<script>
import {
  QCollapsible
} from 'quasar'
export default {
  name: 'AppHeader',
  data () {
    return {
      // leftDrawerOpen: this.$q.platform.is.desktop
      leftDrawerOpen: true,
      userMobileNo: '',
      companyName: '',
      emailId: '',
      image: '',
      popover: false,
      userName: '',
      anchorOrigin: {vertical: 'bottom', horizontal: 'left'},
      selfOrigin: {vertical: 'top', horizontal: 'left'}
    }
  },
  computed: {
    anchor () {
      return `${this.anchorOrigin.vertical} ${this.anchorOrigin.horizontal}`
    },
    self () {
      return `${this.selfOrigin.vertical} ${this.selfOrigin.horizontal}`
    }
  },
  created () {
    var that = this
    firebase.auth().onAuthStateChanged(function(user) {
      if (user) {
        that.userMobileNo = user.phoneNumber
        firebase.database().ref('userDetails').orderByChild('mobileNo').equalTo(that.userMobileNo).on("child_added", function(data) {
          that.userName = data.val().firstName + ' ' + data.val().lastName
          that.image = "https://firebasestorage.googleapis.com/v0/b/doctorseventmanagement-908e5.appspot.com/o/All_Image_Uploads%2F1534838928356-germ.png?alt=media&token=5af4a9e7-c359-4417-bb44-cee3281bf6e4"
        })
      } else {
        that.$router.push('/')
      }
    })
  },
  methods: {
    changeState (uri) {
      this.$router.push(uri)
    },
    logout (pageName) {
      var that = this
      if (pageName === 'logout') {
        firebase.auth().signOut().then(function() {
          that.$router.push('/')
        }).catch(function(error) {
        })
      } else {
        that.collapseNav()
        this.$router.push(pageName)
      }
    },
    getUsersData () {
      var that = this
      firebase.database().ref('UserDetails').orderByChild('userid/uid').once('value', function(snapshot) {
        snapshot.forEach(function(childSnapshot) {
          if (childSnapshot.val().phone_no === that.userMobileNo) {
            that.companyName = childSnapshot.val().company_name
            that.emailId = childSnapshot.val().email_address
            that.image = childSnapshot.val().company_logo
          }
        })
      })
    }
  }
}
</script>

<style>
</style>
