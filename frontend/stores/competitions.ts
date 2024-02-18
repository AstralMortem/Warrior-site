import { defineStore } from 'pinia'

export const useCompetitionsStore = defineStore({
  id: 'myCompetitionsStore',
  state: () => ({
    competitions: [],
    pending:false,
    next:null
   }),
   actions: {
    async initStore(){
      this.pending = true
      const data = await $fetch('/api/events/competitions/')
      this.next = data.next
      this.competitions = data.results
      this.pending = false
    },
    async fetchNext(){
      if(this.next){
        this.pending = true
        const data = await $fetch('/api/events/competitions/',{query:{'next':this.next}})
        this.next = data.next
        this.competitions = [...this.competitions,data.results]
        this.pending = false
      }
    }
  }
})
