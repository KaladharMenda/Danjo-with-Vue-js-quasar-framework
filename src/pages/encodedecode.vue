<template>
  <div class="About">
    <q-card class="bg-white card-styl" style="padding:0px;">
      <q-tabs animated swipeable inverted color="secondary" underline-color= "secondary" align="justify">
        <q-tab default name="exam1" slot="title" label="EN - CODE" @click="emtpyAllFields('ss1')"/>
        <q-tab name="exam2" slot="title" label="DE - CODE" @click="get_decode_data('ss2')"/>
        <q-tab-pane name="exam1">
          <div class="row gutter-sm q-mb-md">
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5">
              <q-field>
                <q-select
                  v-model="semId"
                  :options="semOptions"
                  float-label="Semester *"
                  @input="getSubjectsData"
                />
              </q-field>
            </div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5" v-if="semId">
              <q-select
                v-model="subId"
                :options="subjectDropdownOpts"
                float-label="Subject *"
                @input="getUsersData"
              />
            </div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5" v-if="subId">
              <q-select
                v-model="studentIDs"
                :options="semOptionss"
                float-label="Select Student *"
                filter
                @input="enableScanDiv"
              />
            </div>
          </div>
          <div class="row">
            <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12"></div>
            <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" v-if = "semId && subId && studentIDs">
              <q-field>
                 <q-input type="text" id="scanFocus" ref="scannedItem" v-model="scannedItem" v-on:keyup.enter="checkBinType" float-label="Scan Sem Paper BarCode *"/>
              </q-field>
            </div>
            <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12"></div>
          </div>
        </q-tab-pane>
        <q-tab-pane name="exam2">
          <div class="row gutter-sm q-mb-md">
            <div class="col-lg-4 col-md-4"></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5">
              <q-field v-if="!enableEditDiv">
                 <q-input type="text" ref="scannedItemDecode" v-model="scannedItemDecode" v-on:keyup.enter="checkBinTypeA" float-label="Scan Sem Paper BarCode *"/>
              </q-field>
              <q-chip v-if="enableEditDiv" avatar="statics/boy-avatar.png" small color="teal" align="center">{{  scannedItemDecode}}</q-chip>
            </div>
            <div class="col-lg-4 col-md-4"></div>
          </div>
          <div class="row" v-if= "enableEditDiv">
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 scannedItemTop"></div>
              <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12 scannedItemTop">
                <q-field>
                   <q-input
                      type="text"
                      v-model="subjectMarks"
                      ref="subjectMarks"
                      float-label="Enter the Subject Marks"
                      />
                  </q-field>
                  <q-btn class="toolgreen" style="width:100%;color: aliceblue;" label="Update Sem Subject Marks" @click="updatemarks()"/>
              </div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"></div>
          </div>
          <div class="row" v-if="enableEditDiv">
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">
              <table class="q-table">
                <tr>
                  <th class="text-left">Year / Semester:</th>
                  <td class="text-right">II</td>
                </tr>
                <tr>
                  <th class="text-left">Subject:</th>
                  <td class="text-right">Engineering Physics</td>
                </tr>
                <tr>
                  <th class="text-left">Student PIN:</th>
                  <td class="text-right">14341a0598</td>
                </tr>
                <tr>
                  <th class="text-left">Sem paper Barcode ID:</th>
                  <td class="text-right">{{scannedItemDecode}}</td>
                </tr>
                <tr>
                  <th class="text-left">Marks Posted By:</th>
                  <td class="text-right">User Name</td>
                </tr>
              </table>
            </div>
          </div>
        </q-tab-pane>
      </q-tabs>
    </q-card>
  </div>
</template>

<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-firestore.js"></script>
<script>
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
  QInnerLoading,
  QSpinnerGears,
  QToggle
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
    QInnerLoading,
    QSpinnerGears,
    QToggle
  },
  data () {
    return {
      semId: '',
      subId: '',
      scannedItemDecode: '',
      tempsessionvalue:'',
      studentMark: '',
      studentIDs: '',
      sessionvalue : 'ss1',
      loader: false,
      loading: false,
      tempvalue: '',
      userModalAdd: false,
      ediTablEnable: false,
      enableEditDiv: false,
      scannedItem: '',
      subjectMarks: '',
      subjectDropdownOpts: [],
      studentmarkdetails: [],
      semOptions: [{'label': 'I', 'value': 'I'},{'label': 'II', 'value': 'II'},{'label': 'III', 'value': 'III'},{'label': 'IV', 'value': 'IV'},{'label': 'V', 'value': 'V'},{'label': 'VI', 'value': 'VI'},{'label': 'VII', 'value': 'VII'}],
      semOptionss: [{'label': '14341a0598', 'value': '14341a0598'},{'label': '14341a0599', 'value': '14341a0599'},{'label': '14341a05100', 'value': '14341a05100'},{'label': '14341a05101', 'value': '14341a05101'}],
      tab: 'exam1'
    }
  },
   mounted () {
    // if(localStorage.getItem('userId') !== '') {
    //   this.$router.push('/admin/Transactions')
    // }
  },
  created () {
    var that = this
    // that.updateDataTable()
    // that.getWarehouseDetails ()
  },
  methods: {
    updatemarks () {
      var that = this
      if (that.subjectMarks) {
        that.emtpyAllFields('ss2')
        that.$q.notify({color: 'positive', textColor: 'white', message: 'Successfully Updated Subject Marks', position: 'center', timeout: 1000 })
        setTimeout(function(){
          that.$refs.scannedItemDecode.focus()
        }, 500)
      } else {
        that.$q.notify({color: 'negative', textColor: 'white', message: 'please Enter Subject Marks', position: 'center', timeout: 1000 })
        that.$refs.subjectMarks.focus()
      }
    },
    get_decode_data () {
      var that = this
      that.emtpyAllFields('ss2')
      setTimeout(function(){
        that.$refs.scannedItemDecode.focus()
      }, 500)
    },
    enableScanDiv () {
      var that = this
      setTimeout(function(){
        that.$refs.scannedItem.focus()
      }, 500)
    },
    checkBinType (e) {
      let that = this
      that.$q.notify({color: 'positive', textColor: 'white', message: 'Successfully Added Barcode Number', position: 'center', timeout: 1000 })
      that.emtpyAllFields('ss1')
    },
    checkBinTypeA (e) {
      let that = this
      that.enableEditDiv = true
      setTimeout(function(){
        that.$refs.subjectMarks.focus()
      }, 500)
      // that.$q.notify({color: 'positive', textColor: 'white', message: 'Successfully Added Barcode Number', position: 'center', timeout: 1000 })
      // that.emtpyAllFields()
    },
    getSubjectsData () {
      var that = this
      that.subjectDropdownOpts = []
      firebase.database().ref('subjects/'+ that.semId).once('value', function(snapshot) {
        snapshot.forEach(function (child) {
          // if (child.val().active === true) {
          that.subjectDropdownOpts.push({
            'label': child.key,
            'value': child.key,
          })
          // }
        })
      })
    },
    enableresultsdiv () {
      let that = this
      that.userModalAdd = true
      if (that.sessionvalue == 'ss1'){
        that.tempsessionvalue = 'SessionExam 1'
      } else if (that.sessionvalue == 'ss2') {
        that.tempsessionvalue = 'SessionExam 2'
      }
    },
    savetofirebase () {
      let that = this
      that.loading = true
      console.log(that.studentmarkdetails)
      if (that.subId && that.semId && that.sessionvalue) {
        that.studentmarkdetails.forEach(function(data){
          let key = that.subId
          let dataToInsert = {
            [key]: data.marked
          }
          firebase.database().ref('StudentsMarks/'+data.studentid +'/'+that.semId +'/'+that.sessionvalue).update(dataToInsert)
        })
        that.emtpyAllFields(that.sessionvalue)
        that.loading = false
      } else {
        that.showNotify('Required data Missing, Please Try Again !!')
      }
    },
    getUsersData () {
      var that = this
      that.loader = true
      if(that.semId != '' && that.subId != '') {
        that.studentmarkdetails =[]
        firebase.database().ref('StudentDetails').once('value', function(snapshot) {
          snapshot.forEach(function (child) {
            that.studentmarkdetails.push({
              'studentid':child.key,
            });
          })
          that.loader = false
        })
      } else {
        that.showNotify('please select SEMESTER & SUBJECT')
      }
    },
    getTimeFormat (curDate) {
      if (curDate !=0 && curDate != '') {
        var d = new Date(curDate)
      var currDate = String(d.getDate())
      var currMonth = String(d.getMonth())
      var currYear = String(d.getFullYear())
      var currHour = String(d.getHours())
      var currMinutes = String(d.getMinutes())
      var currSeconds = String(d.getSeconds())
      currMonth = Number(currMonth) + 1
      var joinTime = currDate + '/' + currMonth + '/' + currYear + ' ' + currHour + ':' + currMinutes + ':' + currSeconds
      return joinTime
      } else {
        return joinTime = 'NA';
      }
    },
    emtpyAllFields (val) {
      var that = this
      that.sessionvalue = val
      that.userModalAdd = false
      that.semId = ''
      that.subId = ''
      that.scannedItemDecode = ''
      that.scannedItem = ''
      that.studentIDs = ''
      that.loader = false
      that.loading = false
      that.subjectMarks = ''
      that.enableEditDiv = false
      that.ediTablEnable = false
      that.subjectDropdownOpts = []
      that.studentmarkdetails = []
      that.tempsessionvalue = ''
      console.log(that.sessionvalue)
    },
    // ontogochange () {
    //   let that = this
    //   console.log(that.studentmarkdetails)
    // },
    closePopUp () {
      var that = this
      that.userModalAdd = false
      // that.emtpyAllFields()
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
    }
  }
}
</script>

<style lang="stylus">
.docs-tab-pane
  .q-tab-pane
    display flex
    align-items center
    justify-content center
    height 65px
</style>
