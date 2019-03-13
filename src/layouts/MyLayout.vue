<template>
  <q-layout view="lHh Lpr lFf">

    <!-- <q-layout-header style="left: 0px;">
      <q-toolbar
        style="height: 57px;"
        color="primary"
        :inverted="$q.theme === 'ios'"
        class="backgroung_color"
      > -->

        <!-- <q-toolbar-title>
          <img src="statics/logo1.png" class="img_logo">
        </q-toolbar-title>
        <span class="textFont2"><b>{{$store.state.example.userName}}</b></span>
      </q-toolbar>
    </q-layout-header> -->
    <q-layout-drawer
      class ="backgroung_color vertical-scrollbar-demo"
      v-model="leftDrawerOpen"
      :content-class="$q.theme === 'mat' ? 'backgroung_color' : null"
    >
      <q-list
        no-border
        link
        inset-delimiter
      >
        <q-list-header>Essential links</q-list-header>
        <q-item class="navlink" :to="{ path: '/admin/Usermanagement'}">
           <img src="statics/usermanagement.png" class="link-img">
           <div class="navigation-text header_fontM header_text">User Management</div>
        </q-item>
        <a href="javascript:void(0)">
          <q-collapsible class="box">
            <template slot="header">
              <img src="statics/student.png" class="link-img" />
              <div icon-right="send" class="navigation-text header_fontM header_text">Student Information</div>
            </template>
            <q-collapsible class="box">
              <template slot="header">
                <img src="statics/user.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">Student Details</div>
              </template>
              <q-item class="navlink childnav" :to="{ path: '/admin/addstudent'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Add Student Info</div>
              </q-item>
              <q-item class="navlink childnav" :to="{ path: '/admin/updatestudent'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Update Student Info</div>
              </q-item>
              <q-item class="navlink childnav" :to="{ path: '/admin/transferstudent'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Transfer Student</div>
              </q-item>
              <q-item class="navlink childnav" :to="{ path: '/admin/deletestudent'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Delete Student</div>
              </q-item>
            </q-collapsible>
            <!-- <END THE STUDENT INFO DETAILS > -->
            <q-collapsible class="box">
              <template slot="header">
                <img src="statics/attend.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">Attendence Details</div>
              </template>
              <q-item class="navlink childnav" :to="{ path: '/admin/addattendance'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Add Attendence</div>
              </q-item>
              <q-item class="navlink childnav" :to="{ path: '/admin/viewattendance'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">View Attendence</div>
              </q-item>
              <q-item class="navlink childnav" :to="{ path: '/admin/transferstudent'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Confirm Attendence</div>
              </q-item>
            </q-collapsible>
            </q-collapsible>
            <q-collapsible class="box">
              <template slot="header">
                <img src="statics/user.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">Reports</div>
              </template>
            <q-collapsible class="box">
              <template slot="header">
                <img src="statics/user.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">Student</div>
              </template>
              <q-item class="navlink childnav" :to="{ path: '/admin/DeletedStudentsReport'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Deleted Students</div>
              </q-item>
            </q-collapsible>
          </q-collapsible>
            <!-- <END THE STUDENT Attendance DETAILS > -->

        </a>
        <!-- <q-item v-if="$store.state.example.userType != 'Admin'" class="navlink" :to="{ path: '/admin/studentreccords'}">
           <img src="statics/primary.png" class="link-img">
           <div class="navigation-text header_fontM header_text">Student Data</div>
        </q-item>
        <q-item class="navlink" :to="{ path: '/admin/sessionexams'}">
           <img src="statics/primary.png" class="link-img">
           <div class="navigation-text header_fontM header_text">Session Exams</div>
         </q-item>
         <q-item v-if="$store.state.example.userType != 'Admin'" class="navlink" :to="{ path: '/admin/Encode'}">
           <img src="statics/primary.png" class="link-img">
           <div class="navigation-text header_fontM header_text">Encode</div>
         </q-item>
         <q-item v-if="$store.state.example.userType != 'Admin'" class="navlink" :to="{ path: '/admin/Decode'}">
           <img src="statics/primary.png" class="link-img">
           <div class="navigation-text header_fontM header_text">Decode</div>
         </q-item>
         <q-item class="navlink" :to="{ path: '/admin/settings'}">
           <img src="statics/settings.png" class="link-img">
           <div class="navigation-text header_fontM header_text">Settings</div>
         </q-item> -->
          <q-item class="navlink" @click.native="logout('logout')">
            <a href="#">
              <img src="statics/logout.png" class="link-img">
              <div class="navigation-text header_fontM header_text" style="display: inline;">Logout</div>
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
  body::-webkit-scrollbar {
    width: 1em;
}
body::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
}
body::-webkit-scrollbar-thumb {
  background-color: darkgrey;
  outline: 1px solid slategrey;
}
</style>
