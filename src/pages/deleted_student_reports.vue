<template>
  <div class="About">
    <q-card class="bg-white card-styl">
     <div class="loader" v-if="spinner"></div>
     <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12" align="center">
       <q-toolbar color="orange" class="toolblue">
         <q-toolbar-title>
           <b>Deleted Student List</b>
         </q-toolbar-title>
       </q-toolbar>
     </div>
      <div class="row">
        <div class="col-lg-4 col-md-4"></div>
        <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
          <q-field>
            <q-select
              v-model="year_sem"
              :options="year_semOptions"
              float-label="Year / Semester"
              @input="getSubjects_scheme_Data"
            />
          </q-field>
        </div>
      </div>
       <q-table
         v-if = "enable_division"
         :data="tableData"
         title="Deleted Students List"
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
         <!-- <q-td>
           <q-btn color="green"  @click="editUserData(props.row)" class="q-mr-xs">
           <span class="otp_fs">RELEASE</span>
         </q-btn>
         </q-td> -->
       </q-tr>
      </q-table>

      <!-- <q-modal v-model="userModalAdd" no-backdrop-dismiss :content-css="{minWidth: '75vw'}">
        <q-modal-layout>
          <q-toolbar slot="header" class="bg-secondary">
            <q-toolbar-title v-if="addUserDiv">
              Add New User
            </q-toolbar-title>
            <q-toolbar-title v-if="editUserDiv">
              Edit User
            </q-toolbar-title>
            <q-btn
              flat
              round
              dense
              @click="closePopUp()"
              icon="close"
              style="float:right"
            />
          </q-toolbar>
          <div class="q-pa-lg">
            <div class="row gutter-sm q-mb-md">
              <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                   <q-field>
                     <q-input  type="text" :readonly="readonly" ref="firstName" v-model="firstName" float-label="Name *"/>
                     <div v-if="firstNameErrorMsg" class="first_s">
                        Please Enter Your Name.
                      </div>
                  </q-field>
                 </div>
                 <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                 <q-field>
                     <q-input class="input-field inline_s" type="text" v-model="Password" float-label="Password *"/>
                    <div v-if="passwordErrorMsg" class="first_s">
                       Please Enter Password.
                    </div>
                  </q-field>
               </div>
               <div class="col-lg-4 col-md-4 col-sm-12 col-xs-12">
                 <q-field>
                    <q-select
                      v-model="GroupId"
                      :options="groupOptions"
                      stack-label="GroupId *"
                    />
                    <div v-if="groupidErrorMsg" class="first_s">
                       Please Enter groupID.
                    </div>
                  </q-field>
               </div>
            </div>
            <div class="row justify-end q-mt-md">
              <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6" v-if="checkStatusForAdmin" style="padding-top: 4px;align-self: center;">
                <q-toggle v-model="checkStatus" color="green" label="Active" left-label />
              </div>
               <div class="col-lg-3 col-md-3 col-sm-6 col-xs-6">
                   <q-btn class="full-width otp_send" :disabled="btnLoading" @click="submitUserData()">
                     <span class="otp_fs">SUBMIT</span>
                   </q-btn>
            </div>
             </div>
          </div>
        </q-modal-layout>
      </q-modal> -->
    </q-card>
  </div>
</template>

<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-auth.js"></script>
<script src="https://www.gstatic.com/firebasejs/5.0.4/firebase-database.js"></script>
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
      year_sem: '',
      name: '',
      usertype: '',
      year_semOptions: [{'label': '1YR', 'value': '1YR'},{'label': '2YR', 'value': '2YR'},{'label': '3SEM', 'value': '3SEM'},{'label': '4SEM', 'value': '4SEM'},{'label': '5SEM', 'value': '5SEM'},{'label': '6SEM', 'value': '6SEM'},{'label': '7SEM', 'value': '7SEM'},{'label': '8SEM', 'value': '8SEM'}],
      btnLoading: false,
      LocationErrorMsg: false,
      tableData: [],
      loading: false,
      separator: 'cell',
      filter: '',
      userKey: '',
      number: '',
      spinner: false,
      userId: '',
      editAdminInfo: true,
      enable_division: false,
      columns: [
        {
          name: 'pin',
          required: true,
          label: 'Pin Number',
          align: 'center',
          field: 'pin',
          sortable: true,
          descending: false
        },
        {
          name: 'username',
          required: true,
          label: 'Student Name',
          align: 'center',
          field: 'username',
          sortable: true,
          descending: false
        },
        {
          name: 'gender',
          required: true,
          label: 'Gender',
          align: 'center',
          field: 'gender',
          sortable: true,
          descending: false
        }
      ]
    }
  },
   mounted () {
  },
  created () {
    var that = this
  },
  methods: {
    getSubjects_scheme_Data () {
      var that = this
      that.loading = true
      that.tableData = []
      var sem_obj = {
        'sem': that.year_sem
      }
      axios.post(baseUrlForBackend+'govweb/get_deleted_students/', JSON.stringify(sem_obj))
      .then(function(resp){
        if ((resp.data != 'fail' && resp.data != 'Some thing went wrong') && resp.data) {
          resp.data.forEach(function(item){
            that.enable_division = true
            that.tableData.push({
              'pin': item.pin,
              'username': item.username,
              'gender': item.gender
            })
          });
        } else if(resp.data == 'Some thing went wrong') {
          that.showNotify(resp.data)
        } else {
          that.showNotify('No Records')
        }
        that.loading = false
      })
    },
    closePopUp () {
      var that = this
      that.emtpyAllFields()
      that.userModalAdd = false
    },
    emtpyAllFields () {
      var that = this
      that.firstName = ''
      that.name = ''
      that.usertype = ''
      that.emailId = ''
      that.UserId = ''
      that.Password = ''
      that.GroupId = ''
      that.groupidErrorMsg = false
      that.passwordErrorMsg = false
      that.firstNameErrorMsg = false
      that.emailIdErrorMsg = false
      that.addUserDiv = false
      that.btnLoading = false
      that.editUserDiv = false
      that.checkStatusForAdmin = false
      that.readonly = false
      that.disabled = false
    },
    showNotify (msg) {
      let that = this
      that.$q.notify({
        color: 'green',
        textColor: 'white',
        message: msg,
        position: 'bottom-right',
        timeout: 3000
      })
    }
  }
}
</script>

<style>
</style>
