<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolgradientblue">
          <q-toolbar-title>
            <b>Add Unit Marks For Students</b>
          </q-toolbar-title>
        </q-toolbar>
      </div>
      <div class="row gutter-sm" style="margin-top: 0px;">
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-datetime color="blue" v-model="exam_date" type="date" float-label="EXAM DATE"/>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="year_sem"
              :options="year_sem_options"
              float-label="YEAR / SEMESTER"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="unit_exam"
              :options="unit_exam_options"
              float-label="UNIT EXAM TYPE"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="subject"
              :options="subject_options"
              float-label="SUBJECT"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="total_marks" float-label="TOTAL MARKS"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6" align="center">
          <q-btn color="purple" icon-right="send" @click="get_student_details()" :disabled="btnLoading" style="background: linear-gradient(60deg, #66bb6a, #43a047) !important;">
            <q-spinner-hourglass v-if="btnLoading" class="on-left"/>
            GET STUDENT DETAILS
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
        <q-btn color="light-blue-7" icon-right="send" @click="send_attendence_details()" :disabled="btnLoading" style="    background: linear-gradient(60deg, rgb(27, 98, 204), rgb(8, 149, 249)) !important;">
          <q-spinner-hourglass v-if="btnLoading" class="on-left"/>
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
      unit_exam: '',
      subject: '',
      total_marks: '',
      year_sem_options: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'}],
      unit_exam_options: [{'label': 'UNIT TEST ONE', 'value': 'UNIT TEST ONE'},{'label': 'UNIT TEST TWO', 'value': 'UNIT TEST TWO'},{'label': 'UNIT TEST THREE', 'value': 'UNIT TEST THREE'}],
      subject_options: [{'label': 'x', 'value': 'x'},{'label': 'y', 'value': 'y'}],
      btnLoading: false,
      student_unit_details: [],
      alldivisionenable : false,
    }
  },
  created () {
    var that = this
  },
  methods: {
    get_student_details () {
      var that = this
      var unit_dict = {}
      if (that.exam_date != '' && that.year_sem != '' && that.unit_exam != '' && that.subject != '' && that.total_marks != '') {
          unit_dict['exam_date'] = that.exam_date
          unit_dict['year_sem'] = that.year_sem
          unit_dict['unit_exam'] = that.unit_exam
          unit_dict['subject'] = that.subject
          unit_dict['total_marks'] = that.total_marks
          that.alldivisionenable = true
          axios.post(baseUrlForBackend+'govweb/get_unit_marks/',JSON.stringify(unit_dict))
          .then(function(resp){
            resp.data.forEach(function(record){
              that.student_unit_details.push({
                'pin' : record.pin,
                'student_name': record.student_name,
                'year_sem':record.year_sem,
                'marks': record.marks,
              })
            })
            that.btnLoading = false
            console.log(that.student_unit_details)
          })
      } else {
        that.$q.notify({color: 'negative', textColor: 'white', message: 'Please select the Required Fields', position: 'center', timeout: 1000 })
      }
    },
    send_attendence_details (){
      var that = this
      that.student_unit_details[0]['subject'] = that.subject
      that.student_unit_details[0]['unit_exam'] = that.unit_exam
      that.student_unit_details[0]['total_marks'] = that.total_marks
      console.log(that.student_unit_details)
      axios.post(baseUrlForBackend+'govweb/unit_marks_update/',JSON.stringify(that.student_unit_details))
      .then(function(resp){
        let respdata = resp.data
        that.$q.notify({color: 'green', textColor: 'white', message:respdata, position: 'center', timeout: 1000})
        console.log(respdata)
      })
    },
  }
}
</script>

<style>
</style>
