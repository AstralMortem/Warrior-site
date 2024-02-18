<template>
  <div class="px-[5px] py-2.5 rounded-[10px] shadow border border-yellow flex-col justify-start items-center gap-[5px] inline-flex md:p-2.5 md:rounded-[15px] md:gap-2.5 lg:p-5 lg:rounded-[20px]
  cursor-pointer hover:bg-yellow hover:text-black text-yellow" @click="router.push({path:`/participants/${props.id}`})">
    <UIUserAvatar :src="props.photo"/>
    <p class="text-center text-base font-normal font-title lg:text-xl">
      {{ props.full_name }}
    </p>
    <p class="text-center text-xs md:text-[15px] lg: font-normal font-display" v-show="props.mobile">{{ props.mobile }}</p>
    <img :src="props.belt?.photo" class="w-16 h-6 md:w-[100px] md:h-9 lg:w-[110px] lg:h-11" :alt="props.belt.title"> 
  </div>
</template>

<script lang="ts" setup>
  import { type IUserSmall } from '~/types/db';
  const router = useRouter()
  const props = defineProps<IUserSmall>()
</script>

<style>

</style>