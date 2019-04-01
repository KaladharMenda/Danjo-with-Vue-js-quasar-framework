<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolgradientlightgreen">
          <q-toolbar-title>
            <b>Encode For Semester Exams</b>
          </q-toolbar-title>
        </q-toolbar>
      </div>
      <div class="row gutter-sm q-mb-md toppadding">
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
          <q-field>
            <q-select
              v-model="semId"
              :options="semOptions"
              float-label="Semester *"
              @input="getSubjectsData"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" v-if="semId">
          <q-select
            v-model="subId"
            :options="subjectDropdownOpts"
            float-label="Subject *"
            @input="getUsersData"
          />
        </div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" v-if="subId">
          <q-select
            v-model="studentIDs"
            :options="semOptionss"
            float-label="Select Student *"
            filter
            @input="enableScanDiv"
          />
        </div>
      </div>
      <div class="row toppadding">
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12"></div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" v-if = "semId && subId && studentIDs">
          <q-field>
             <q-input type="text" id="scanFocus" ref="scannedItem" v-model="scannedItem" v-on:keyup.enter="checkBinType" float-label="Scan Sem Paper BarCode *"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12"></div>
      </div>
    </q-card>
  </div>
</template>

<script type="text/javascript" src="https://www.baqend.com/js-sdk/latest/baqend-realtime.js"></script>

<script>
import axios from 'axios'
import { Notify } from 'quasar'

import {
  date,
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
    date,
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
      semId: '',
      subId: '',
      scannedItemDecode: '',
      tempsessionvalue:'',
      studentMark: '',
      studentIDs: '',
      scannedItem: '',
      subjectMarks: '',
      subjectDropdownOpts: [],
      studentmarkdetails: [],
      semOptions: [{'label': 'I', 'value': 'I'},{'label': 'II', 'value': 'II'},{'label': 'III', 'value': 'III'},{'label': 'IV', 'value': 'IV'},{'label': 'V', 'value': 'V'},{'label': 'VI', 'value': 'VI'},{'label': 'VII', 'value': 'VII'}],
      semOptionss: [{'label': '14341a0598', 'value': '14341a0598'},{'label': '14341a0599', 'value': '14341a0599'},{'label': '14341a05100', 'value': '14341a05100'},{'label': '14341a05101', 'value': '14341a05101'}],
      tab: 'exam1'
    }
  },
  created () {
    var that = this
  },
  methods: {
    updatemarks () {
      var that = this
      if (that.subjectMarks) {
        that.emtpyAllFields('ss2')
        that.$q.notify({color: 'positive', textColor: 'white', message: 'Successfully Updated Subject Marks', position: 'center', timeout: 1000 })
        setTimeout(function(){
          that.$refs.scannedItemDecode.focus()
        }, 500)
      } else {
        that.$q.notify({color: 'negative', textColor: 'white', message: 'please Enter Subject Marks', position: 'center', timeout: 1000 })
        that.$refs.subjectMarks.focus()
      }
    },
    enableScanDiv () {
      var that = this
      setTimeout(function(){
        that.$refs.scannedItem.focus()
      }, 500)
    },
    checkBinType (e) {
      let that = this
      that.$q.notify({color: 'positive', textColor: 'white', message: 'Successfully Added Barcode Number', position: 'center', timeout: 1000 })
      that.emtpyAllFields('ss1')
    },
    getSubjectsData () {
      var that = this
      that.subjectDropdownOpts = []
      firebase.database().ref('subjects/'+ that.semId).once('value', function(snapshot) {
        snapshot.forEach(function (child) {
          // if (child.val().active === true) {
          that.subjectDropdownOpts.push({
            'label': child.key,
            'value': child.key,
          })
          // }
        })
      })
    },
    getUsersData () {
      var that = this
      that.loader = true
      if(that.semId != '' && that.subId != '') {
        that.studentmarkdetails =[]
        firebase.database().ref('StudentDetails').once('value', function(snapshot) {
          snapshot.forEach(function (child) {
            that.studentmarkdetails.push({
              'studentid':child.key,
            });
          })
          that.loader = false
        })
      } else {
        that.showNotify('please select SEMESTER & SUBJECT')
      }
    },
    emtpyAllFields (val) {
      var that = this
      that.sessionvalue = val
      that.userModalAdd = false
      that.semId = ''
      that.subId = ''
      that.scannedItemDecode = ''
      that.scannedItem = ''
      that.studentIDs = ''
      that.loader = false
      that.loading = false
      that.subjectMarks = ''
      that.enableEditDiv = false
      that.ediTablEnable = false
      that.subjectDropdownOpts = []
      that.studentmarkdetails = []
      that.tempsessionvalue = ''
      console.log(that.sessionvalue)
    },
    showNotify (msg) {
      let that = this
      that.$q.notify({
        color: 'green',
        textColor: 'white',
        message: msg,
        position: 'bottom-right',
        timeout: 1000
      })
    }
  }
}
</script>

<style>
</style>
