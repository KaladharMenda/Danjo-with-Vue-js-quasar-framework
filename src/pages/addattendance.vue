<template>
  <div class="About">
    <q-card class="bg-white card-styl width_typesss">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolblue">
          <q-toolbar-title>
            <b>Attendance Details</b>
          </q-toolbar-title>
        </q-toolbar>
      </div>
      <div class="row gutter-sm" style="margin-top: 0px;">
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="year_sem"
              :options="year_sem_options"
              float-label="YEAR / SEMESTER"
            />
          </q-field>
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="month" float-label="MONTH " readonly/>
          </q-field>
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="period"
              :options="period_options"
              float-label="PERIOD"
            />
          </q-field>
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="working_days" float-label="TOTAL COLLEGE WORKING DAYS"/>
          </q-field>
        </div>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center" style="padding-bottom: 15px;">
        <q-btn color="purple" @click="get_attendence_details()" :disabled="btnLoading" style="background: linear-gradient(60deg, #66bb6a, #43a047) !important;">
          <q-spinner-hourglass v-if="btnLoading" class="on-left"/>
          GET STUDENT DETAILS
        </q-btn>
      </div>
      <div class="row" v-if="alldivisionenable">
        <table class="q-table responsive" style="width: 100%; text-align: center; border-color: white;" border="1" cellspacing="2">
          <thead>
            <tr>
              <th style="font-family: sans-serif;"><b>PIN</b></th>
              <th style="font-family: sans-serif;"><b>Student Name</b></th>
              <th style="font-family: sans-serif;"><b>Academic Year</b></th>
              <th style="font-family: sans-serif;"><b>Working Days</b></th>
              <th style="font-family: sans-serif;"><b>No of Days Attend</b></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data ,index) in student_attendance_details" :key="index">
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="PIN">{{ data.pin }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Student Name">{{ data.student_name }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Academic Year">{{ data.year_sem }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="No of Days Attend">{{ data.working_days }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);">
                <q-field>
                  <q-input  type="text" v-model="data.no_of_days_attend"/>
                </q-field>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center" style="padding-top: 15px;" v-if="alldivisionenable">
        <q-btn color="light-blue-7" icon-right="send" @click="send_attendence_details()" :disabled="btnLoadings" style="    background: linear-gradient(60deg, rgb(27, 98, 204), rgb(8, 149, 249)) !important;">
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
      month: '',
      year_sem: '',
      period: '',
      year_sem_options: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'},{'label': '8SEM', 'value': '8SEM'},{'label': 'PROJECT', 'value': 'PROJECT'}],
      period_options: [{'label': '1st to 15 Days', 'value': 'first_period'},{'label': '16th to Month End', 'value': 'second_period'}],
      btnLoading: false,
      btnLoadings: false,
      working_days: '',
      student_attendance_details: [],
      alldivisionenable : false,
    }
  },
  created () {
    var that = this
    that.convertDate(new Date().getMonth())
  },
  methods: {
    send_attendence_details () {
      var that = this
      that.btnLoadings = true
      console.log(that.student_attendance_details)
      axios.post(baseUrlForBackend+'govweb/attendece_update/',JSON.stringify(that.student_attendance_details))
      .then(function(resp){
        let respdata = resp.data
        console.log(respdata)
        that.$q.notify({color: 'green', textColor: 'white', message:respdata, position: 'center', timeout: 1000})
        that.btnLoadings = false
      })
    },
    get_attendence_details () {
      let that = this
      that.btnLoading = true
      var attendence_dict = {}
      that.student_attendance_details = []
      if (that.year_sem !='' && that.month != '' && that.working_days != '' && that.period != '') {
        attendence_dict ['year_sem'] = that.year_sem
        attendence_dict['month'] = that.month
        attendence_dict['period'] = that.period
        that.alldivisionenable = true
        axios.post(baseUrlForBackend+'govweb/get_attendence_names/',JSON.stringify(attendence_dict))
        .then(function(resp){
          resp.data.forEach(function(record){
            that.student_attendance_details.push({
              'pin' : record.pin,
              'student_name': record.student_name,
              'year_sem':record.year_sem,
              'period': that.period,
              'working_days': that.working_days,
              'month':that.month,
              'no_of_days_attend': record.attended_days,
            })
          })
          that.btnLoading = false
          console.log(that.student_attendance_details)
        })
      } else {
        that.btnLoading = false
        that.$q.notify({color: 'negative', textColor: 'white', message: 'Please Select Required Fields', position: 'center', timeout: 1000})
      }
    },
    convertDate: function (date) {
      var that = this
      if ((date+1) == 1) {
        that.month = 'January'
      }else if((date+1) == 2) {
        that.month = 'February'
      }else if((date+1) == 3) {
        that.month = 'March'
      }else if((date+1) == 4) {
        that.month = 'April'
      }else if((date+1) == 5) {
        that.month = 'May'
      }else if((date+1) == 6) {
        that.month = 'June'
      }else if((date+1) == 7) {
        that.month = 'July'
      }else if((date+1) == 8) {
        that.month = 'August'
      }else if((date+1) == 9) {
        that.month = 'September'
      }else if((date+1) == 10) {
        that.month = 'October'
      }else if((date+1) == 11) {
        that.month = 'November'
      }else if((date+1) == 12) {
        that.month = 'December'
      }
      console.log(that.month)
    },
  }
}
</script>

<style>
</style>
