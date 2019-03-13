function genericImport (page) {
  return import('pages/' + page + '.vue')
}

const routes = [
  {
    path: '/',
    component: () => import('layouts/flat_layout'),
    children: [
      { path: '', component: () => genericImport('login') }
    ]
  },
  {
    path: '/admin',
    component: () => import('layouts/MyLayout'),
    children: [
      { path: 'dashboard', component: () => genericImport('dashboard') },
      { path: 'Usermanagement', component: () => genericImport('Usermanagement') },
      { path: 'events', component: () => genericImport('events') },
      { path: 'addstudent', component: () => genericImport('addstudent') },
      { path: 'updatestudent', component: () => genericImport('updatestudent') },
      { path: 'transferstudent', component: () => genericImport('transferstudent') },
      { path: 'deletestudent', component: () => genericImport('deletestudent') },
      { path: 'addattendance', component: () => genericImport('addattendance') },
      { path: 'viewattendance', component: () => genericImport('viewattendance') },
      { path: 'sessionexams', component: () => genericImport('sessionexams') },
      { path: 'Encode', component: () => genericImport('Encode') },
      { path: 'Decode', component: () => genericImport('Decode') },
      { path: 'DeletedStudentsReport', component: () => genericImport('deleted_student_reports') },
      { path: 'smmarksreport', component: () => genericImport('smmarks_report') },
      { path: 'pmmarksreport', component: () => genericImport('pmmarks_report') },
      { path: 'settings', component: () => genericImport('settings') },
      { path: 'picking', component: () => genericImport('picking') },
      { path: 'flushCarton', component: () => genericImport('flushCarton') },
      { path: 'getgp', component: () => genericImport('getgp') },
      { path: 'masterbag', component: () => genericImport('masterbag') },
      { path: 'settings', component: () => genericImport('settings') }
    ]
  }
  // {
  //   path: '/reconciliation_report/stNo/:stNo/:Source',
  //   component: () => import('components/reconcReport')
  // },
  // {
  //   path: '/stn',
  //   component: () => import('layouts/MyLayout'),
  //   children: [
  //     {
  //       path: 'createStn',
  //       component: () => import('components/createStn')
  //     },
  //     {
  //       path: 'receivedStn',
  //       component: () => import('components/receivedStn')
  //     },
  //     {
  //       path: 'printStn/stNo/:stNo',
  //       component: () => import('components/printStn')
  //     },
  //     {
  //       path: 'reconciliation_report/stNo/:stNo/:Source',
  //       component: () => import('components/reconcReport')
  //     },
  //     {
  //       path: 'carton_info/stNo/:stNo',
  //       component: () => import('components/stncartoninfo')
  //     }
  //   ]
  // }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
