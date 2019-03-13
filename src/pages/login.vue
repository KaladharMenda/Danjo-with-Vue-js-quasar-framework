<template>
 <q-layout>
   <div class="register-page regist_s">
     <div class="window-height window-width row justify-center items-center">
       <div class="col-md-12 right window-height items-center justify-center">
         <div class="row window-height items-center justify-center">
           <q-card flat class="bigger qcard_s" style = "padding-top: 65px;">
             <q-card-title>
              <div class="row" align="center">
                <img class = 'justify-center' srcset="statics/logo.jpg 3x" alt="…" style="width: 100%;height: 100%;">
              </div>
             </q-card-title>
             <q-card-main v-if="sendOtpDiv">
               <q-field>
                 <p class="caption cap_s">Enter UserId</p>
                 <q-input class="input-field mobile_s" type="text" onfocus="this.value=''; this.style.color='#fff'" v-on:keyup="ezoIdEvent()" ref="userId" v-model="userId"/>
                 <div v-if="exoIdErrorMsg" class="mobile_is">
                   Please enter the valid userName.
                 </div>
               </q-field>
               <q-field>
                 <p class="caption cap_s">Enter password</p>
                 <q-input class="input-field mobile_s" type="password" onfocus="this.value=''; this.style.color='#fff'" v-on:keyup="pwdEvent()" v-model="pwd"/>
                 <div v-if="otpErrorMsg" class="mobile_is">
                   Please enter the valid password.
                 </div>
               </q-field>
               <div class="div_s"></div>
               <q-btn color="green" class="full-width otp_send" :disabled="btnLoading" @click="submitOtp()">
                 <q-spinner-hourglass v-if="btnLoading" class="on-left" />
                 <span class="otp_fs">SUBMIT</span>
               </q-btn>
             </q-card-main>
           </q-card>
         </div>
       </div>
     </div>
   </div>
 </q-layout>
</template>

<script src="https://www.gstatic.com/firebasejs/5.2.0/firebase.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-database.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-firestore.js"></script>
<script>
import axios from 'axios'
import { Notify } from 'quasar'

import {
  QSelect,
  QField,
  QBtn,
  QInput,
  QCard,
  QCardTitle,
  QCardMain,
  QCardActions,
  QLayout,
  QCheckbox,
  QSpinnerHourglass
} from 'quasar'

export default {
  components: {
    QSelect,
    QField,
    QBtn,
    QInput,
    QCard,
    QCardTitle,
    QCardMain,
    QCardActions,
    QLayout,
    QCheckbox,
    QSpinnerHourglass
  },
  data () {
    return {
      userId: '',
      pwd:'',
      otp: '',
      pathway: false,
      btnLoading: false,
      userDetails: '',
      staySignIn: true,
      exoIdErrorMsg: false,
      otpErrorMsg: false,
      submitOtpDiv: false,
      sendOtpDiv: true,
      LDBbind: {},
      country: '',
      verificationId: '',
      trailMobileNo: '',
      loggedUser: '',
      errorCode: '',
      totalGrpId: '',
      userIsActive: '',
      flag: true,
      url: '/admin/primarySort'
    }
  },
  methods: {
    submitOtp: function () {
      let that = this
      that.btnLoading = true
      if (that.pwd !== '' && that.userId !== '') {
        firebase.auth().signInAnonymously().then(suc =>{
          firebase.database().ref('UserDetails/' + that.userId).once('value', function(doc) {
            if (doc.val().is_active || doc.val().usertype == 'Admin') {
              if (doc.val() && that.userId == doc.val().name && that.pwd == doc.val().password) {
                localStorage.setItem('usertype', doc.val().usertype)
                localStorage.setItem('username', doc.val().name)
                if (doc.val().usertype == 'Admin') {
                  that.$router.push('/admin/Usermanagement')
                } else if (doc.val().usertype == 'G1') {
                  that.$router.push('/admin/Usermanagement')
                } else if (doc.val().usertype == 'G2') {
                  that.$router.push('/admin/Usermanagement')
                }
              } else {
                that.showNotify('Please enter your valid credentials')
                that.$refs.userId.focus()
                that.btnLoading = false
                that.$router.push('/')
                that.userId = ''
                that.pwd = ''
              }
            } else {
              that.showNotify('Your Account is InActive, Please contact to ADMIN !')
              that.$refs.userId.focus()
              that.btnLoading = false
              that.$router.push('/')
              that.userId = ''
              that.pwd = ''
            }
          })
        })
      } else {
        that.showNotify('Please enter your valid credentials')
        that.$refs.userId.focus()
        that.btnLoading = false
        that.$router.push('/')
        that.userId = ''
        that.pwd = ''
      }
    },
    ezoIdEvent () {
      var that = this
      if (that.ezoId !== '') {
        that.exoIdErrorMsg = false
      }
      if(event.key == "Enter") {
        that.submitOtp()
      }
    },
    pwdEvent () {
      var that = this
      if (that.otp !== '') {
        that.otpErrorMsg = false
      }
      if(event.key == "Enter") {
        that.submitOtp()
      }
    },
    showNotify (msg) {
      let that = this
      that.$q.notify({
        color: 'black',
        textColor: 'white',
        message: msg,
        position: 'bottom-left',
        timeout: 1700
      })
    }
  }
}
</script>

<style>
</style>
