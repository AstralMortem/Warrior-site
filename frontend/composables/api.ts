import { type UseFetchOptions } from '#app';
import { type NitroFetchRequest } from 'nitropack';
import { KeyOfRes } from 'nuxt/dist/app/composables/asyncData';

export function useApiRequest<T>(
  request: NitroFetchRequest,
  opts?:
    | UseFetchOptions<T extends void ? unknown : T,
    (res: T extends void ? unknown : T) => T extends void ? unknown : T,
    KeyOfRes<(res: T extends void ? unknown : T) => T extends void ? unknown : T>>
    | undefined
) {
  const config = useRuntimeConfig();

  return useFetch(request, {baseURL: config.public.BASE_URL,server:false,immediate:true,...opts});
}