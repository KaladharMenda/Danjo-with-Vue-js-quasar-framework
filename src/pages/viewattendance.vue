<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolblue">
          <q-toolbar-title>
            <b>View Attendance Details</b>
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
            <q-select
              v-model="month"
              :options="month_options"
              float-label="MONTH"
            />
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
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6" align="center">
          <q-btn color="purple" @click="get_attendence_details()" :disabled="btnLoading" style="background: linear-gradient(60deg, #66bb6a, #43a047) !important;">
            <q-spinner-hourglass v-if="btnLoading" class="on-left"/>
            GET STUDENT DETAILS
          </q-btn>
        </div>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-btn color="purple" @click="downloadCsv('tableTitle')" :disabled="btnLoading" style="background: linear-gradient(60deg, rgb(95, 105, 96), rgb(113, 113, 113)) !important;">
            <img src="statics/excel.png" style="height: 25px;width: auto" class="on-left">
            Download CSV
        </q-btn>
      </div>
      <div class="row">
        <table class="q-table responsive" style="width: 100%; text-align: center; border-color: white;">
          <thead>
            <tr>
              <th style="font-family: sans-serif;"><b>PIN</b></th>
              <th style="font-family: sans-serif;"><b>Student Name</b></th>
              <th style="font-family: sans-serif;"><b>Academic Year</b></th>
              <th style="font-family: sans-serif;"><b>Period</b></th>
              <th style="font-family: sans-serif;"><b>College Working Days</b></th>
              <th style="font-family: sans-serif;"><b>Student Attend Days</b></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data ,index) in student_attendance_details" :key="index">
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="PIN">{{ data.Pin }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Student Name">{{ data.StudentName }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Academic Year">{{ data.year_sem }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Period">{{ data.period }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="College Working Days">{{ data.CollegeWorkingDays }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Student Attend Days">{{ data.StudentAttendDays }}</td>
            </tr>
          </tbody>
        </table>
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
      month_options: [{'label': 'January', 'value': 'January'},{'label': 'February', 'value': 'February'},{'label': 'March', 'value': 'March'},{'label': 'April', 'value': 'April'},{'label': 'May', 'value': 'May'},{'label': 'June', 'value': 'June'},{'label': 'July', 'value': 'July'},{'label': 'August', 'value': 'August'},{'label': 'September', 'value': 'September'},{'label': 'October', 'value': 'October'},{'label': 'November', 'value': 'November'},{'label': 'December', 'value': 'December'}],
      year_sem_options: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'}],
      period_options: [{'label': '1st to 15 Days', 'value': 'first_period'},{'label': '16th to Month End', 'value': 'second_period'},{'label': '1st to Month End', 'value': 'complete'}],
      btnLoading: false,
      student_attendance_details: [],
    }
  },
  created () {
    var that = this
  },
  methods: {
    updateCreateCartonsDt () {
      var that = this
      that.tableData = []
      that.loading = true
      firebase.database().ref('StudentDetails').once('value', function(data){
        data.forEach(function(record){
          that.tableData.push({
            'id' : record.key,
            'name': record.val().name,
          })
        })
          // that.tableData = that.tableData.sort(function(a,b){
          //   return new Date(b.date) - new Date(a.date);
          // })
          that.loading = false
        })
    },
    get_attendence_details () {
      let that = this
      that.btnLoading = true
      var attendence_dict = {}
      that.student_attendance_details = []
      attendence_dict ['year_sem'] = that.year_sem
      attendence_dict['month'] = that.month
      if (that.year_sem !='' && that.month != '' && that.period != '') {
        attendence_dict ['year_sem'] = that.year_sem
        attendence_dict['month'] = that.month
        attendence_dict['period'] = that.period
        that.alldivisionenable = true
        axios.post(baseUrlForBackend+'govweb/all_attendence/',JSON.stringify(attendence_dict))
        .then(function(resp){
          resp.data.forEach(function(record){
            that.student_attendance_details.push({
              'Pin' : record.pin,
              'StudentName': record.student_name,
              'year_sem':record.year_sem,
              'period': record.period,
              'CollegeWorkingDays': record.working_days,
              'StudentAttendDays': record.attended_days
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
    downloadCsv(title) {
      this.JSONToCSVConvertor(this.student_attendance_details, 'okay', 1)
    },
    JSONToCSVConvertor(JSONData, ReportTitle, ShowLabel) {
        var arrData = typeof JSONData != 'object' ? JSON.parse(JSONData) : JSONData;
        var CSV = '';
        CSV += ReportTitle + '\r\n\n';
        if (ShowLabel) {
            var row = "";
            for (var index in arrData[0]) {
                row += index + ',';
            }
            row = row.slice(0, -1);
            CSV += row + '\r\n';
        }
        for (var i = 0; i < arrData.length; i++) {
            var row = "";
            for (var index in arrData[i]) {
                row += '"' + arrData[i][index] + '",';
            }
            row.slice(0, row.length - 1);
            CSV += row + '\r\n';
        }
        if (CSV == '') {
            alert("Invalid data");
            return;
        }
        var fileName = ReportTitle.replace(/ /g,"_");
        var blobdata = new Blob([CSV],{type : 'text/csv'});
        var link = document.createElement("a");
        link.setAttribute("href", window.URL.createObjectURL(blobdata));
        link.setAttribute("download", "Data.csv");
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    },
  }
}
</script>

<style>
</style>
