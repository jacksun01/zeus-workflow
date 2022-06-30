const stree = {
  state: {
    defaultExpandKeys: [],
    currentNodeKey:'',
  },

  mutations: {
    SET_DEFAULTEXPANDKEYS: (state, defaultExpandKeys) => {
      state.defaultExpandKeys = defaultExpandKeys
    },
    SET_CURRENTNODEKEY: (state, id) => {
      state.currentNodeKey = id
    },
  },

  actions: {
    updateCurrentNodeKey({commit},id) {
      return new Promise(resolve => {
        commit('SET_CURRENTNODEKEY', id)
        resolve()
      })
    },
    updateDefaultExpandKeys({commit},defaultExpandKeys) {
      return new Promise(resolve => {
        commit('SET_DEFAULTEXPANDKEYS', defaultExpandKeys)
        resolve()
      })
    },
  }
}

export default stree
