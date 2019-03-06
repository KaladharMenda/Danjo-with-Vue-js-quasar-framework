export function fetchUserType (context, userType) {
  context.commit('setUserType', userType)
}
export function fetchMasterDb (context, dbName) {
  context.commit('setMasterDB', dbName)
}
export function fetchMasterUrl (context, url) {
  context.commit('setMasterDBUrl', url)
}
export function fetchsecondrydb (context, secondrydb) {
  context.commit('setsecondrydb', secondrydb)
}

export function fetchUserEmail (context, secondrydb) {
  context.commit('setUserEmail', secondrydb)
}

export function fetchAdminKey (context, adminKey) {
  context.commit('setAdminKey', adminKey)
}

export function fetchUserPwd (context, userPwd) {
  context.commit('setUserPwd', userPwd)
}

export function fetchUserLocId (context, userLocId) {
  context.commit('setUserLocId', userLocId)
}

export function fetchUserName (context, userName) {
  context.commit('setUserName', userName)
}
// export function fetchMasterFbConfPageType (context, pageName) {
//   context.commit('setMasterFbConfPageType', pageName)
// }
// export function fetchFbConf (context, fbConf) {
//   context.commit('setFbConf', fbConf)
// }
