ARG NODE_VERSION=20.10.0
ARG PORT=3000

FROM node:${NODE_VERSION}-alpine as base
ENV NODE_ENV=production

WORKDIR /src

#build
FROM base as build
COPY ../../frontend/package*.json ../../frontend/yarn.lock ./
RUN yarn install
COPY ../../frontend .
RUN yarn run build

#run 
FROM base
COPY --from=build /src/.output /src/.output
EXPOSE $PORT
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=$PORT

CMD ["node", ".output/server/index.mjs"]