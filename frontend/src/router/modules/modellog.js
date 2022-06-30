/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/views/layout/Layout'

const modellogRouter = {
  path: '/modellog',
  component: Layout,
  redirect: '/modellog/logsentry',
  name: 'Modellog',
  meta: {
    title: 'modellog',
    icon: 'log_1'
  },
  children: [
    {
      path: 'logsentrys',
      component: () => import('@/components/CommonVue/vueAdSearchNoMenu'),
      name: 'logSentryList',
      meta: { title: 'logSentryList' }
    }
  ]
}
export default modellogRouter
