import { defineStore } from 'pinia'

export const useNewsStore = defineStore({
  id: 'myNewsStore',
  state: () => ({ 
    news: [],
    pending: false,
    next: null,
  }),
  actions: {
    async initStore(){
      this.pending = true
      const data = await $fetch('/api/news/')
      this.next = data.next
      this.news = data.results
      this.pending = false
    },
    async fetchNext(){
      if(this.next){
        this.pending = true
        const data = await $fetch('/api/news/',{query:{'next':this.next}})
        this.next = data.next
        this.news = [...this.news,data.results]
        this.pending = false
      }
    }
  }
})
