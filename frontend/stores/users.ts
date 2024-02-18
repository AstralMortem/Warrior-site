import { defineStore } from 'pinia'

export const useUsersStore = defineStore({
  id: 'myUsersStore',
  state: () => ({
    coaches: [],
    participants: [],
    pending: false,
    nextParticipants: null,
    nextCoaches: null
   }),
   actions: {
    async initStore(){
      this.pending = true
      const coachesData = await $fetch('/api/users/coaches/')
      const participantsData = await $fetch('/api/users/participants/')
      this.nextCoaches = coachesData.next
      this.coaches = coachesData.results
      this.nextParticipants = participantsData.next
      this.participants = participantsData.results
      this.pending = false
    },
    async fetchNextCoaches(){
      if(this.nextCoaches){
        this.pending = true
        const data = await $fetch('/api/users/coaches/',{query:{'next':this.nextCoaches}})
        this.nextCoaches = data.next
        this.coaches = [...this.coaches,data.results]
        this.pending = false
      }
    },
    async fetchNextParticipants(){
      if(this.nextParticipants){
        this.pending = true
        const data = await $fetch('/api/users/participants/',{query:{'next':this.nextParticipants}})
        this.nextParticipants = data.next
        this.coaches = [...this.participants,data.results]
        this.pending = false
      }
    }
  }
})
