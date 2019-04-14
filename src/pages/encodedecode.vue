<template>
  <div class="About">
    <q-card class="bg-white card-styl" style="padding:0px;">
      <q-tabs animated swipeable inverted color="secondary" underline-color= "secondary" align="justify">
        <q-tab default name="exam1" slot="title" label="SEM - SUBJECTS" @click="emtpyAllFields('ss1')"/>
        <q-tab name="exam2" slot="title" label="SEM - SCHEME CODE" @click="get_decode_data('ss2')"/>
        <q-tab-pane name="exam1">
          <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6" align="left">
            </div>
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6" align="right">
              <q-btn  round slot="right" color="primary" icon="add" @click="addsem_sub()"></q-btn>
            </div>
          </div>
          <div class="row gutter-sm q-mb-md">
            <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
              <q-field>
                <q-select
                  v-model="semId"
                  :options="semOptions"
                  float-label="Semester *"
                  @input="getSubjectsData"
                />
              </q-field>
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
          <q-table
              ng-if = "semId"
             :data="tableData"
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
             <q-td>
               <q-btn color="red" icon="delete" @click="deletesem_subject(props.row)" class="q-mr-xs" />
             </q-td>
           </q-tr>
          </q-table>
        </q-tab-pane>
        <q-tab-pane name="exam2">
          <div class="row">
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6" align="left">
            </div>
            <div class="col-lg-6 col-md-6 col-sm-6 col-xs-6" align="right">
              <q-btn  round slot="right" color="primary" icon="add" @click="addsem_scheme_code()"></q-btn>
            </div>
          </div>
          <div class="row gutter-sm q-mb-md">
            <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
              <q-field>
                <q-select
                  v-model="semIds"
                  :options="semOptions"
                  float-label="Semester *"
                  @input="getSchmesData"
                />
              </q-field>
            </div>
          </div>
          <q-table
             :data="tableData"
             :columns="columns1"
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
             <q-td>
               <q-btn color="red" icon="delete" @click="deletesem_schemeCode(props.row)" class="q-mr-xs" />
             </q-td>
           </q-tr>
          </q-table>
        </q-tab-pane>
      </q-tabs>
      <q-modal v-model="userModalAdd" no-backdrop-dismiss no-esc-dismiss :content-css="{padding: '20px', minWidth: '75vw'}"
          >
          <div class="row">
            <h6 style="margin-top: 5px;">Add Semester Subjects</h6>
            <div class="col" align="right">
              <q-btn
              flat
              round
              dense
              @click="closePopUps()"
              icon="close"
              style="float:right"
            />
            </div>
          </div>
          <div class="q-pa-lg">
            <div class="row gutter-sm q-mb-md">
              <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" style="margin-top: 6px;">
               <q-field>
                  <q-select
                    v-model="semIdp"
                    :options="semOptions"
                    float-label="Semester *"
                  />
                  <div v-if="semidpErrorMsg" class="first_s">
                     Please Select Semester.
                  </div>
                </q-field>
             </div>
              <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" style="margin-top: 6px;">
               <q-field>
                  <q-input class="input-field inline_s" type="text" v-model="subjectName" float-label="Subject Name *"/>
                   <div v-if="subjectErrorMsg" class="first_s">
                      Please Enter The Subject.
                   </div>
               </q-field>
             </div>
           </div>
            <div class="row justify-end q-mt-md">
              <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
               <q-btn color="green" class="full-width" @click="addLocationData()">
                 SUBMIT
               </q-btn>
              </div>
            </div>
          </div>
      </q-modal>
      <q-modal v-model="semSchemeCode" no-backdrop-dismiss no-esc-dismiss :content-css="{padding: '20px', minWidth: '75vw'}"
          >
          <div class="row">
            <h6 style="margin-top: 5px;">Add Semester Scheme Codes</h6>
            <div class="col" align="right">
              <q-btn
              flat
              round
              dense
              @click="closePopUps()"
              icon="close"
              style="float:right"
            />
            </div>
          </div>
          <div class="q-pa-lg">
            <div class="row gutter-sm q-mb-md">
              <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" style="margin-top: 6px;">
               <q-field>
                  <q-select
                    v-model="semIdpp"
                    :options="semOptions"
                    float-label="Semester *"
                  />
                  <div v-if="semidpErrorMsgs" class="first_s">
                     Please Select Semester.
                  </div>
                </q-field>
             </div>
              <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" style="margin-top: 6px;">
               <q-field>
                  <q-input class="input-field inline_s" type="text" v-model="schemeCode" float-label="Scheme Code *"/>
                   <div v-if="subjectErrorMsgs" class="first_s">
                      Please Enter The Scheme Code.
                   </div>
               </q-field>
             </div>
           </div>
            <div class="row justify-end q-mt-md">
              <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
               <q-btn color="green" class="full-width" @click="addLocationDatas()">
                 SUBMIT
               </q-btn>
              </div>
            </div>
          </div>
      </q-modal>
    </q-card>
  </div>
</template>

<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-firestore.js"></script>
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
      semIds: '',
      tableData: [],
      loading: false,
      separator: 'cell',
      filter: '',
      semIdp: '',
      semIdpp: '',
      subjectName: '',
      schemeCode: '',
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
      semSchemeCode: false,
      ediTablEnable: false,
      enableEditDiv: false,
      semidpErrorMsg: false,
      semidpErrorMsgs: false,
      subjectErrorMsg: false,
      subjectErrorMsgs: false,
      scannedItem: '',
      subjectMarks: '',
      subjectDropdownOpts: [],
      studentmarkdetails: [],
      columns: [
        {
          name: 'semester',
          required: true,
          label: 'SEMESTER',
          align: 'center',
          field: 'semester',
          sortable: true,
          descending: false
        },
        { name: 'subject', label: 'SUBJECT', align: 'center', field: 'subject', sortable: true }
      ],
      columns1: [
        {
          name: 'semester',
          required: true,
          label: 'SEMESTER',
          align: 'center',
          field: 'semester',
          sortable: true,
          descending: false
        },
        { name: 'scheme', label: 'SCHEME CODE', align: 'center', field: 'scheme', sortable: true }
      ],
      semOptions: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'},{'label': '8SEM', 'value': '8SEM'},{'label': 'PROJECT', 'value': 'PROJECT'}],
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
    addsem_sub (){
      var that = this
      that.userModalAdd = true
    },
    addsem_scheme_code (){
      var that = this
      that.semSchemeCode = true
    },
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
      that.loading = true
      that.tableData = []
      var sem_obj = {
        'sem': that.semId
      }
      axios.post(baseUrlForBackend+'govweb/get_sem_subjects/', JSON.stringify(sem_obj))
      .then(function(resp){
        if (resp.data != 'Subject Details Not Available for this Semester' && resp.data) {
          resp.data.forEach(function(item){
            that.tableData.push({
              'semester': item.semester,
              'subject' : item.subject,
            })
          });
        } else if(resp.data == 'Subject Details Not Available for this Semester') {
          that.showNotify(resp.data)
        } else {
          that.showNotify('something went Wrong !!!')
        }
        that.loading = false
      })
    },
    getSchmesData () {
      var that = this
      that.loading = true
      that.tableData = []
      var sem_obj = {
        'sem': that.semIds
      }
      axios.post(baseUrlForBackend+'govweb/get_sem_schemes/', JSON.stringify(sem_obj))
      .then(function(resp){
        if (resp.data != 'SchemeCode Details Not Available for this Semester' && resp.data) {
          resp.data.forEach(function(item){
            that.tableData.push({
              'semester': item.semester,
              'scheme' : item.scheme,
            })
          });
        } else if(resp.data == 'SchemeCode Details Not Available for this Semester') {
          that.showNotify(resp.data)
        } else {
          that.showNotify('something went Wrong !!!')
        }
        that.loading = false
      })
    },
    deletesem_subject (row) {
      var that = this
      var sem_obj = {
        'sem': row.semester,
        'subject' : row.subject
      }
      axios.post(baseUrlForBackend+'govweb/delete_sem_subjects/', JSON.stringify(sem_obj))
      .then(function(resp){
        if (resp.data == 'Deleted') {
          that.getSubjectsData()
          that.showNotify(resp.data)
        } else {
          that.showNotify(resp.data)
        }
      })
    },
    deletesem_schemeCode (row) {
      var that = this
      var sem_obj = {
        'sem': row.semester,
        'scheme' : row.scheme
      }
      axios.post(baseUrlForBackend+'govweb/delete_sem_scheme_code/', JSON.stringify(sem_obj))
      .then(function(resp){
        if (resp.data == 'Deleted') {
          that.getSchmesData()
          that.showNotify(resp.data)
        } else {
          that.showNotify(resp.data)
        }
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
      that.semIds = ''
      that.semIdp = ''
      that.semIdpp = ''
      that.schemeCode = ''
      that.tableData = []
      that.subjectName = ''
      that.sessionvalue = val
      that.userModalAdd = false
      that.semSchemeCode = false
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
      that.semidpErrorMsg = false
      that.subjectErrorMsg = false
      that.semidpErrorMsgs = false
      that.subjectErrorMsgs = false
      that.subjectDropdownOpts = []
      that.studentmarkdetails = []
      that.tempsessionvalue = ''
      // console.log(that.sessionvalue)
    },
    closePopUps () {
      var that = this
      that.emtpyAllFields()
    },
    addLocationData () {
      var that = this;
      if (that.validationForUserData()) {
        var sem_obj = {
          'sem': that.semIdp,
          "subject" : that.subjectName
        }
        axios.post(baseUrlForBackend+'govweb/update_sem_subjects/', JSON.stringify(sem_obj))
        .then(function(resp){
          if (resp.data == 'Success') {
            that.semIdp = ''
            that.subjectName = ''
            that.semidpErrorMsg = false
            that.subjectErrorMsg = false
            that.showNotify(resp.data)
          } else {
            that.showNotify(resp.data)
          }
        })
      }
    },
    addLocationDatas () {
      var that = this;
      if (that.validationForUserDatas()) {
        var sem_obj = {
          'sem': that.semIdpp,
          "scheme" : that.schemeCode
        }
        axios.post(baseUrlForBackend+'govweb/update_sem_scheme_code/', JSON.stringify(sem_obj))
        .then(function(resp){
          if (resp.data == 'Success') {
            that.semIdpp = ''
            that.schemeCode = ''
            that.semidpErrorMsgs = false
            that.subjectErrorMsgs = false
            that.showNotify(resp.data)
          } else {
            that.showNotify(resp.data)
          }
        })
      }
    },
    validationForUserData () {
      let that = this;
      if (that.semIdp === '') {
        that.semidpErrorMsg = true
        return false
      } else {
        that.semidpErrorMsg = false
      }
      if (that.subjectName === '') {
        that.subjectErrorMsg = true
        return false
      } else {
        that.subjectErrorMsg = false
      }
      return true
    },
    validationForUserDatas () {
      let that = this;
      if (that.semIdpp === '') {
        that.semidpErrorMsgs = true
        return false
      } else {
        that.semidpErrorMsgs = false
      }
      if (that.schemeCode === '') {
        that.subjectErrorMsgs = true
        return false
      } else {
        that.subjectErrorMsgs = false
      }
      return true
    },
    showNotify (msg) {
      let that = this
      that.$q.notify({
        color: 'green',
        textColor: 'white',
        message: msg,
        position: 'center',
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
