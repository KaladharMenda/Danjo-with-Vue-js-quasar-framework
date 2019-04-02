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
             <q-input type="text" ref="scannedItemDecode" v-model="scannedItemDecode" v-on:keyup.enter="checkBinTypeA" float-label="Scan Sem Paper BarCode *"/>
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
                  />
              </q-field>
              <q-btn class="toolgreen" style="width:100%;color: aliceblue;" label="Update Sem Subject Marks" @click="updatemarks()"/>
          </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"></div>
      </div>
      <div class="row" v-if="enableEditDiv">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"></div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
          <table class="q-table">
            <tr>
              <th class="text-left">Year / Semester:</th>
              <td class="text-right">II</td>
            </tr>
            <tr>
              <th class="text-left">Subject:</th>
              <td class="text-right">Engineering Physics</td>
            </tr>
            <tr>
              <th class="text-left">Student PIN:</th>
              <td class="text-right">14341a0598</td>
            </tr>
            <tr>
              <th class="text-left">Sem paper Barcode ID:</th>
              <td class="text-right">{{scannedItemDecode}}</td>
            </tr>
            <tr>
              <th class="text-left">Marks Posted By:</th>
              <td class="text-right">User Name</td>
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
    updatemarks () {
      var that = this
      if (that.subjectMarks) {
        that.$q.notify({color: 'positive', textColor: 'white', message: 'Successfully Updated Subject Marks', position: 'center', timeout: 1000 })
        that.emtpyAllFields()
        setTimeout(function(){
          that.$refs.scannedItemDecode.focus()
        }, 500)
      } else {
        that.$q.notify({color: 'negative', textColor: 'white', message: 'please Enter Subject Marks', position: 'center', timeout: 1000 })
        that.$refs.subjectMarks.focus()
      }
    },
    get_decode_data () {
      var that = this
      that.emtpyAllFields('ss2')
      setTimeout(function(){
        that.$refs.scannedItemDecode.focus()
      }, 500)
    },
    enableScanDiv () {
      var that = this
      setTimeout(function(){
        that.$refs.scannedItem.focus()
      }, 500)
    },
    checkBinTypeA (e) {
      let that = this
      that.enableEditDiv = true
      setTimeout(function(){
        that.$refs.subjectMarks.focus()
      }, 500)
      // that.$q.notify({color: 'positive', textColor: 'white', message: 'Successfully Added Barcode Number', position: 'center', timeout: 1000 })
      // that.emtpyAllFields()
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
