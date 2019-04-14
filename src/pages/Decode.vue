<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolgradientlightgreen">
          <q-toolbar-title>
            <b>Decode For Semester Exams</b>
          </q-toolbar-title>
        </q-toolbar>
      </div>
      <div class="row gutter-sm q-mb-md toppadding">
        <div class="col-lg-4 col-md-4"></div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
          <q-field v-if="!enableEditDiv">
             <q-input type="text" ref="scannedItemDecode" v-model="scannedItemDecode" v-on:keyup.enter="checkBinTypeA('get')" float-label="Scan Sem Paper BarCode *"/>
          </q-field>
          <q-chip v-if="enableEditDiv" avatar="statics/boy-avatar.png" small color="teal" align="center">{{  scannedItemDecode}}</q-chip>
        </div>
        <div class="col-lg-4 col-md-4"></div>
      </div>
      <div class="row" v-if= "enableEditDiv">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 scannedItemTop"></div>
          <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 scannedItemTop">
            <q-field>
               <q-input
                  type="text"
                  v-model="subjectMarks"
                  ref="subjectMarks"
                  float-label="Enter the Subject Marks"
                  v-on:keyup.enter="checkBinTypeA('save')"
                  />
              </q-field>
              <q-btn class="toolgreen" style="width:100%;color: aliceblue;" label="Update Sem Subject Marks" @click="checkBinTypeA('save')"/>
          </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"></div>
      </div>
      <div class="row" v-if="enableEditDiv">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"></div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
          <table class="q-table">
            <tr>
              <th class="text-left">Year / Semester:</th>
              <td class="text-right">{{years}}</td>
            </tr>
             <tr>
              <th class="text-left">Scheme Code:</th>
              <td class="text-right">{{scheme_codes}}</td>
            </tr>
            <tr>
              <th class="text-left">Subject:</th>
              <td class="text-right">{{subjectss}}</td>
            </tr>
            <tr>
              <th class="text-left">Student PIN:</th>
              <td class="text-right">{{students}}</td>
            </tr>
            <tr>
              <th class="text-left">Sem paper Barcode ID:</th>
              <td class="text-right">{{barcodes}}</td>
            </tr>
            <tr>
              <th class="text-left">Total Marks:</th>
              <td class="text-right">{{total_marks}}</td>
            </tr>
            <tr>
              <th class="text-left">Marks Posted By:</th>
              <td class="text-right">{{users}}</td>
            </tr>
          </table>
        </div>
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
      years: '',
      scheme_codes: '',
      subjectss: '',
      students: '',
      barcodes: '',
      total_marks: '',
      users: '',
      scannedItemDecode: '',
      tempsessionvalue:'',
      studentMark: '',
      studentIDs: '',
      loader: false,
      loading: false,
      tempvalue: '',
      userModalAdd: false,
      ediTablEnable: false,
      enableEditDiv: false,
      scannedItem: '',
      subjectMarks: '',
      subjectDropdownOpts: [],
      studentmarkdetails: []
    }
  },
  created () {
    var that = this
    setTimeout(function(){
      that.$refs.scannedItemDecode.focus()
    }, 200)
  },
  methods: {
    enableScanDiv () {
      var that = this
      setTimeout(function(){
        that.$refs.scannedItem.focus()
      }, 500)
    },
    checkBinTypeA (e) {
      var that = this
      if (e == 'get') {
        if (that.scannedItemDecode) {
          var sem_obj = {
            'barcode': that.scannedItemDecode,
            'flag': e
          }
          axios.post(baseUrlForBackend+'govweb/get_semester_marks_update/', JSON.stringify(sem_obj))
          .then(function(resp){
            if (resp.data != 'Scanned Barcode Not Exists' && resp.data) {
              console.log(resp.data)
              that.enableEditDiv = true
              setTimeout(function(){
                that.$refs.subjectMarks.focus()
              }, 200)
              that.years = resp.data[0].year
              that.scheme_codes = resp.data[0].scheme
              that.subjectss = resp.data[0].subject
              that.students = resp.data[0].student
              that.barcodes = resp.data[0].barcode
              that.total_marks = resp.data[0].totalmarks
              that.users = localStorage.getItem('username')
            } else if(resp.data == 'Scanned Barcode Not Exists') {
              that.showNotify(resp.data)
            } else {
              that.showNotify('something went Wrong !!!')
            }
          })
        } else {
          that.$q.notify({color: 'negative', textColor: 'white', message: 'Successfully Added Barcode Number', position: 'center', timeout: 1000 })
        }
      } else if (e == 'save') {
        if (that.subjectMarks) {
          var sem_obj = {
            'barcode': that.barcodes,
            'marks': that.subjectMarks,
            'posted_by': localStorage.getItem('username'),
            'flag': e
          }
          axios.post(baseUrlForBackend+'govweb/get_semester_marks_update/', JSON.stringify(sem_obj))
          .then(function(resp){
            if (resp.data == 'Success') {
              that.enableEditDiv = false
              that.years = ''
              that.scheme_codes = ''
              that.subjectss = ''
              that.students = ''
              that.barcodes = ''
              that.total_marks = ''
              that.users = ''
              that.subjectMarks = ''
              that.scannedItemDecode = ''
              that.$q.notify({color: 'positive', textColor: 'white', message: resp.data, position: 'center', timeout: 1000 })
              setTimeout(function(){
                that.$refs.scannedItemDecode.focus()
              }, 20)
            } else {
              that.$q.notify({color: 'negative', textColor: 'white', message: resp.data, position: 'center', timeout: 1000 })
            }
          })
        } else {
          that.$q.notify({color: 'negative', textColor: 'white', message: 'Successfully Added Barcode Number', position: 'center', timeout: 1000 })
        }
      }
    },
    enableresultsdiv () {
      let that = this
      that.userModalAdd = true
      if (that.sessionvalue == 'ss1'){
        that.tempsessionvalue = 'SessionExam 1'
      } else if (that.sessionvalue == 'ss2') {
        that.tempsessionvalue = 'SessionExam 2'
      }
    },
    emtpyAllFields () {
      var that = this
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
