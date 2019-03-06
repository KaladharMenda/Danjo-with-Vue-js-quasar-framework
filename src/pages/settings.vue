<template>
  <div class="About">
    <q-card class="bg-white card-styl">
      <div class="row">
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12" align="left" style="margin-top: -35px;">
          <h3 class="inner_head_styl">Subjects</h3>
        </div>
        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12" align="right">
          <q-btn color="green" @click="addUser()" slot="right">Add Semester Subjects</q-btn>
        </div>
      </div>
      <div class="row col-lg-12 col-md-12 col-sm-12 col-xs-12" style="padding: 5px;">
        <div class="col-lg-3 col-md-3 col-sm-6 col-xs-12" v-for="(data, index) in location" :key="index" style="padding-right: 5px; padding-left: 5px;padding-top: 5px;">
          <div class=" bg-teal text-white" style="min-height: 215px;">
            <div class="card-title" align="center">
              SEMESTER :  {{ data.Semester}}
            </div>
            <hr>
            <div class="card-content" align="center" v-for="(datas, index) in data.subjects" :key="index">
              <span class="text-left q-mb-xs" style="font-size: 16px;align-content: flex-start;">{{datas}}</span><br>
            </div>
          </div>
        </div>
      </div>
      <q-modal v-model="userModalAdd" no-backdrop-dismiss no-esc-dismiss :content-css="{padding: '20px', minWidth: '75vw'}"
          >
          <div class="row">
            <h6 style="margin-top: 5px;">Add Semester Subjects</h6>
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
          <div class="q-pa-lg">
            <div class="row gutter-sm q-mb-md">
              <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12" style="margin-top: 6px;">
               <q-field>
                  <q-select
                    v-model="GroupId"
                    :options="groupOptions"
                    stack-label="Semester *"
                  />
                  <div v-if="groupidErrorMsg" class="first_s">
                     Please Select Semester.
                  </div>
                </q-field>
             </div>
              <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
               <q-field>
                  <q-input class="input-field inline_s" type="text" v-model="subjectName" float-label="Subject Name *"/>
                   <div v-if="locationErrorMsg" class="first_s">
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
    </q-card>
  </div>
</template>

<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.3.0/firebase-firestore.js"></script>
<script>
import { Dialog } from 'quasar'
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
    QToggle
  },
  data () {
    return {
      GroupId:'',
      groupidErrorMsg : false,
      groupOptions: [{'label': 'I', 'value': 'I'},{'label': 'II', 'value': 'II'},{'label': 'III', 'value': 'III'},{'label': 'IV', 'value': 'IV'},{'label': 'V', 'value': 'V'},{'label': 'VI', 'value': 'VI'},{'label': 'VII', 'value': 'VII'}],
      agreebtn: true,
      tempstatus: '',
      tempkey: '',
      deletedCount: 0,
      confirmDialog: false,
      subjectName: '',
      location:[],
      subjects:[],
      active :true,
      userModalAdd: false,
      addUserDiv: false,
      locationErrorMsg: false,
      filter: '',
      separator: 'cell',
      // tableData: [],
      columns: [
        {name: 'location', required: true, label: 'WarehouseLocation', align: 'left', field: 'location', sortable: true, descending: false},
        {name: 'active', label: 'Status', align: 'left', field: 'active', sortable: true}
      ]
    }
  },
   mounted () {
    // if(localStorage.getItem('userId') !== '') {
    //   this.$router.push('/admin/Transactions')
    // }
  },
  created () {
    var that = this
    that.getData()
  },
  methods: {
    addUser () {
      var that = this
      that.addUserDiv = true
      that.userModalAdd = true
    },
    getData () {
      var that = this;
      that.location = []
      firebase.database().ref('subjects').once('value', function(snapshot) {
        snapshot.forEach(function(doc) {
          that.subjects = []
          doc.forEach(function(data) {
            // debugger
            that.subjects.push(data.key)
          })
          that.location.push({
            'Semester':doc.key,
            'subjects':that.subjects
          })
        })
      })
    },
    closePopUp () {
      var that = this
      that.addUserDiv = false
      that.userModalAdd = false
      that.emtpyAllFields()
    },
    emtpyAllFields () {
      var that = this
      that.GroupId = ''
      that.groupidErrorMsg = false
      that.subjectName = ''
      that.locationErrorMsg = false
    },
    addLocationData () {
      var that = this;
      if (that.validationForUserData()) {
        var user_obj = {
            "name" : that.subjectName,
          }
        firebase.database().ref('subjects/' + that.GroupId + '/' + that.subjectName).update(user_obj).then(function(response){
            that.showNotify("Subject Added Successfully.")
            that.closePopUp()
            that.emtpyAllFields()
            that.getData()
        })
      }
    },
    validationForUserData () {
      let that = this;
      if (that.GroupId === '') {
        that.groupidErrorMsg = true
        return false
      } else {
        that.groupidErrorMsg = false
      }
      if (that.subjectName === '') {
        that.locationErrorMsg = true
        return false
      } else {
        that.locationErrorMsg = false
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
        timeout: 300
      })
    }
  }
}
</script>

<style>
</style>
