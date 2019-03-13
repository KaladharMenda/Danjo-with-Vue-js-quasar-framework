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
      </div>
       <q-table
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
         <q-td>
           <q-btn color="green"  @click="editUserData(props.row)" class="q-mr-xs">
           <span class="otp_fs">RELEASE</span>
         </q-btn>
         </q-td>
       </q-tr>
      </q-table>

      <q-modal v-model="userModalAdd" no-backdrop-dismiss :content-css="{minWidth: '75vw'}">
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
                 <!-- <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
                   <q-field>
                     <q-input class="input-field inline_s" type="text" :readonly="readonly" v-model="emailId" float-label="EmailId *" />
                     <div v-if="emailIdErrorMsg" class="first_s">
                        Please Enter the Email Id.
                     </div>
                   </q-field>
                 </div> -->
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
      </q-modal>
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
      name: '',
      usertype: '',
      groupOptions: [{'label': 'G1 - Teachers', 'value': 'G1'},{'label': 'G2 - HOD & Principal', 'value': 'G2'}],
      btnLoading: false,
      LocationErrorMsg: false,
      tableData: [],
      loading: false,
      separator: 'cell',
      filter: '',
      userModalAdd: false,
      firstName: '',
      firstNameErrorMsg: false,
      emailId: '',
      emailIdErrorMsg: false,
      UserId: '',
      UserIdErrorMsg: false,
      Password: '',
      passwordErrorMsg: false,
      GroupId:'',
      groupidErrorMsg : false,
      readonly: false,
      checkStatus: true,
      checkStatusForAdmin: false,
      dropDownRole: '',
      roleErrorMsg: false,
      disableSbtn: false,
      addUserDiv: false,
      editUserDiv: false,
      userKey: '',
      number: '',
      spinner: false,
      userId: '',
      editAdminInfo: true,
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
          name: 'student_name',
          required: true,
          label: 'Name',
          align: 'center',
          field: 'student_name',
          sortable: true,
          descending: false
        },
        {
          name: 'branch',
          required: true,
          label: 'Branch',
          align: 'center',
          field: 'branch',
          sortable: true,
          descending: false
        },
        {
          name: 'year_sem',
          required: true,
          label: 'Semester',
          align: 'center',
          field: 'year_sem',
          sortable: true,
          descending: false
        },
        {
          name: 'scheme_code',
          required: true,
          label: 'Scheme',
          align: 'center',
          field: 'scheme_code',
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
    that.updateDataTable()
  },
  methods: {
    updateDataTable () {
      var that = this
      that.loading = true
      that.tableData.length = 0
      // axios.get( baseUrlForBackend+'/rest_api/app_shipment_info_data/?manifest_number=448983599/1').then(function(result){
      //   console.log(result)
      //   debugger
      // })
      firebase.database().ref('UserDetails').once('value', function(snapshot) {
        snapshot.forEach(function(childSnapshot) {
          if (childSnapshot.val().usertype != 'Admin') {
            that.tableData.push({
              'userName': childSnapshot.val().name,
              'role' : childSnapshot.val().usertype,
            })
          }
        })
        that.tableData.reverse()
        that.loading = false
      })
    },
    getLocationID () {
      var that = this
      that.enterSelectOptions = []
      let locationNames = firebase.database().ref('Locations');
      locationNames.once('value', function (snapshot) {
        that.enterSelectOptions = []
        snapshot.forEach(function (child) {
          var temp = child.key
          that.allLocations[child.key] = child.val()
          that.enterSelectOptions.push({
            'label': child.val().name,
            'value': temp
          })
        })
      })
    },
    addUser () {
      var that = this
      that.addUserDiv = true
      that.userModalAdd = true
      setTimeout(function () {
        that.$refs.firstName.focus()
      }, 400)
    },
    editUserData (row) {
      var that = this
      that.readonly = true
      that.editUserDiv = true
      that.userModalAdd = true
      var date = new Date().getTime()
      firebase.database().ref('UserDetails/' + row.userName).once('value', function(childSnapshot) {
        that.checkStatusForAdmin = true
        that.firstName = childSnapshot.val().name
        that.Password = childSnapshot.val().password
        that.GroupId = childSnapshot.val().usertype
        that.checkStatus = childSnapshot.val().is_active
      })
    },
    submitUserData () {
      var that = this
      if (that.addUserDiv === true) {
        that.addUserFunction()
      }
      if (that.editUserDiv === true) {
        that.editUserFunction()
      }
    },
    editUserFunction () {
      var that = this
      that.btnLoading = true
      if (that.validationForUserData()) {
        var userDataToInsert = {
          'name': that.firstName,
          'password': that.Password,
          'usertype' : that.GroupId,
          'is_active': that.checkStatus,
          'created_at':new Date().getTime()
        }
        firebase.database().ref('UserDetails/' + that.firstName).update(userDataToInsert).then(function (){
          that.userModalAdd = false
          that.$q.notify({
            color: 'green',
            textColor: 'white',
            message: "Data has been updated succussfully",
            position: 'bottom-right',
            timeout: 3000
          })
          that.updateDataTable()
          that.emtpyAllFields()
          that.btnLoading = false
          }).catch(function (err){
            that.$q.notify({
              color: 'black',
              textColor: 'white',
              message: "Data couldn't be saved.Please try again later.",
              position: 'bottom-left',
              timeout: 3000
            })
          that.emtpyAllFields()
          that.btnLoading = false
        })
      }
      that.btnLoading = false
    },
    addUserFunction() {
      var that = this
      that.btnLoading = true
      that.savedUId = ''
      if (that.validationForUserData()) {
        var name = that.firstName;
        // var email = that.emailId;
        var password = that.Password;
        var usertype = that.GroupId;
        var user_obj = {
          'name': name,
          'password': password,
          'usertype' : usertype,
          'is_active' : true,
          'created_at':new Date().getTime()
        }
        if (user_obj) {
          firebase.database().ref('UserDetails').child(name).set(user_obj).then(function(response){
            that.btnLoading = false
            that.showNotify("User added successfully.")
            that.updateDataTable()
            that.closePopUp()
            that.btnLoading = false
          }).catch(function(error) {
            // Handle Errors here.
            var errorCode = error.code;
            var errorMessage = error.message;
            that.showNotify(error.message)
            that.btnLoading = false
          });
        }
      } else{
        that.btnLoading = false
      }
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
    validationForUserData () {
      if (this.firstName === '') {
        this.firstNameErrorMsg = true
        return false
      } else {
        this.firstNameErrorMsg = false
      }
      // if (this.emailId === '') {
      //   this.emailIdErrorMsg = true
      //   return false
      // } else {
      //   this.emailIdErrorMsg = false
      // }
      if (this.Password === '') {
        this.passwordErrorMsg = true
        return false
      } else {
        this.passwordErrorMsg = false
      }
      if (this.GroupId === '') {
        this.groupidErrorMsg = true
        return false
      } else {
        this.groupidErrorMsg = false
      }
      return true
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
