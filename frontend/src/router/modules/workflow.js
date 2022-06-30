/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/views/layout/Layout'

const workflowRouter = {
  path: '/workflow',
  component: Layout,
  redirect: '/workflow/workorders/',
  name: 'Workflow',
  meta: {
    title: 'workflow',
    icon: 'workflow'
  },
  children: [
    {
      path: 'workorders',
      component: () => import('@/views/workflow/workorders'),
      name: 'workorderList',
      meta: {title: 'workorderList'}
    },
     {
      path: 'workorderswaiting',
      component: () => import('@/views/workflow/workorderswaiting'),
      name: 'woswaitingList',
      meta: {title: 'woswaitingList'}
    },
    {
      path: 'workorderssupervise',
      component: () => import('@/views/workflow/workorderssupervise'),
      name: 'wosuperviseList',
      meta: {title: 'wosuperviseList'}
    },
    {
      path: 'workordershistory',
      component: () => import('@/views/workflow/workordershistory'),
      name: 'wohistoryList',
      meta: {title: 'wohistoryList'}
    },
    {
      path: 'workflows',
      component: () => import('@/views/workflow/workflows'),
      name: 'workflowList',
      meta: {title: 'workflowList'}
    },
    {
      path: 'workflowgroup',
      component: () => import('@/views/workflow/workflowgroup'),
      name: 'workflowgroupList',
      meta: {title: 'workflowgroupList'},
      hidden:true,
    },


    {
      path: 'formfields',
      component: () => import('@/views/workflow/formfields'),
      name: 'formfieldsList',
      meta: {title: 'formfieldsList'},
      hidden: true,
    },
    {
      path: 'auditsteps',
      component: () => import('@/views/workflow/auditSteps'),
      name: 'auditStepsList',
      meta: {title: 'auditStepsList'},
      hidden: true,
    },

  ]
}
export default workflowRouter
