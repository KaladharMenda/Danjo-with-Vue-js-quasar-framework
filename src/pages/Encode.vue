<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="row" align="center">
        <div class="col-lg-11 col-md-11 col-sm-11 col-xs-11" align="center">
          <q-toolbar color="orange" class="toolgradientlightgreen">
            <q-toolbar-title>
              <b>Encode For Semester Exams</b>
            </q-toolbar-title>
          </q-toolbar>
        </div>
        <div class="col-lg-1 col-md-1 col-sm-1 col-xs-1" align="center" style="background: linear-gradient(155deg, rgb(91, 216, 89), rgb(133, 255, 0)) !important">
          <q-btn flat round icon="refresh" @click="emtpyAllFields" style="float:right;"/>
        </div>
      </div>
      <div class="row gutter-sm q-mb-md toppadding">
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
          <q-field>
             <q-input type="text" id="scanFocus" ref="totalmarks" v-model="totalmarks"  float-label="Enter Total Marks *"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" v-if="totalmarks">
          <q-field>
            <q-select
              v-model="semId"
              :options="semOptions"
              float-label="Semester *"
              @input="getSubjects_scheme_Data"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" v-if="semId">
          <q-field>
            <q-select
              v-model="schemeCode"
              :options="schemeDropdownOpts"
              float-label="SchemeCode *"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" v-if="schemeCode">
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
            :options="studentOptionss"
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
      schemeCode: '',
      totalmarks: '',
      scannedItemDecode: '',
      tempsessionvalue:'',
      studentMark: '',
      studentIDs: '',
      scannedItem: '',
      subjectMarks: '',
      subjectDropdownOpts: [],
      schemeDropdownOpts: [],
      studentmarkdetails: [],
      semOptions: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'},{'label': '8SEM', 'value': '8SEM'}],
      studentOptionss: [],
      tab: 'exam1'
    }
  },
  created () {
    var that = this
    that.user = localStorage.getItem('username')
    that.flagShow = localStorage.getItem('flagShow')
    if (!that.user) {
      that.$router.push('/')
    } else {
      setTimeout(function(){
        that.$refs.totalmarks.focus()
      }, 500)
    }
  },
  methods: {
    enableScanDiv () {
      var that = this
      setTimeout(function(){
        that.$refs.scannedItem.focus()
      }, 500)
    },
    checkBinType (e) {
      let that = this
      if (that.totalmarks && that.semId && that.schemeCode && that.subId && that.studentIDs && that.scannedItem) {
        var sem_obj = {
          'total_marks': that.totalmarks, 'sem': that.semId, 'scheme': that.schemeCode,
          'subject': that.subId, 'student': that.studentIDs, 'barcode': that.scannedItem
        }
        axios.post(baseUrlForBackend+'govweb/update_semester_marks/', JSON.stringify(sem_obj))
        .then(function(resp){
          if (resp.data == 'Success') {
            that.scannedItem = ''
            that.$q.notify({color: 'positive', textColor: 'white', message: resp.data, position: 'center', timeout: 1000 })
          } else if(resp.data == 'Already this barcode Available') {
            that.$q.notify({color: 'negative', textColor: 'white', message: resp.data, position: 'center', timeout: 1000 })
          } else {
            that.$q.notify({color: 'negative', textColor: 'white', message: resp.data, position: 'center', timeout: 1000 })
          }
        })
      } else {
        that.$q.notify({color: 'negative', textColor: 'white', message: 'INPUT MISMATCH !!!', position: 'center', timeout: 1000 })
      }
    },
    getSubjects_scheme_Data () {
      var that = this
      that.schemeDropdownOpts = []
      var sem_obj = {
        'sem': that.semId
      }
      axios.post(baseUrlForBackend+'govweb/get_sem_schemes/', JSON.stringify(sem_obj))
      .then(function(resp){
        if (resp.data != 'SchemeCode Details Not Available for this Semester' && resp.data) {
          resp.data.forEach(function(item){
            that.schemeDropdownOpts.push({
              'label': item.scheme,
              'value' : item.scheme,
            })
          });
          that.getSubjectsData()
        } else if(resp.data == 'SchemeCode Details Not Available for this Semester') {
          that.showNotify(resp.data)
        } else {
          that.showNotify('something went Wrong !!!')
        }
      })
    },
    getSubjectsData () {
      var that = this
      that.subjectDropdownOpts = []
      var sem_obj = {
        'sem': that.semId
      }
      axios.post(baseUrlForBackend+'govweb/get_sem_subjects/', JSON.stringify(sem_obj))
      .then(function(resp){
        if (resp.data != 'Subject Details Not Available for this Semester' && resp.data) {
          resp.data.forEach(function(item){
            that.subjectDropdownOpts.push({
              'label': item.subject,
              'value' : item.subject,
            })
          });
        } else if(resp.data == 'Subject Details Not Available for this Semester') {
          that.showNotify(resp.data)
        } else {
          that.showNotify('something went Wrong !!!')
        }
      })
    },
    getUsersData () {
      var that = this
      that.studentOptionss = []
      var sem_obj = {
        'sem': that.semId
      }
      axios.post(baseUrlForBackend+'govweb/get_student_names/', JSON.stringify(sem_obj))
      .then(function(resp){
        if (resp.data != 'NO Students are Found' && resp.data) {
          resp.data.forEach(function(item){
            that.studentOptionss.push({
              'label': item.pin,
              'value' : item.pin,
            })
          });
        } else if(resp.data == 'NO Students are Found') {
          that.showNotify(resp.data)
        } else {
          that.showNotify('something went Wrong !!!')
        }
      })
    },
    emtpyAllFields () {
      var that = this
      that.userModalAdd = false
      that.semId = ''
      that.totalmarks =  ''
      that.subId = ''
      that.schemeCode = ''
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
