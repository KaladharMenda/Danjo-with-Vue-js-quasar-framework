<template>
  <div class="HOME PAGE-CONTENT">
    <q-card class="bg-white card-styl">
      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6" align="left">
          <h3>Student Data</h3>
        </div>
        <!-- <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6" align="right">
          <q-btn style="margin-right: 4px;" round slot="right" color="primary" icon="print" @click="printBarcodesforCartons()"></q-btn>
          <q-btn  round slot="right" color="primary" icon="add" @click="addStn()"></q-btn>
        </div> -->
      </div>
     <!--  <q-select
         v-if="false"
         v-model="tableStatus"
         :options="availableStatuses"
         stack-label="Status"
         @input="updateCreateCartonsDt"
      /> -->
      <q-table
        :data="tableData"
        :columns="columns"
        color="black"
        :filter="filter"
        :separator="separator"
        row-key="name"
        :loading="loading"
        @input="updateCreateCartonsDt"
      >
        <template slot="top-right" slot-scope="props">
          <q-search class="col-12" v-model="filter" />
        </template>
        <!-- <template slot="top-left" slot-scope="props">
          <q-btn icon="refresh" @click="updateCreateCartonsDt"/>
        </template> -->

        <q-tr slot="body" slot-scope="props" :props="props" @click.native="rowClick(props.row)" class="cursor-pointer">
          <q-td v-for="col in props.cols" :key="col.name" :props="props">
            {{ col.value }}
          </q-td>
          <q-td>
            <q-btn color="secondary" icon="visibility" @click="stnActionDeatils(props.row)" class="q-mr-xs" />
            <q-btn color="secondary" icon="info" @click="stnActionDeatilsInfo(props.row)" class="q-mr-xs" />
        </q-td>
        </q-tr>
      </q-table>
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
  QInnerLoading
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
    QInnerLoading
  },
  data () {
    return {
      tableData : [],
      separator: 'cell',
      filter: '',
      columns: [
        {
          name: 'id',
          required: true,
          label: 'Student Id',
          align: 'center',
          field: 'id',
          sortable: true,
          descending: false
        },
        { name: 'name', label: 'Student Name', align: 'center', field: 'name', sortable: true },
      ]
    }
  },
  created () {
    var that = this
    that.updateCreateCartonsDt()
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
    convertDate: function (date) {
      var myDate = new Date(date)
      var month = myDate.getMonth() + 1
      var day = myDate.getDate()
      var year = myDate.getFullYear()
      var hour = myDate.getHours()
      var minutes = myDate.getMinutes()
      var seconds = myDate.getSeconds()
      if (minutes < 10) {
        minutes = '0' + minutes
      }
      if (seconds < 10) {
        seconds = '0' + seconds
      }
      if (hour < 10) {
        hour = '0' + hour
      }
      if (day < 10) {
        day = '0' + day
      }
      if (month < 10) {
        month = '0' + month
      }
      var formattedTime =  hour + ':' + minutes + ':' + seconds
      var formattedDate =  month+ '-' + day + '-' + year + ' ' + formattedTime
      return formattedDate
    },
    convertNewDate: function (date) {
      var myDate = new Date(date)
      var month = myDate.getMonth() + 1
      var day = myDate.getDate()
      var year = myDate.getFullYear()
      var hour = myDate.getHours()
      var minutes = myDate.getMinutes()
      var seconds = myDate.getSeconds()
      if (minutes < 10) {
        minutes = '0' + minutes
      }
      if (seconds < 10) {
        seconds = '0' + seconds
      }
      if (hour < 10) {
        hour = '0' + hour
      }
      if (day < 10) {
        day = '0' + day
      }
      if (month < 10) {
        month = '0' + month
      }
      var formattedTime =  hour + ':' + minutes + ':' + seconds
      var formattedDate =  month+ '-' + day + '-' + year
      return formattedDate
    }
  }
}
</script>

<style>
.q-card {
  box-shadow: none;
}
.q-table-container {
  box-shadow: none;
}
.label {
  padding-right: 20px;
}
.modal input {
  height: 30px;
  padding: 5px;
}
.msg {
  font-size: 13px;
  color: #EB0019;
  padding-top: 5px;
}
.extra-cartons .q-input {
  border-bottom: 1px solid #ccc;
}
</style>
