<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolgradientblue">
          <q-toolbar-title>
            <b>View Student Unit Marks Details</b>
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
              @input="getSubjectsData"
            />
          </q-field>
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="unit_exam"
              :options="unit_exam_options"
              float-label="UNIT EXAM TYPE"
            />
          </q-field>
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="subject"
              :options="subjectDropdownOpts"
              float-label="Subject"
            />
          </q-field>
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6" align="center">
          <q-btn color="purple" icon-right="send" @click="get_unit_details()" :disabled="btnLoading" style="background: linear-gradient(60deg, #66bb6a, #43a047) !important;">
            <q-spinner-hourglass v-if="btnLoading" class="on-left"/>
            Show Unit Marks
          </q-btn>
        </div>
      </div>
      <q-table
         v-if="alldivisionenable"
         :data="student_unit_details"
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
              <th style="font-family: sans-serif;"><b>Unit Exam</b></th>
              <th style="font-family: sans-serif;"><b>Subject</b></th>
              <th style="font-family: sans-serif;"><b>Total Marks</b></th>
              <th style="font-family: sans-serif;"><b>Obtained Marks</b></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data ,index) in student_unit_details" :key="index">
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="PIN">{{ data.pin }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Student Name">{{ data.student_name }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Unit Exam">{{ unit_exam }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Subject">{{ subject }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Total Marks">{{ data.total_marks }}</td>
              <td style="border-top: 1px solid rgb(236, 236, 236);" class="text-center" data-th="Obtained Marks">{{ data.marks }}</td>

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
      loading: false,
      separator: 'cell',
      filter: '',
      exam_date: '',
      year_sem: '',
      unit_exam: '',
      subject: '',
      total_marks: '',
      year_sem_options: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'},{'label': '8SEM', 'value': '8SEM'}],
      unit_exam_options: [{'label': 'UNIT TEST ONE', 'value': 'UNIT TEST ONE'},{'label': 'UNIT TEST TWO', 'value': 'UNIT TEST TWO'},{'label': 'UNIT TEST THREE', 'value': 'UNIT TEST THREE'}],
      subject_options: [{'label': 'x', 'value': 'x'},{'label': 'y', 'value': 'y'}],
      btnLoading: false,
      alldivisionenable: false,
      student_unit_details: [],
      subjectDropdownOpts: [],
      columns: [
        {
          name: 'pin',
          required: true,
          label: 'PIN',
          align: 'center',
          field: 'pin',
          sortable: true,
          descending: true
        },
        { name: 'student_name', label: 'Student Name', align: 'center', field: 'student_name', sortable: true },
        { name: 'year_sem', label: 'year/ Sem', align: 'center', field: 'year_sem', sortable: true },
        { name: 'total_marks', label: 'Total Marks', align: 'center', field: 'total_marks', sortable: true },
        { name: 'marks', label: 'Obtained Marks', align: 'center', field: 'marks', sortable: true }
      ]
    }
  },
  created () {
    var that = this
  },
  methods: {
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
    get_unit_details () {
      var that = this
      var unit_dict = {}
      if (that.year_sem != '' && that.unit_exam != '') {
          unit_dict['year_sem'] = that.year_sem
          unit_dict['unit_exam'] = that.unit_exam
          unit_dict['subject'] = that.subject
          unit_dict['view'] = 'view_mode'
          that.loading = true
          that.alldivisionenable = true
          that.btnLoading = true
          axios.post(baseUrlForBackend+'govweb/get_unit_marks/',JSON.stringify(unit_dict))
          .then(function(resp){
            that.student_unit_details = []
            resp.data.forEach(function(record){
              that.student_unit_details.push({
                'pin' : record.pin,
                'student_name': record.student_name,
                'year_sem':record.year_sem,
                'marks': record.marks,
                'total_marks':record.total_marks,
              })
            })
            that.btnLoading = false
            that.loading = false
          })
      } else {
        that.$q.notify({color: 'negative', textColor: 'white', message: 'Please select the Required Fields', position: 'center', timeout: 1000 })
        that.btnLoading = false
        that.loading = false
      }
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
