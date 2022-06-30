import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/views/layout/Layout'
import userRouter from './modules/user'
import modellogRouter from './modules/modellog'
import workflowRouter from "./modules/workflow";

export const constantRouterMap = [
 {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path*',
        component: () => import('@/views/redirect/index')
      }
    ]
  },
  {
    path: '/login',
    component: () => import('@/views/user/login/index'),
    hidden: true
  },

  {
    path: '/resetpwd',
    component: () => import('@/views/user/resetpwd'),
    hidden: true
  },
  {
    path: '/user',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/user/resetpwd',
        component: () => import('@/views/user/pwdReset'),
        name: 'resetPassword',
        meta: {title: 'userResetPwd'}
      },
      {
        path: '/user/changepwd',
        component: () => import('@/views/user/pwdChange'),
        name: 'changePassword',
        meta: {title: 'userChangePwd'}
      },
      {
        path: '/user/info',
        component: () => import('@/views/user/info'),
        name: 'userinfo',
        meta: {title: 'userInfo'}
      },
    ]
  },


  {
    path: '/auth-redirect',
    component: () => import('@/views/user/login//authredirect'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/errorPage/404'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/errorPage/401'),
    hidden: true
  },
  {
    path: '/502',
    component: () => import('@/views/errorPage/502'),
    hidden: true
  },
  {
    path: '',
    component: Layout,
    redirect: 'dashboard',
    children: [
      {
        path: 'dashboard',
        component: () => import('@/views/dashboard/index'),
        name: 'Dashboard',
        meta: {title: 'dashboard', icon: 'dashboard', noCache: true}
      }
    ]
  }
]

export default new Router({
  scrollBehavior: () => ({y: 0}),
  routes: constantRouterMap
})

export const asyncRouterMap = [
  workflowRouter,
  userRouter,
  modellogRouter,
  {path: '*', redirect: '/404', hidden: true}
]
