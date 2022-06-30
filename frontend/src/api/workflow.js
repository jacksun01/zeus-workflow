import request from '@/utils/request'

const WorkflowUrl = '/workflow/workflows'
const WorkorderUrl = '/workflow/workorders'
const WorkflowgroupUrl = '/workflow/workflowgroups'
const FormfieldsUrl = '/workflow/formfields'

const AuditStepsUrl = '/workflow/auditsteps'

export const Workflow = {
  create(params) {return request.post(`${WorkflowUrl}/`, params).then(response => {return response.data})},
  delete(id) {return request.delete(`${WorkflowUrl}/${id}/`)},
  update(id, params) {return request.put(`${WorkflowUrl}/${id}/`, params).then(response => {return response.data})},
  patch(id, params) {return request.patch(`${WorkflowUrl}/${id}/`, params).then(response => {return response.data})},
  get(id) {return request.get(`${WorkflowUrl}/${id}/`).then(response => {return response.data})},
  list(params) {return request.get(`${WorkflowUrl}/`, {params: params}).then(response => {return response.data})},

  formfields(id) {return request.get(`${WorkflowUrl}/${id}/formfields/`).then(response => {return response.data})},
  steps(id) {return request.get(`${WorkflowUrl}/${id}/steps/`).then(response => {return response.data})},

  hot() {return request.get(`${WorkflowUrl}/hot/`).then(response => {return response.data})},

  getDemoformfields() {return request.get(`${WorkflowUrl}/demoformfields/`).then(response => {return response.data})},
}

export const Workorder = {
  create(params) {return request.post(`${WorkorderUrl}/`, params).then(response => {return response.data})},
  delete(id) {return request.delete(`${WorkorderUrl}/${id}/`)},
  update(id, params) {return request.put(`${WorkorderUrl}/${id}/`, params).then(response => {return response.data})},
  patch(id, params) {return request.patch(`${WorkorderUrl}/${id}/`, params).then(response => {return response.data})},
  get(id) {return request.get(`${WorkorderUrl}/${id}/`).then(response => {return response.data})},
  list(params) {return request.get(`${WorkorderUrl}/`, {params: params}).then(response => {return response.data})},


  audit(id,params) {return request.post(`${WorkorderUrl}/${id}/audit/`, params).then(response => {return response.data})},
  auditrecord(id) {return request.get(`${WorkorderUrl}/${id}/auditrecord/`).then(response => {return response.data})},
  feedback(id,params) {return request.post(`${WorkorderUrl}/${id}/feedback/`, params).then(response => {return response.data})},
  revoke(id,params) {return request.post(`${WorkorderUrl}/${id}/revoke/`, params).then(response => {return response.data})},
  getfileds() {return request.get(`${WorkorderUrl}/getfileds/`).then(response => {return response.data})},
  get_table_info() {return request.get(`${WorkorderUrl}/get_table_info/`).then(response => {return response.data})},
}

export const Workflowgroup = {
  create(params) {return request.post(`${WorkflowgroupUrl}/`, params).then(response => {return response.data})},
  delete(id) {return request.delete(`${WorkflowgroupUrl}/${id}/`)},
  update(id, params) {return request.put(`${WorkflowgroupUrl}/${id}/`, params).then(response => {return response.data})},
  patch(id, params) {return request.patch(`${WorkflowgroupUrl}/${id}/`, params).then(response => {return response.data})},
  get(id) {return request.get(`${WorkflowgroupUrl}/${id}/`).then(response => {return response.data})},
  list(params) {return request.get(`${WorkflowgroupUrl}/`, {params: params}).then(response => {return response.data})},
}


export const Formfields  = {
  create(params) {return request.post(`${FormfieldsUrl}/`, params).then(response => {return response.data})},
  delete(id) {return request.delete(`${FormfieldsUrl}/${id}/`)},
  update(id, params) {return request.put(`${FormfieldsUrl}/${id}/`, params).then(response => {return response.data})},
  patch(id, params) {return request.patch(`${FormfieldsUrl}/${id}/`, params).then(response => {return response.data})},
  get(id) {return request.get(`${FormfieldsUrl}/${id}/`).then(response => {return response.data})},
  list(params) {return request.get(`${FormfieldsUrl}/`, {params: params}).then(response => {return response.data})},

  down(id) {return request.get(`${FormfieldsUrl}/${id}/down/`, ).then(response => {return response.data})},
  up(id) {return request.get(`${FormfieldsUrl}/${id}/up/`, ).then(response => {return response.data})},
}

export const AuditSteps  = {
  create(params) {return request.post(`${AuditStepsUrl}/`, params).then(response => {return response.data})},
  delete(id) {return request.delete(`${AuditStepsUrl}/${id}/`)},
  update(id, params) {return request.put(`${AuditStepsUrl}/${id}/`, params).then(response => {return response.data})},
  patch(id, params) {return request.patch(`${AuditStepsUrl}/${id}/`, params).then(response => {return response.data})},
  get(id) {return request.get(`${AuditStepsUrl}/${id}/`).then(response => {return response.data})},
  list(params) {return request.get(`${AuditStepsUrl}/`, {params: params}).then(response => {return response.data})},

  down(id) {return request.get(`${AuditStepsUrl}/${id}/down/`, ).then(response => {return response.data})},
  up(id) {return request.get(`${AuditStepsUrl}/${id}/up/`, ).then(response => {return response.data})},
  get_table_info() {return request.get(`${AuditStepsUrl}/get_table_info/`).then(response => {return response.data})},
}
