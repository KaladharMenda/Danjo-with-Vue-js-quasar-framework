<template>
  <div class="About">
    <q-card class="bg-white card-styl" style="padding:0px;">
      <q-tabs animated swipeable inverted color="secondary" underline-color= "secondary" align="justify">
        <q-tab default name="exam1" slot="title" label="Session - Exam - I" @click="emtpyAllFields('ss1')"/>
        <q-tab name="exam2" slot="title" label="Session - Exam - II" @click="emtpyAllFields('ss2')"/>
        <q-tab name="exam3" slot="title" label="Session - Exam - III" @click="emtpyAllFields('ss3')"/>
        <q-tab-pane name="exam1">
          <div class="row gutter-sm q-mb-md">
            <div class="col-lg-2 col-md-2"></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5">
              <q-field>
                <q-select
                  v-model="semId"
                  :options="semOptions"
                  stack-label="Semester *"
                  @input="getSubjectsData"
                />
              </q-field>
            </div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5" v-if="semId">
              <q-select
                v-model="subId"
                :options="subjectDropdownOpts"
                stack-label="Subject *"
                @input="getUsersData"
              />
            </div>
            <div class="col-lg-2 col-md-2"></div>
          </div>
        </q-tab-pane>
        <q-tab-pane name="exam2">
          <div class="row gutter-sm q-mb-md">
            <div class="col-lg-2 col-md-2"></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5">
              <q-field>
                <q-select
                  v-model="semId"
                  :options="semOptions"
                  stack-label="Semester *"
                  @input="getSubjectsData"
                />
              </q-field>
            </div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5" v-if="semId">
              <q-select
                v-model="subId"
                :options="subjectDropdownOpts"
                stack-label="Subject *"
                @input="getUsersData"
              />
            </div>
            <div class="col-lg-2 col-md-2"></div>
          </div>
        </q-tab-pane>
        <q-tab-pane name="exam3">
          <div class="row gutter-sm q-mb-md">
            <div class="col-lg-2 col-md-2"></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5">
              <q-field>
                <q-select
                  v-model="semId"
                  :options="semOptions"
                  stack-label="Semester *"
                  @input="getSubjectsData"
                />
              </q-field>
            </div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-xs-5" v-if="semId">
              <q-select
                v-model="subId"
                :options="subjectDropdownOpts"
                stack-label="Subject *"
                @input="getUsersData"
              />
            </div>
            <div class="col-lg-2 col-md-2"></div>
          </div>
        </q-tab-pane>
      </q-tabs>
      <div class="row" v-if = 'loader'>
        <div class="col-lg-4 col-md-4"></div>
        <div class="col-lg-4 col-md-4 col-sm-4 col-xs-12" align="center">
          <span class="secondary"><q-spinner-gears size="30px" color="secondary"></q-spinner-gears>   Processing ....</span>
        </div>
        <div class="col-lg-4 col-md-4"></div>
      </div>
      <div class="row" v-if = 'ediTablEnable'>
        <table class="q-table responsive">
          <thead>
            <tr>
              <th style="font-family: sans-serif;"><b>STUDENT ID</b></th>
              <th style="font-family: sans-serif;"><b>ENTER THE MARKS</b></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(data ,index) in studentmarkdetails" :key="index">
              <td class="text-center" data-th="STUDENT ID">{{ data.studentid }}</td>
              <td>
                <q-field>
                  <q-input  type="text" v-model="data.marked"/>
                </q-field>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="row" v-if = 'ediTablEnable'>
        <div class="col-lg-4 col-md-4"></div>
        <div class="col-lg-4 col-md-4 col-sm-4 col-xs-12" align="center">
          <q-btn class="info" icon-right="send" label="Verify and Save" @click="enableresultsdiv()"/>
        </div>
        <div class="col-lg-4 col-md-4"></div>
      </div>
      <q-modal v-model="userModalAdd" no-backdrop-dismiss no-esc-dismiss :content-css="{padding: '20px', minWidth: '75vw'}"
          >
          <div class="row">
            <q-chip avatar="statics/boy-avatar.png" small color="teal" align="center">{{tempsessionvalue}} - {{semId}} - {{subId}}</q-chip>
            <div class="col" align="right">
              <q-btn
              flat
              round
              dense
              @click="closePopUp()"
              icon="close"
              style="float:right"
            />
            </div>
          </div>
          <div class="row" v-if = 'loading'>
            <div class="col-lg-4 col-md-4"></div>
            <div class="col-lg-4 col-md-4 col-sm-4 col-xs-12" align="center">
              <span class="secondary"><q-spinner-gears size="30px" color="warning"></q-spinner-gears>   Processing ....</span>
            </div>
            <div class="col-lg-4 col-md-4"></div>
          </div>
          <div class="q-pa-lg">
            <div class="row gutter-sm q-mb-md">
              <table class="q-table responsive">
                <thead>
                  <tr>
                    <th style="font-family: sans-serif;"><b>STUDENT ID</b></th>
                    <th style="font-family: sans-serif;"><b>STUDENT MARKS</b></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(data ,index) in studentmarkdetails" :key="index">
                    <td class="text-center" data-th="STUDENT ID">{{ data.studentid }}</td>
                    <td class="text-center" data-th="STUDENT MARKS">{{ data.marked }}</td>
                  </tr>
                </tbody>
              </table>
           </div>
            <div class="row justify-center q-mt-md">
              <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
               <q-btn color="green" class="full-width" @click="savetofirebase()">
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
      tempsessionvalue:'',
      studentMark: '',
      sessionvalue : 'ss1',
      loader: false,
      loading: false,
      userModalAdd: false,
      ediTablEnable: false,
      subjectDropdownOpts: [],
      studentmarkdetails: [],
      semOptions: [{'label': 'I', 'value': 'I'},{'label': 'II', 'value': 'II'},{'label': 'III', 'value': 'III'},{'label': 'IV', 'value': 'IV'},{'label': 'V', 'value': 'V'},{'label': 'VI', 'value': 'VI'},{'label': 'VII', 'value': 'VII'}],
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
      } else if (that.tempsessionvalue = 'ss3') {
        that.tempsessionvalue = 'SessionExam 3'
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
              'marked':''
            });
          })
          that.ediTablEnable = true
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
      that.loader = false
      that.loading = false
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
