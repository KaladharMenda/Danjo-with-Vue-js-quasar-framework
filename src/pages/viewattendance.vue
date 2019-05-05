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
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" v-if="alldivisionenable" align="center">
        <q-btn color="purple" @click="downloadCsv('tableTitle')" :disabled="btnLoading" style="background: linear-gradient(60deg, rgb(95, 105, 96), rgb(113, 113, 113)) !important;">
            <img src="statics/excel.png" style="height: 25px;width: auto" class="on-left">
            Download CSV
        </q-btn>
      </div>
      <!-- <div class="row"> -->
        <q-table
         v-if="alldivisionenable"
         :data="student_attendance_details"
         :columns="columns"
         color="black"
         :filter="filter"
         :separator="separator"
         row-key="name"
         :loading="loading"
         >
       <template slot="top-right" slot-scope="props">
         <q-search class="col-12" v-model="filter" />
       </template>

       <q-tr slot="body" slot-scope="props" :props="props" class="cursor-pointer">
         <q-td v-for="col in props.cols" :key="col.name" :props="props">
           {{ col.value }}
         </q-td>
       </q-tr>
      </q-table>
        <!-- <table class="q-table responsive" style="width: 100%; text-align: center; border-color: white;">
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
        </table> -->
      <!-- </div> -->
    </q-card>
  </div>
</template>

<script>
import axios from 'axios'

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
      loading: false,
      separator: 'cell',
      filter: '',
      month: '',
      year_sem: '',
      period: '',
      month_options: [{'label': 'January', 'value': 'January'}, {'label': 'February', 'value': 'February'}, {'label': 'March', 'value': 'March'}, {'label': 'April', 'value': 'April'}, {'label': 'May', 'value': 'May'}, {'label': 'June', 'value': 'June'}, {'label': 'July', 'value': 'July'}, {'label': 'August', 'value': 'August'}, {'label': 'September', 'value': 'September'}, {'label': 'October', 'value': 'October'}, {'label': 'November', 'value': 'November'}, {'label': 'December', 'value': 'December'}],
      year_sem_options: [{'label': '1YR', 'value': '1YR'}, {'label': '2YR', 'value': '2YR'}, {'label': '3SEM', 'value': '3SEM'}, {'label': '4SEM', 'value': '4SEM'}, {'label': '5SEM', 'value': '5SEM'}, {'label': '6SEM', 'value': '6SEM'}, {'label': '7SEM', 'value': '7SEM'}, {'label': '8SEM', 'value': '8SEM'}, {'label': 'PROJECT', 'value': 'PROJECT'}],
      period_options: [{'label': '1st to 15 Days', 'value': 'first_period'}, {'label': '16th to Month End', 'value': 'second_period'}, {'label': '1st to Month End', 'value': 'complete'}],
      btnLoading: false,
      alldivisionenable: false,
      student_attendance_details: [],
      columns: [
        {
          name: 'Pin',
          required: true,
          label: 'PIN',
          align: 'center',
          field: 'Pin',
          sortable: true,
          descending: true
        },
        { name: 'StudentName', label: 'Student Name', align: 'center', field: 'StudentName', sortable: true },
        { name: 'year_sem', label: 'year/ Sem', align: 'center', field: 'year_sem', sortable: true },
        { name: 'period', label: 'Period', align: 'center', field: 'period', sortable: true },
        { name: 'CollegeWorkingDays', label: 'College Working Days', align: 'center', field: 'CollegeWorkingDays', sortable: true },
        { name: 'StudentAttendDays', label: 'Student Attend Days', align: 'center', field: 'StudentAttendDays', sortable: true }
      ]
    }
  },
  created () {
    var that = this
    that.user = localStorage.getItem('username')
    that.flagShow = localStorage.getItem('flagShow')
    if (!that.user || that.flagShow === 'false') {
      that.$router.push('/')
    }
  },
  methods: {
    get_attendence_details () {
      let that = this
      that.btnLoading = true
      that.loading = true
      that.alldivisionenable = true
      var baseUrlForBackend = 'http://3.82.197.239:8000/'
      var attendenceDict = {}
      that.student_attendance_details = []
      attendenceDict['year_sem'] = that.year_sem
      attendenceDict['month'] = that.month
      if (that.year_sem !== '' && that.month !== '' && that.period !== '') {
        attendenceDict['year_sem'] = that.year_sem
        attendenceDict['month'] = that.month
        attendenceDict['period'] = that.period
        axios.post(baseUrlForBackend + 'govweb/all_attendence/', JSON.stringify(attendenceDict))
          .then(function (resp) {
            that.student_attendance_details = []
            resp.data.forEach(function (record) {
              that.student_attendance_details.push({
                'Pin': record.pin,
                'StudentName': record.student_name,
                'year_sem': record.year_sem,
                'period': record.period,
                'CollegeWorkingDays': record.working_days,
                'StudentAttendDays': record.attended_days
              })
            })
            that.btnLoading = false
            that.loading = false
            console.log(that.student_attendance_details)
          })
      } else {
        that.btnLoading = false
        that.$q.notify({color: 'negative', textColor: 'white', message: 'Please Select Required Fields', position: 'center', timeout: 1000})
      }
    },
    downloadCsv (title) {
      this.JSONToCSVConvertor(this.student_attendance_details, '', 1)
    },
    JSONToCSVConvertor (JSONData, ReportTitle, ShowLabel) {
      var arrData = typeof JSONData !== 'object' ? JSON.parse(JSONData) : JSONData
      var CSV = ''
      CSV += ReportTitle + '\r\n\n'
      if (ShowLabel) {
        var row = ''
        for (var index in arrData[0]) {
          row += index + ','
        }
        row = row.slice(0, -1)
        CSV += row + '\r\n'
      }
      for (var i = 0; i < arrData.length; i++) {
        let row = ''
        for (let index in arrData[i]) {
          row += '"' + arrData[i][index] + '",'
        }
        row.slice(0, row.length - 1)
        CSV += row + '\r\n'
      }
      if (CSV === '') {
        alert('Invalid data')
        return
      }
      var blobdata = new Blob([CSV], {type: 'text/csv'})
      var link = document.createElement('a')
      link.setAttribute('href', window.URL.createObjectURL(blobdata))
      link.setAttribute('download', 'ViewAttendance.csv')
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)
    }
  }
}
</script>

<style>
</style>
