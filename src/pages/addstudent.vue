<template>
  <div class="About">
    <q-card class="bg-white card-styl">
    <form>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolbackground">
          <q-toolbar-title>
            <b>Add Student Personal Details</b>
          </q-toolbar-title>
        </q-toolbar>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="padding-top: 10px;" align="center" >
        <q-chip color="grey-4" text-color="black">PERSONAL DETAILS</q-chip>
      </div>
      <div class="row gutter-sm q-mb-md">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" :readonly="readonly" ref="pin" v-model="studen_info.pin" float-label="PIN *"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.student_name" float-label="NAME *"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="studen_info.gender"
              :options="genderOptions"
              float-label="Gender *"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-datetime color="orange" v-model="studen_info.date_of_birth" type="date" float-label="Date Of Birth *"/>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="studen_info.relation_ship"
              :options="relationOptions"
              float-label="Relation Ship "
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.relative_name" float-label="Relative Name"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="studen_info.caste"
              :options="casteOptions"
              float-label="caste"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="studen_info.qualification"
              :options="qualificationOptions"
              float-label="Qualification"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-datetime color="orange" v-model="studen_info.joining_date" type="date" float-label="Joining Date "/>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="studen_info.ph"
              :options="phOptions"
              float-label="Is PH ?"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.mole_one" float-label="Mole One "/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.mole_two" float-label="Mole Two "/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.tenth_passed_year" float-label="10th Class Passed Year "/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.tenth_hallticket" float-label="10th Class Hall TocketNo "/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="studen_info.scheme_code"
              :options="schemeOptions"
              float-label="Scheme Code"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="studen_info.year_sem"
              :options="year_semOptions"
              float-label="Year / Semester"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="studen_info.shift"
              :options="shiftOptions"
              float-label="Shift"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="studen_info.section"
              :options="sectionOptions"
              float-label="Section"
            />
          </q-field>
        </div>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" style="padding-top: 10px;" align="center" >
        <q-chip color="grey-4" text-color="black">COMMUNICATION DETAILS</q-chip>
      </div>
      <div class="row gutter-sm q-mb-md">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.door_num" float-label="Door No"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.street_name" float-label="Street Name"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.city" float-label="City / Village"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.pincode" float-label="Pin Code"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.district" float-label="District"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.mandal" float-label="Mandal"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.phone_number" float-label="Mobile No"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="studen_info.email" float-label="Email"/>
          </q-field>
        </div>
      </div>
      <div class="row gutter-sm q-mb-md">
        <div class="col-lg-4 col-md-4 col-sm-2 col-xs-1"></div>
        <div class="col-lg-2 col-md-2 col-sm-4 col-xs-5">
          <q-btn color="amber" class="full-width toolbackground" label="CANCEL" @click="emtpyAllFields"/>
        </div>
        <div class="col-lg-2 col-md-2 col-sm-4 col-xs-5">
          <q-btn class="full-width toolgreen" text-color= "white" label="SUBMIT" @click="changeMessage"/>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-2 col-xs-1">
        </div>
      </div>
    </form>
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
  QInnerLoading
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
    QInnerLoading
  },
  data () {
    return {
      studen_info:{
        pin: '',
        student_name:'',
        ph: '',
        gender:'',
        date_of_birth: '',
        relation_ship: '',
        relative_name: '',
        caste: '',
        qualification: '',
        joining_date: '',
        mole_one: '',
        mole_two: '',
        tenth_passed_year: '',
        tenth_hallticket: '',
        scheme_code: '',
        year_sem: '',
        shift: '',
        section: '',
        door_num: '',
        street_name: '',
        city: '',
        pincode: '',
        district: '',
        mandal: '',
        phone_number: '',
        email: '',
        adding:true,
      },
      readonly: false,
      genderOptions: [{'label': 'Male', 'value': 'Male'},{'label': 'Female', 'value': 'Female'}],
      relationOptions: [{'label': 'Father', 'value': 'Father'},{'label': 'Mother', 'value': 'Mother'}],
      casteOptions: [{'label': 'OC', 'value': 'OC'},{'label': 'BC', 'value': 'BC'},{'label': 'SC', 'value': 'SC'},{'label': 'ST', 'value': 'ST'},{'label': 'OTHERS', 'value': 'OTHERS'}],
      qualificationOptions: [{'label': '10th Class', 'value': '10thClass'},{'label': 'Intermediate', 'value': 'Intermediate'},{'label': 'Inter(vocational)', 'value': 'Inter(vocational)'},{'label': 'Degree', 'value': 'Degree'},{'label': 'OTHERS', 'value': 'OTHERS'}],
      phOptions: [{'label': 'Yes', 'value': 'Yes'},{'label': 'No', 'value': 'No'}],
      schemeOptions: [{'label': 'ER91', 'value': 'ER91'},{'label': 'C14', 'value': 'C14'},{'label': 'C16', 'value': 'C16'}],
      year_semOptions: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'}],
      shiftOptions: [{'label': '1', 'value': '1'},{'label': '2', 'value': '2'}],
      sectionOptions: [{'label': '1', 'value': '1'},{'label': '2', 'value': '2'}],
    }
  },
  mounted () {
    let that = this
  },
  created () {
    var that = this
    setTimeout(function () {
      that.$refs.pin.focus()
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
      axios.post(baseUrlForBackend+'govweb/student_details/', JSON.stringify(this.studen_info));
      // setTimeout(() => {
      //   this.show({
      //     spinner: QSpinnerGears,
      //     spinnerColor: 'amber',
      //     message: 'Processing ....'
      //   })
      // }, 0)
    },
    getVendorLimit () {
      var that = this
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
      that.student_name = ''
      that.ph = '',
      that.gender = '',
      that.date_of_birth = '',
      that.relation_ship = '',
      that.relative_name = '',
      that.caste = '',
      that.qualification = '',
      that.joining_date = '',
      that.mole_one = '',
      that.mole_two = '',
      that.tenth_passed_year = '',
      that.tenth_hallticket = '',
      that.scheme_code = '',
      that.year_sem = '',
      that.shift = '',
      that.section = '',
      that.door_num = '',
      that.street_name = '',
      that.city = '',
      that.pincode = '',
      that.district = '',
      that.mandal = '',
      that.phone_number = '',
      that.email = '',
      that.adding = true
    }
  }
}
</script>
<style>
</style>
