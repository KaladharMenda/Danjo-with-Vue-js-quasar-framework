<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
        <q-toolbar color="orange" class="toolblue">
          <q-toolbar-title>
            <b>Attendance Details</b>
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
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-input  type="text" v-model="month" float-label="MONTH " readonly/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6">
          <q-field>
            <q-select
              v-model="period"
              :options="period_options"
              float-label="PERIOD"
            />
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-6" style="margin-top: -16px;">
          <q-field>
            <q-input  type="text" v-model="working_days" float-label="TOTAL COLLEGE WORKING DAYS"/>
          </q-field>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-5 col-xs-12" align="center">
          <q-btn color="purple" @click="checkpinexists()" :disabled="btnLoading">
            <q-spinner-hourglass v-if="btnLoading" class="on-left" />
            Verify and update
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
      month: '',
      year_sem: '',
      period: '',
      year_sem_options: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'}],
      period_options: [{'label': '1st to 15 Days', 'value': 'first_period'},{'label': '16th to Month End', 'value': 'second_period'}],
      btnLoading: false,
      working_days: ''
    }
  },
  created () {
    var that = this
    that.convertDate(new Date().getMonth())
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
    checkpinexists () {
      let that = this
      that.btnLoading = true
      setTimeout(function () {
        that.btnLoading = false
      },2000)
      that.alldivisionenable = true
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
