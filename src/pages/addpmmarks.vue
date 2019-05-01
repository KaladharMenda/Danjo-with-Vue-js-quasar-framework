<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl width_typesss">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolgradientred">
          <q-toolbar-title>
            <b>Add PM Marks For Students</b>
          </q-toolbar-title>
        </q-toolbar>
      </div>
      <div class="row gutter-sm" style="margin-top: 0px;">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="year_sem"
              :options="year_sem_options"
              float-label="YEAR / SEMESTER"
              @input="getSubjects_scheme_Data"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="scheme_code"
              :options="schemeDropdownOpts"
              float-label="SCHEME CODE"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="project_title" float-label="Project title"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="total_marks" float-label="TOTAL MARKS"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" align="center" style="padding-bottom: 5px;">
          <q-btn color="purple" @click="get_student_details()" :disabled="btnLoading" style="background: linear-gradient(60deg, #66bb6a, #43a047) !important;">
            <q-spinner-hourglass v-if="btnLoading" class="on-left"/>
            Add Project Marks
          </q-btn>
        </div>
      </div>
      <div class="row" v-if="alldivisionenable">
        <table class="q-table responsive" style="width: 100%; text-align: center; border-color: white;" border="1" cellspacing="2">
          <thead>
            <tr>
              <th style="font-family: sans-serif;"><b>PIN</b></th>
              <th style="font-family: sans-serif;"><b>Student Name</b></th>
              <th style="font-family: sans-serif;"><b>Academic Year</b></th>
              <th style="font-family: sans-serif;"><b>Marks</b></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data ,index) in student_unit_details" :key="index">
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="PIN">{{ data.pin }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Student Name">{{ data.student_name }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Academic Year">{{ data.year_sem }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);">
                <q-field>
                  <q-input  type="text" v-model="data.marks"/>
                </q-field>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center" style="padding-top: 15px;" v-if="alldivisionenable">
        <q-btn color="light-blue-7" icon-right="send" @click="send_pm_details()" :disabled="btnLoadings" style="    background: linear-gradient(60deg, rgb(27, 98, 204), rgb(8, 149, 249)) !important;">
          <q-spinner-hourglass v-if="btnLoadings" class="on-left"/>
          CONFIRM
        </q-btn>
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
  QInnerLoading,
  QSpinnerHourglass
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
    QInnerLoading,
    QSpinnerHourglass
  },
  data () {
    return {
      exam_date: '',
      year_sem: '',
      scheme_code: '',
      project_title:'',
      subject: '',
      total_marks: '',
      year_sem_options: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'},{'label': '8SEM', 'value': '8SEM'},{'label': 'PROJECT', 'value': 'PROJECT'}],
      unit_exam_options: [{'label': 'UNIT TEST ONE', 'value': 'UNIT TEST ONE'},{'label': 'UNIT TEST TWO', 'value': 'UNIT TEST TWO'},{'label': 'UNIT TEST THREE', 'value': 'UNIT TEST THREE'}],
      btnLoading: false,
      btnLoadings: false,
      schemeDropdownOpts: [],
      student_unit_details: [],
      alldivisionenable : false,
    }
  },
  created () {
    var that = this
    that.user = localStorage.getItem('username')
    that.flagShow = localStorage.getItem('flagShow')
    if (!that.user || that.flagShow == 'false') {
      that.$router.push('/')
    }
  },
  methods: {
    getSubjects_scheme_Data () {
      var that = this
      that.schemeDropdownOpts = []
      var sem_obj = {
        'sem': that.year_sem
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
        } else if(resp.data == 'SchemeCode Details Not Available for this Semester') {
          that.showNotify(resp.data)
        } else {
          that.showNotify('something went Wrong !!!')
        }
      })
    },
    get_student_details () {
      var that = this
      var pm_dict = {}
      if (that.year_sem != '' && that.project_title != '' && that.scheme_code != '' && that.total_marks != '') {
          pm_dict['year_sem'] = that.year_sem
          pm_dict['scheme_code'] = that.scheme_code
          pm_dict['project_title'] = that.project_title
          pm_dict['total_marks'] = that.total_marks
          that.alldivisionenable = true
          that.btnLoading = true
          axios.post(baseUrlForBackend+'govweb/get_pm_marks/',JSON.stringify(pm_dict))
          .then(function(resp){
            that.student_unit_details = []
            resp.data.forEach(function(record){
              that.student_unit_details.push({
                'pin' : record.pin,
                'student_name': record.student_name,
                'year_sem':record.year_sem,
                'marks': record.marks,
              })
            })
            that.btnLoading = false
          })
      } else {
        that.btnLoading = false
        that.$q.notify({color: 'negative', textColor: 'white', message: 'Please select the Required Fields', position: 'center', timeout: 1000 })
      }
    },
    send_pm_details (){
      var that = this
      that.btnLoadings = true
      that.student_unit_details[0]['scheme_code'] = that.scheme_code
      that.student_unit_details[0]['project_title'] = that.project_title
      that.student_unit_details[0]['total_marks'] = that.total_marks
      console.log(that.student_unit_details)
      axios.post(baseUrlForBackend+'govweb/pm_marks_update/',JSON.stringify(that.student_unit_details))
      .then(function(resp){
        let respdata = resp.data
        that.$q.notify({color: 'green', textColor: 'white', message:respdata, position: 'center', timeout: 1000})
        that.btnLoadings = false
      })
    },
    showNotify (msg) {
      let that = this
      that.$q.notify({
        color: 'negative',
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
