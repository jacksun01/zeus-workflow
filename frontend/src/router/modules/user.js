/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/views/layout/Layout'

const userRouter = {
  path: '/users',
  component: Layout,
  redirect: '/user/info',
  name: 'User',
  meta: {
    title: 'user',
    icon: 'user'
  },
  children: [
    {
      path: 'users',
      component: () => import('@/components/CommonVue/vueAdSearch'),
      name: 'userList',
      meta: { title: 'userList' }
    },
    {
      path: 'roles',
      component: () => import('@/views/user/role'),
      name: 'roleList',
      meta: { title: 'roleList' }
    },
    {
      path: 'urls',
      component: () => import('@/components/CommonVue/vueAdSearch'),
      name: 'urlList',
      meta: { title: 'urlList' }
    },
  ]
}
export default userRouter
