<template>
  <div class="PRINT PAGE-CONTENT" align="left" style="font-size: 15px;">
    <div class="row card-styl">
      <div>
       <i class="material-icons" style="font-size: 30px">
        <strong>
         <a class="floating-left" href="javascript:void(0)" @click="backtoCreateStn()">
           keyboard_backspace
         </a>
        </strong>
       </i>
      </div>
      <div class="col" align="right" style="padding-bottom: 10px;">
        <q-btn type='button' id='btn' color="primary" value='Print' @click="printDiv()">Print</q-btn>
      </div>
    </div>
    <div id='DivIdToPrint' class="bg-white" style="padding: 50px;">

      <table style="width: 100%;" border="0">
        <tr>
          <td align="center">
            <h4 style="margin: 0px; font-weight: 500">{{sourceCompanyName}}</h4>
            <span style="line-height: 1.8">{{sourceAddress}}</span>
          </td>
        </tr>
      </table>
      <hr>

      <div class="stn-details">
        <table style="width: 100%">
          <tr style="width: 100%">
            <td style="width: 50%">
              <strong>Name : </strong>
              <span>{{destCompanyName}}</span>
            </td>
            <td style="width: 50%;padding-left: 100px;">
              <strong style="line-height: 1.8">ST Number : </strong>
              <span style="padding-left: 20px;font-size: 15px;">{{stNumber}}</span>
            </td>
          </tr>
          <tr style="width: 100%">
            <td style="width: 50%;">
              <strong>Address : </strong>
              <span style="line-height: 2.4">{{destAddress}}</span>
            </td>
            <td style="width: 50%;padding-left: 100px;padding-top: 10px;">
              <strong>ST Date :</strong><span style="padding-left: 20px;font-size: 15px;">{{stDate}}</span><br><br>
              <strong>Total No.of Cartons :</strong><span style="padding-left: 20px;font-size: 15px;">{{totalCartons}}</span><br><br>
              <strong>Total No.of Items :</strong><span style="padding-left: 20px;font-size: 15px;">{{totalItems}}</span><br><br>
              <strong>Vehicle Number :</strong><span style="padding-left: 20px;font-size: 15px;">{{vehicleNo}}</span><br><br>
              <div v-if="$store.state.example.userType == 'Admin'">
              <strong>Status :</strong><span style="padding-left: 20px;font-size: 15px;">
                <q-select
                   v-model="status"
                   :options="statusOptions"
                   @input="changeStnStatus"
                />
              </span><br><br>
              </div>
            </td>
          </tr>
        </table>
      </div>
      <br>
      <div class="carton-items-data">
        <table style="width: 100%; text-align: center;" border="1" cellspacing="0">
          <tr>
            <td style="border-top: 1px solid #666;padding: 10px;">S.No</td>
            <td style="border-top: 1px solid #666;padding: 10px;">Carton number</td>
            <td style="border-top: 1px solid #666;padding: 10px;">Items</td>
          </tr>
          <tr v-for="(carton, index) in cartonsList" :key="index">
            <td style="border-top: 1px solid #666;padding: 10px;">{{index + 1}}</td>
            <td style="border-top: 1px solid #666;padding: 10px;">{{carton.carton_number}}</td>
            <td style="border-top: 1px solid #666;padding: 10px;">{{carton.item}}</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript" src="https://www.baqend.com/js-sdk/latest/baqend-realtime.js"></script>
<script>
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
  QSearch
} from 'quasar'

export default {
  // name: 'ComponentName',
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
    QSearch
  },
  data () {
    return {
      stNumber: '',
      sourceAddress: '',
      destAddress: '',
      sourceCompanyName: '',
      destCompanyName: '',
      cartonsList: [],
      sourceCode: '',
      destCode:'',
      totalCartons: 0,
      totalItems: 0,
      stDate: '',
      count: 0,
      vehicleNo: '',
      status: '',
      statusOptions: [
        {'value':'Scan Pending','label':'Scan Pending'},
        {'value':'Partially Received','label':'Partially Received'},
        {'value':'Received','label':'Received'},
        {'value':'Dispatched','label':'Dispatched'},
        {'value':'Ready To Dispatch','label':'Ready To Dispatch'}
      ]

    }
  },
  created () {
    var that = this
    var stn = that.$route.params.stNo
    that.stNumber = stn
    firebase.auth().onAuthStateChanged(function(user) {
      if (!user) {
        that.$router.push('/')
      } else {
        firebase.database(app2).ref('UserDetails').once('value', function(response){
          response.forEach(function(userDetails){
            if (user.uid == userDetails.key) {
              if(userDetails.val()) {
                that.user = userDetails.val()
                that.Source = that.user.location_id
                console.log(that.user)
              }
            }
          })
        })
      }
    })
    setTimeout(function () {
      that.getDataForThisStn(stn)
      that.getCartonItemDetails(stn)
    } , 1000 )
  },
  methods: {
    changeStnStatus () {
      var that =this
      firebase.database(app2).ref('StnCartonItemData/'+that.Source+'/'+that.$route.params.stNo+'/status').set(that.status)
    },
    printDiv () {
      var divToPrint = document.getElementById('DivIdToPrint')
      var newWin = window.open('', 'Print-Window')
      newWin.document.open()
      newWin.document.write('<html><body onload = "window.print()">' + divToPrint.innerHTML + '</body></html>')
      newWin.document.close()
      setTimeout(function () { newWin.close() }, 10)
    },
    getDataForThisStn: function (stn) {
      var that = this
      axios.post(
                  baseUrlForBackend+'/stn/details',
                  {
                    'stn':stn,
                  }
      ).then(function(result) {
        that.status = result.data.status
        that.sourceCode = result.data.source
        that.destCode = result.data.destination
        that.stDate = that.convertDate(result.data.created_at)
        that.totalCartons = result.data.no_of_bags
        that.totalItems = result.data.no_of_items
        that.vehicleNo = result.data.vehicle_no
        that.getAddress(result.data.source,['sourceAddress','sourceCompanyName'])
        that.getAddress(result.data.destination,['destAddress','destCompanyName'])
        that.cartonsList = result.data.cartons
        // that.getSourceCodeCompany(result.val().source_code)
        // that.getDestCompanyName(result.destination_code)
      })
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
    getAddress: function (src,variable) {
      var that = this
      firebase.database().ref('Locations/'+src).on('value', function(result) {
          that[variable[0]] = result.val().Address
          that[variable[1]] = result.val().name
      })
    },
    getCartonItemDetails: function (stn) {
      var that = this
      firebase.database(app2).ref('StnCartonItemData/'+ that.Source + '/' + stn).on('value', function(result) {
        console.log(result.val())
        result.forEach(function(data){
          if (typeof(data.val()) === 'object') {
            that.cartonsList.push({
              'carton_number': data.key,
              'item': data.val().totalItems
            })
          }
        })
      })
    },
    backtoCreateStn: function () {
      // this.$router.push('../../createStn')
    }
  }
}
</script>

<style>
</style>
