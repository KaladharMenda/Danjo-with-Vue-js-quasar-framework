<template>
  <q-layout view="lHh Lpr lFf">

    <q-layout-header style="left: 0px;">
      <q-toolbar
        style="height: 57px;"
        color="primary"
        :inverted="$q.theme === 'ios'"
        class="backgroung_colors top-headderr"
      >
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
          style="background: #03d003;"
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
      class ="backgroung_color vertical-scrollbar-demo"
      v-model="leftDrawerOpen"
      :content-class="$q.theme === 'mat' ? 'backgroung_color' : null"
    >
      <q-list
        no-border
        link
        inset-delimiter
      >
        <q-list-header>{{user}}</q-list-header>
        <!-- <q-item class="navlink" :to="{ path: '/admin/Usermanagement'}">
           <img src="statics/usermanagement.png" class="link-img">
           <div class="navigation-text header_fontM header_text">User Management</div>
        </q-item> -->
        <q-item class="navlink" :to="{ path: '/admin/encodedecode'}" v-if="flagShow == 'true'">
           <img src="statics/usermanagement.png" class="link-img">
           <div class="navigation-text header_fontM header_text">Masters</div>
        </q-item>
        <a href="javascript:void(0)">
          <q-collapsible class="box" v-if="flagShow == 'true'">
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
              <!-- <q-item class="navlink childnav" :to="{ path: '/admin/transferstudent'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Transfer Student</div>
              </q-item> -->
              <q-item class="navlink childnav" :to="{ path: '/admin/deletestudent'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Delete Student</div>
              </q-item>
            </q-collapsible>
            <!-- <END THE STUDENT INFO DETAILS > -->
            <q-collapsible class="box">
              <template slot="header">
                <img src="statics/checklist.png" class="link-img" />
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
            </q-collapsible>
            <!-- <END THE STUDENT Attendance DETAILS > -->
            <q-collapsible class="box">
              <template slot="header">
                <img src="statics/attend.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">Unit Marks</div>
              </template>
              <q-item class="navlink childnav" :to="{ path: '/admin/addunitmarks'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Add Unit Marks</div>
              </q-item>
              <q-item class="navlink childnav" :to="{ path: '/admin/viewunitmarks'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">View Unit Marks</div>
              </q-item>
            </q-collapsible>
            <!-- <END THE UNIT MARKS > -->
            <q-collapsible class="box">
              <template slot="header">
                <img src="statics/attend.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">SM Marks</div>
              </template>
              <q-item class="navlink childnav" :to="{ path: '/admin/viewsmmarks'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">View SM Marks</div>
              </q-item>
            </q-collapsible>
            <!-- <END THE SM MARKS > -->
            <q-collapsible class="box">
              <template slot="header">
                <img src="statics/attend.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">PM Marks</div>
              </template>
              <q-item class="navlink childnav" :to="{ path: '/admin/addpmmarks'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Add PM Marks</div>
              </q-item>
              <q-item class="navlink childnav" :to="{ path: '/admin/viewpmmarks'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">View PM Marks</div>
              </q-item>
            </q-collapsible>
            <!-- <q-item class="navlink childnav" :to="{ path: '/admin/Encode'}">
              <img src="statics/qr-code.png" class="link-imgs">
              <div class="navigation-text header_fontS header_text">Encode</div>
            </q-item>
            <q-item class="navlink childnav" :to="{ path: '/admin/Decode'}">
              <img src="statics/qr-code.png" class="link-imgs">
              <div class="navigation-text header_fontS header_text">Decode</div>
            </q-item> -->
            </q-collapsible>
            <q-item class="navlink childnav" :to="{ path: '/admin/Encode'}" v-if="flagShow == 'false' || flagShow == 'true'">
              <img src="statics/qr-code.png" class="link-imgs">
              <div class="navigation-text header_fontM header_text">Encode</div>
            </q-item>
            <q-item class="navlink childnav" :to="{ path: '/admin/Decode'}" v-if="flagShow == 'true'">
              <img src="statics/qr-code.png" class="link-imgs">
              <div class="navigation-text header_fontM header_text">Decode</div>
            </q-item>
        </a>
        <a href="javascript:void(0)">
            <q-collapsible class="box" v-if="flagShow == 'true'">
              <template slot="header">
                <img src="statics/reports.png" class="link-img" />
                <div class="navigation-text header_fontM header_text">Reports</div>
              </template>
              <!-- <template slot="header">
                <img src="statics/studentsub.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">Student</div>
              </template> -->
              <q-item class="navlink childnav" :to="{ path: '/admin/DeletedStudentsReport'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Deleted Students</div>
              </q-item>
              <q-item class="navlink childnav" :to="{ path: '/admin/detainedlist'}">
                <img src="statics/delete.png" class="link-imgs">
                <div class="navigation-text header_fontS header_text">Detained List</div>
              </q-item>
              <q-item class="navlink childnav" :to="{ path: '/admin/condonationlist'}">
                <img src="statics/link.png" class="link-imgs">
                <div class="navigation-text header_fontS header_text">Condonation List</div>
              </q-item>
            <!-- <q-collapsible class="box">
              <template slot="header">
                <img src="statics/attend.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">Sm Marks</div>
              </template>
              <q-item class="navlink childnav" :to="{ path: '/admin/smmarksreport'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Confirmed Report</div>
              </q-item>
            </q-collapsible>
            <q-collapsible class="box">
              <template slot="header">
                <img src="statics/attend.png" class="link-img" />
                <div class="navigation-text header_fontS header_text">Pm Marks</div>
              </template>
              <q-item class="navlink childnav" :to="{ path: '/admin/pmmarksreport'}">
                <img src="statics/arrow.png" class="link-imgs">
                <div class="navigation-text header_fontC header_text">Confirmed Report</div>
              </q-item>
            </q-collapsible> -->
          </q-collapsible>
            <!-- <END THE STUDENT Attendance DETAILS > -->
        </a>
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
    that.user = localStorage.getItem('username')
    that.flagShow = localStorage.getItem('flagShow')
    console.log(that.flagShow)
    if (!that.user) {
      that.$router.push('/')
    }
    // firebase.auth().onAuthStateChanged(function(user) {
    // })
   },
  methods: {
    logout (pageName) {
      var that = this
      console.log(pageName)
      if (pageName === 'logout') {
        firebase.auth().signOut().then(function() {
          that.$router.push('/')
          // that.$store.dispatch('example/fetchAdminKey', false)
          // localStorage.removeItem('usertype')
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
