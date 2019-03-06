<template>
  <div class="About">
    <q-card class="bg-white card-styl">
      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6">
            <h3 class="inner_head_styl">Encode</h3>
        </div>
        <!-- <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6" align="right"> -->
            <!-- <q-btn @click="getDownloadData()" slot="right">Current Sorted Items</q-btn> -->
            <!-- <q-btn @click="getDownloadData(1)" slot="right">Globally Sorted Items</q-btn> -->
        <!-- </div> -->
      </div>
      <!-- <div class="row">
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12"></div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
          <q-field>
             <q-input type="text" id="scanFocus" ref="scannedItem" v-model="scannedItem" v-on:keyup="checkBinType" float-label="Scan Item *"/>
          </q-field>
          <div v-if="binType && saveScannedItem && !loading">
            <h1 v-bind:class="binClass" class="text-center big-font"><span class="small-font">{{ saveScannedItem }} &nbsp;&nbsp;:</span>&nbsp;&nbsp;{{ binType }}</h1>
          </div>
          <div class="text-center">
            <h5 class="text-negative" v-if="noItemErr && saveScannedItem && !loading">Scanned item not available</h5>
            <q-spinner color="green" v-if="loading" style="margin: 0 auto" size="40px" />
          </div>
        </div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12"></div>
      </div> -->
    </q-card>
  </div>
</template>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-database.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-firestore.js"></script>
<script>
import _ from 'lodash';
import axios from 'axios'
import {
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
      location:[],
      SettingsCollection: 'WareHouseSettings',
      dwnloadData: [],
      userModalAdd: true,
      loading: false,
      binType: '',
      scannedItem: '',
      totalVendors: {},
      topVendors: [],
      vendorLimit: 0,
      temp_vendor: '',
      noItemErr: false,
      saveScannedItem: '',
      binClass: '',
      userStat: '',
      htmlData: '',
      currentSort: [],
      VendorLimit: 0
    }
  },
  mounted () {
    let that = this
  },
  created () {
    var that = this
  },
  methods: {
    getVendorLimit () {
      var that = this
      if (that.$store.state.example.userName !== "") {
        window.app2.database().ref('WareHouseSettings/VendorLimit').on('value', function(vendors) {
          if (vendors.val()) {
            that.VendorLimit = vendors.val()
          }
          that.getAVendors()
        })
      } else {
        setTimeout(function(){
            that.getVendorLimit()
        },500)
      }
    },
    convertDate: function (date) {
      var myDate = new Date(date)
      var month = myDate.getMonth() + 1
      var day = myDate.getDate()
      var year = myDate.getFullYear()
      if (day < 10) {
        day = '0' + day
      }
      if (month < 10) {
        month = '0' + month
      }
      var formattedDate = day + '-' + month + '-' + year
      return formattedDate
    },
  }
}
</script>

<style>
</style>
