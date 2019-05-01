<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolgradientred">
          <q-toolbar-title>
            <b>View Project Marks</b>
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
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" align="center">
          <q-btn color="purple" @click="get_pm_details()" :disabled="btnLoading" style="background: linear-gradient(60deg, #66bb6a, #43a047) !important;">
            <q-spinner-hourglass v-if="btnLoading" class="on-left"/>
            View Project Marks
          </q-btn>
        </div>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center" v-if="alldivisionenable" style="padding-top: 5px;">
        <q-btn color="purple" @click="downloadCsv('tableTitle')" :disabled="btnLoading" style="background: linear-gradient(60deg, rgb(95, 105, 96), rgb(113, 113, 113)) !important;">
            <img src="statics/excel.png" style="height: 25px;width: auto" class="on-left">
            Download CSV
        </q-btn>
      </div>
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
      <!-- <div class="row">
        <table class="q-table responsive" style="width: 100%; text-align: center; border-color: white;">
          <thead>
            <tr>
              <th style="font-family: sans-serif;"><b>PIN</b></th>
              <th style="font-family: sans-serif;"><b>Student Name</b></th>
              <th style="font-family: sans-serif;"><b>Academic Year</b></th>
              <th style="font-family: sans-serif;"><b>Scheme Code</b></th>
              <th style="font-family: sans-serif;"><b>Project Name</b></th>
              <th style="font-family: sans-serif;"><b>Total Marks</b></th>
              <th style="font-family: sans-serif;"><b>Obtained Marks</b></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data ,index) in student_attendance_details" :key="index">
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="PIN">{{ data.Pin }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Student Name">{{ data.StudentName }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Academic Year">{{ data.year_sem }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Scheme Code">{{ scheme_code }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Project Name">{{ data.project_name }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Total Marks">{{ data.total_marks }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Obtained Marks">{{ data.obtained_marks }}</td>
            </tr>
          </tbody>
        </table>
      </div> -->
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
      alldivisionenable: false,
      loading: false,
      separator: 'cell',
      filter: '',
      month: '',
      year_sem: '',
      period: '',
      scheme_code:'',
      year_sem_options: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'},{'label': '8SEM', 'value': '8SEM'},{'label': 'PROJECT', 'value': 'PROJECT'}],
      btnLoading: false,
      schemeDropdownOpts: [],
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
        { name: 'Year/Sem', label: 'year/ Sem', align: 'center', field: 'Year/Sem', sortable: true },
        { name: 'projectName', label: 'Project Name', align: 'center', field: 'projectName', sortable: true },
        { name: 'TotalMarks', label: 'Total Marks', align: 'center', field: 'TotalMarks', sortable: true },
        { name: 'ObtainedMarks', label: 'Obtained Marks', align: 'center', field: 'ObtainedMarks', sortable: true }
      ]
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
    get_pm_details () {
      let that = this
      that.btnLoading = true
      that.loading = true
      var pm_dict = {}
      that.student_attendance_details = []
      pm_dict ['year_sem'] = that.year_sem
      pm_dict['month'] = that.month
      if (that.year_sem !='' && that.scheme_code != '') {
        pm_dict ['year_sem'] = that.year_sem
        pm_dict['scheme_code'] = that.scheme_code
        pm_dict['view'] = 'view_mode'
        that.alldivisionenable = true
        axios.post(baseUrlForBackend+'govweb/get_pm_marks/',JSON.stringify(pm_dict))
        .then(function(resp){
          that.student_attendance_details = []
          resp.data.forEach(function(record){
            that.student_attendance_details.push({
              'Pin' : record.pin,
              'StudentName': record.student_name,
              'Year/Sem':record.year_sem,
              'projectName': record.project_name,
              'TotalMarks': record.total_marks,
              'ObtainedMarks': record.marks,
            })
          })
          that.loading = false
          that.btnLoading = false
        })
      } else {
        that.loading = false
        that.btnLoading = false
        that.$q.notify({color: 'negative', textColor: 'white', message: 'Please Select Required Fields', position: 'center', timeout: 1000})
      }
    },
    downloadCsv(title) {
      this.JSONToCSVConvertor(this.student_attendance_details, '', 1)
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
