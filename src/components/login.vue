<template>
  <q-layout>
  <div class="register-page">
    <div class="window-height window-width row justify-center items-center">
      <div class="col-md-5 left window-height items-center justify-center desktop-only tab-only">
        <div class="row window-height items-center justify-center">
          <q-card flat class="bigger">
            <img src="../assets/Myntra-Logo.jpg" class="logo">
            <h3>Enjoy The benefits <br> of the exclusive <br> network with <br>Myntra</h3>
          </q-card>
        </div>
      </div>
      <div class="col-md-7 right window-height items-center justify-center">
        <div class="row window-height items-center justify-center">
          <q-card flat class="bigger">
            <div class="mobile-only" align="center">
              <img src="../assets/Myntra-Logo.jpg" class="logo" style="height: 80px;width: 200px;">
            </div>
            <q-card-title>
              <h2>Login into Myntra.</h2>
            </q-card-title>
            <q-card-main>
              <q-field>
                <p class="caption">User Id</p>
                <q-input class="input-field" v-on:keyup="ezoIdEvent()" v-model="userId"/>
                <div v-if="exoIdErrorMsg" style="font-size: small; color: #EB0019">
                  Please Enter the Mobile Number.
                </div>
              </q-field>
              <q-field>
                <p class="caption">Enter OTP</p>
                <q-input class="input-field" v-on:keyup="pwdEvent()" v-model="otp" type="password" />
                <div v-if="otpErrorMsg" style="font-size: small; color: #EB0019">
                  Please Enter One Time Password.
                </div>
              </q-field>
              <q-field>
                <q-checkbox v-model="staySignIn" color="primary" label="Stay signed in" />
                <!-- <label class="getOtp" @click="getOtp()">Get OTP</label> -->
              </q-field>
              <q-btn color="primary" @click="login()" class="btn">
                  <q-spinner-hourglass v-if="btnLoading" class="on-left" />
                  LOG IN
              </q-btn>
              <!-- <q-btn color="primary" @click="logout()" class="btn">LOGOUT</q-btn> -->
            </q-card-main>
          </q-card>
        </div>
      </div>
    </div>
  </div>
  </q-layout>
</template>

<script type="text/javascript" src="https://www.baqend.com/js-sdk/latest/baqend-realtime.js"></script>
<script>
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
      otp: '',
      btnLoading: false,
      userDetails: '',
      staySignIn: true,
      exoIdErrorMsg: false,
      otpErrorMsg: false,
      LDBbind: {}
    }
  },
  created () {
    this.checkLoginStatus()
  },
  methods: {
    login: function () {
      var that = this
      that.btnLoading = true
      if (this.validationForLogin()) {
        DB.User.login(this.userId, this.otp).then(function () {
          var role = DB.User.me.user_role
          that.$router.push('/app/createStn')
        }, function(err) {
          that.btnLoading = false
          that.$q.notify({
            color: 'black',
            textColor: 'white',
            message: "User name or password is incorrect.",
            position: 'bottom-left',
            timeout: 3000
          })
        })
      } else {
        that.btnLoading = false
      }
    },
    ezoIdEvent () {
      if (this.ezoId !== '') {
        this.exoIdErrorMsg = false
      }
      if(event.key == "Enter") {
        this.login()
      }
    },
    pwdEvent () {
      if (this.otp !== '') {
        this.otpErrorMsg = false
      }
      if(event.key == "Enter") {
        this.login()
      }
    },
    validationForLogin () {
      if (this.userId === '') {
        this.exoIdErrorMsg = true
        return false
      } else {
        this.exoIdErrorMsg = false
      }
      if (this.otp === '') {
        this.otpErrorMsg = true
        return false
      } else {
        this.otpErrorMsg = false
      }
      return true
    },
    checkLoginStatus () {
      var that = this
      if (navigator.onLine) { // if user on online
        DB.ready(function() {
          if (DB.User.me) {
            that.$router.push('/app/createStn')
          } else {
            console.log('Hello Anonymous')
          }
        })
      } else {
        that.$q.notify({
          color: 'white',
          textColor: 'black',
          message: "You are in offline.",
          position: 'bottom-left',
          timeout: 3000
        })
      }
    }
  }
}
</script>

<style>
</style>
