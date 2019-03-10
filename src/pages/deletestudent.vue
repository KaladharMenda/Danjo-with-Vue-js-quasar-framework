<template>
  <div class="About">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="left">
        <q-toolbar color="yellow" class="tooldanger" align="center">
          <q-toolbar-title>
            <b>Delete Student Details</b>
          </q-toolbar-title>
        </q-toolbar>
      </div>
      <div class="row" style="padding-top: 10px;" align="center" >
        <div class="col-lg-2 col-md-2 col-sm-1 col-xs-1"></div>
        <div class="col-lg-4 col-md-4 col-sm-5 col-xs-12" align="center">
          <q-field>
            <q-input type="text" ref="firstpin" v-model="firstpin" placeholder="PIN *" />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-5 col-xs-12" align="center">
          <q-btn color="red" @click="checkpinexists()" :disabled="btnLoading">
            <q-spinner-hourglass v-if="btnLoading" class="on-left" />
            Verify and Delete
          </q-btn>
        </div>
        <div class="col-lg-2 col-md-2 col-sm-1 col-xs-1"></div>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="padding-top: 10px;" align="center" v-if="alldivisionenable">
        <q-chip color="grey-4" text-color="black">PERSONAL DETAILS</q-chip>
      </div>
      <div class="row gutter-sm q-mb-md" v-if="alldivisionenable">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" :readonly="readonly" v-model="pin" float-label="PIN *"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="name" float-label="NAME *"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="gender"
              :options="genderOptions"
              float-label="Gender *"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-datetime color="orange" v-model="dateofbirth" type="date" float-label="Date Of Birth *"/>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="relationShip"
              :options="relationOptions"
              float-label="Relation Ship "
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="relativeName" float-label="Relative Name"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="category"
              :options="categoryOptions"
              float-label="Category"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="qualification"
              :options="qualificationOptions"
              float-label="Qualification"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-datetime color="orange" v-model="joiningDate" type="date" float-label="Joining Date "/>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="ph"
              :options="phOptions"
              float-label="Is PH ?"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="mole1" float-label="Mole One "/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="mole2" float-label="Mole Two "/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="tenpassyear" float-label="10th Class Passed Year "/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="tenhallticket" float-label="10th Class Hall TocketNo "/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="schemeCode"
              :options="schemeOptions"
              float-label="Scheme Code"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="yearsem"
              :options="yearsemOptions"
              float-label="Year / Semester"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="shift"
              :options="shiftOptions"
              float-label="Shift"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="section"
              :options="sectionOptions"
              float-label="Section"
            />
          </q-field>
        </div>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="padding-top: 10px;" align="center" v-if="alldivisionenable">
        <q-chip color="grey-4" text-color="black">COMMUNICATION DETAILS</q-chip>
      </div>
      <div class="row gutter-sm q-mb-md" v-if="alldivisionenable">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="doorno" float-label="Door No"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="streetname" float-label="Street Name"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="cityvillage" float-label="City / Village"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="pincode" float-label="Pin Code"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="district" float-label="District"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="mandal" float-label="Mandal"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="mobileno" float-label="Mobile No"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="Email" float-label="Email"/>
          </q-field>
        </div>
      </div>
      <div class="row gutter-sm q-mb-md" v-if="alldivisionenable">
        <div class="col-lg-4 col-md-4 col-sm-2 col-xs-1"></div>
        <div class="col-lg-4 col-md-4 col-sm-4 col-xs-4">
          <q-btn class="full-width toolgreen" text-color= "white" label="DELETE" @click="changeMessage"/>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-2 col-xs-1">
        </div>
      </div>
    </q-card>
  </div>
</template>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-database.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-firestore.js"></script>
<script>
import { QSpinnerFacebook, Loading, QSpinnerGears } from 'quasar'
import _ from 'lodash';
import axios from 'axios'
import {
  QTable,
  QTh,
  QTr,
  QTd,
  QTableColumns,
  QModal,
  QCard,
  QCardTitle,
  QSelect,
  QUploader,
  QSearch,
  QLayout,
  QModalLayout,
  QToggle,
  QInnerLoading,
  QSpinnerHourglass
} from 'quasar'

export default {
  components: {
    QTable,
    QTh,
    QTr,
    QTd,
    QTableColumns,
    QModal,
    QCard,
    QCardTitle,
    QSelect,
    QUploader,
    QSearch,
    QLayout,
    QModalLayout,
    QToggle,
    QInnerLoading,
    QSpinnerHourglass
  },
  data () {
    return {
      firstpin: '',
      pin: '',
      name:'',
      readonly: false,
      btnLoading: false,
      genderOptions: [{'label': 'Male', 'value': 'Male'},{'label': 'Female', 'value': 'Female'}],
      relationOptions: [{'label': 'Father', 'value': 'Father'},{'label': 'Mother', 'value': 'Mother'}],
      categoryOptions: [{'label': 'OC', 'value': 'OC'},{'label': 'BC', 'value': 'BC'},{'label': 'SC', 'value': 'SC'},{'label': 'ST', 'value': 'ST'},{'label': 'OTHERS', 'value': 'OTHERS'}],
      qualificationOptions: [{'label': '10th Class', 'value': '10thClass'},{'label': 'Intermediate', 'value': 'Intermediate'},{'label': 'Inter(vocational)', 'value': 'Inter(vocational)'},{'label': 'Degree', 'value': 'Degree'},{'label': 'OTHERS', 'value': 'OTHERS'}],
      phOptions: [{'label': 'Yes', 'value': 'Yes'},{'label': 'No', 'value': 'No'}],
      schemeOptions: [{'label': 'ER91', 'value': 'ER91'},{'label': 'C14', 'value': 'C14'},{'label': 'C16', 'value': 'C16'}],
      yearsemOptions: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'}],
      shiftOptions: [{'label': '1', 'value': '1'},{'label': '2', 'value': '2'}],
      sectionOptions: [{'label': '1', 'value': '1'},{'label': '2', 'value': '2'}],
      ph: '',
      gender:'',
      dateofbirth: '',
      relationShip: '',
      relativeName: '',
      category: '',
      qualification: '',
      joiningDate: '',
      mole1: '',
      mole2: '',
      tenpassyear: '',
      tenhallticket: '',
      schemeCode: '',
      yearsem: '',
      shift: '',
      section: '',
      doorno: '',
      streetname: '',
      cityvillage: '',
      pincode: '',
      district: '',
      mandal: '',
      mobileno: '',
      Email: '',
      alldivisionenable: ''
    }
  },
  mounted () {
    let that = this
  },
  created () {
    var that = this
    setTimeout(function () {
      that.$refs.firstpin.focus()
    },200)
  },
  methods: {
    show (options) {
      this.$q.loading.show(options)
      setTimeout(() => {
        this.$q.loading.hide()
      }, 3000)
    },
    changeMessage () {
      setTimeout(() => {
        this.show({
          spinner: QSpinnerGears,
          spinnerColor: 'amber',
          message: 'Processing ....'
        })
      }, 0)
    },
    checkpinexists () {
      let that = this
      that.btnLoading = true
      setTimeout(function () {
        that.btnLoading = false
      },2000)
      that.alldivisionenable = true
    },
    getVendorLimit () {
      var that = this
      alert('ok')
      if (that.$store.state.example.userName !== "") {
        window.app2.database().ref('WareHouseSettings/VendorLimit').on('value', function(vendors) {
          if (vendors.val()) {
            that.VendorLimit = vendors.val()
          }
          that.getAVendors()
        })
      } else {
        setTimeout(function(){
            that.getVendorLimit()
        },500)
      }
    },
    emtpyAllFields () {
      var that = this
      that.pin = ''
      that.name = ''
      that.ph = '',
      that.gender = '',
      that.dateofbirth = '',
      that.relationShip = '',
      that.relativeName = '',
      that.category = '',
      that.qualification = '',
      that.joiningDate = '',
      that.mole1 = '',
      that.mole2 = '',
      that.tenpassyear = '',
      that.tenhallticket = '',
      that.schemeCode = '',
      that.yearsem = '',
      that.shift = '',
      that.section = '',
      that.doorno = '',
      that.streetname = '',
      that.cityvillage = '',
      that.pincode = '',
      that.district = '',
      that.mandal = '',
      that.mobileno = '',
      that.Email = ''
    }
  }
}
</script>
<style>
</style>
