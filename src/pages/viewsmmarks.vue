<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolgradientgreen">
          <q-toolbar-title>
            <b>View Student SM Marks Details</b>
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
              @input="getSubjects_scheme_Data"
            />
          </q-field>
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6" v-if="year_sem">
          <q-field>
            <q-select
              v-model="schemeCode"
              :options="schemeDropdownOpts"
              float-label="SchemeCode *"
            />
          </q-field>
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-16" v-if="schemeCode">
          <q-select
            v-model="subId"
            :options="subjectDropdownOpts"
            float-label="Subject *"
          />
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6" v-if="subId">
          <q-btn color="purple" @click="get_student_details()" :disabled="btnLoading" style="background: #ff9e10 !important;">
            <q-spinner-hourglass v-if="btnLoading" class="on-left"/>
            VIEW SM MARKS
          </q-btn>
        </div>
      </div>
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center" v-if = "table_enable_flag">
        <q-btn color="purple" @click="downloadCsv('tableTitle')" :disabled="btnLoading" style="background: linear-gradient(60deg, rgb(95, 105, 96), rgb(113, 113, 113)) !important;">
            <img src="statics/excel.png" style="height: 25px;width: auto" class="on-left">
            Download CSV
        </q-btn>
      </div>
      <q-table
         v-if="table_enable_flag"
         :data="final_semester_marks"
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
      <!-- <div class="row" v-if = "table_enable_flag"> -->
        <!-- <table class="q-table responsive" style="width: 100%; text-align: center; border-color: white;">
          <thead>
            <tr>
              <th style="font-family: sans-serif;"><b>PIN</b></th>
              <th style="font-family: sans-serif;"><b>Student Name</b></th>
              <th style="font-family: sans-serif;"><b>Scheme Code</b></th>
              <th style="font-family: sans-serif;"><b>Subject</b></th>
              <th style="font-family: sans-serif;"><b>Total Marks</b></th>
              <th style="font-family: sans-serif;"><b>Marks</b></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data ,index) in final_semester_marks" :key="index">
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="PIN">{{ data.Pin }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Student Name">{{ data.StudentName }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Scheme Code">{{ data.scheme }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Subject">{{ data.subject }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Total Marks">{{ data.total_marks }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Marks">{{ data.marks }}</td>
            </tr>
          </tbody>
        </table> -->
      <!-- </div> -->
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
      loading: false,
      separator: 'cell',
      filter: '',
      year_sem: '',
      year_sem_options: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'},{'label': '8SEM', 'value': '8SEM'}],
      btnLoading: false,
      subjectDropdownOpts: [],
      schemeDropdownOpts: [],
      schemeCode: '',
      subId: '',
      table_enable_flag : false,
      final_semester_marks: [],
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
        { name: 'Scheme', label: 'year/ Sem', align: 'center', field: 'Scheme', sortable: true },
        { name: 'Subject', label: 'Subject', align: 'center', field: 'Subject', sortable: true },
        { name: 'TotalMarks', label: 'Total Marks', align: 'center', field: 'TotalMarks', sortable: true },
        { name: 'Marks', label: 'Obtained Marks', align: 'center', field: 'Marks', sortable: true }
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
    get_student_details () {
      var that = this
      that.loading = true
      that.btnLoading = true
      that.table_enable_flag = true
      that.final_semester_marks = []
      if (that.year_sem && that.schemeCode && that.subId) {
        var sem_obj = {
          'sem': that.year_sem,
          'scheme': that.schemeCode,
          'subject': that.subId
        }
        axios.post(baseUrlForBackend+'govweb/get_semester_viewtable/', JSON.stringify(sem_obj))
        .then(function(resp){
          if (resp.data != 'No Data Found !!' && resp.data) {
            that.final_semester_marks = []
            resp.data.forEach(function(record){
              that.final_semester_marks.push({
                'Pin' : record.student_id,
                'StudentName': record.student_name,
                'Scheme':record.scheme,
                'Subject': record.subject,
                'TotalMarks': record.total_marks,
                'Marks': record.marks
              })
            })
            that.btnLoading = false
            that.loading = false
          } else if(resp.data == 'No Data Found !!') {
            that.$q.notify({color: 'negative', textColor: 'white', message: resp.data, position: 'center', timeout: 1000 })
            that.btnLoading = false
            that.loading = false
          } else {
            that.showNotify('something went Wrong !!!')
            that.btnLoading = false
            that.loading = false
          }
        })
      } else {
        that.$q.notify({color: 'negative', textColor: 'white', message: 'Please select the Required Fields', position: 'center', timeout: 1000 })
      }
    },
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
        'sem': that.year_sem
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
    showNotify (msg) {
      let that = this
      that.$q.notify({
        color: 'green',
        textColor: 'white',
        message: msg,
        position: 'bottom-right',
        timeout: 1000
      })
    },
    downloadCsv(title) {
      this.JSONToCSVConvertor(this.final_semester_marks, '', 1)
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
        link.setAttribute("download", "SemesterMarks.csv");
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    },
  }
}
</script>

<style>
</style>
