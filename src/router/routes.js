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
      { path: 'studentreccords', component: () => genericImport('studentreccords') },
      { path: 'sessionexams', component: () => genericImport('sessionexams') },
      { path: 'Encode', component: () => genericImport('Encode') },
      { path: 'Decode', component: () => genericImport('Decode') },
      { path: 'settings', component: () => genericImport('settings') },
      { path: 'rto', component: () => genericImport('rto') },
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
