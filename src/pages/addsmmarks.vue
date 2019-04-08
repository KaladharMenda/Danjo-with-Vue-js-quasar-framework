<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolgradientgreen">
          <q-toolbar-title>
            <b>Add SM Marks For Students</b>
          </q-toolbar-title>
        </q-toolbar>
      </div>
      <div class="row gutter-sm" style="margin-top: 0px;">
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="scheme_code"
              :options="scheme_code_options"
              float-label="SCHEME CODE"
            />
          </q-field>
        </div>
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
              v-model="subject"
              :options="subject_options"
              float-label="SECTION"
            />
          </q-field>
        </div>
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6" align="center">
          <q-btn color="purple" icon-right="send" @click="get_student_details()" :disabled="btnLoading" style="background: #ff9e10 !important;">
            <q-spinner-hourglass v-if="btnLoading" class="on-left"/>
            GET STUDENT DETAILS
          </q-btn>
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
      scheme_code: '',
      year_sem: '',
      subject: '',
      total_marks: '',
      year_sem_options: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'}],
      scheme_code_options: [{'label': 'C05', 'value': 'C05'},{'label': 'C09', 'value': 'C09'},{'label': 'C014', 'value': 'C014'},{'label': 'C016', 'value': 'C016'},{'label': 'ER91', 'value': 'ER91'}],
      subject_options: [{'label': '1', 'value': '1'},{'label': '2', 'value': '2'}],
      btnLoading: false,
      student_sm_details :[],
    }
  },
  created () {
    var that = this
  },
  methods: {
    get_student_details () {
      var that = this
      var sm_dict = {}
      if (that.scheme_code != '' && that.year_sem != '' && that.subject != '') {
        sm_dict ['year_sem'] = that.year_sem
        sm_dict['scheme_code'] = that.scheme_code
        sm_dict ['subject'] = that.subject
        axios.post(baseUrlForBackend+'govweb/get_sm_marks/',JSON.stringify(sm_dict))
        .then(function(resp){
          resp.data.forEach(function(record){
            that.student_sm_details.push({
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
    },
}
</script>

<style>
</style>
