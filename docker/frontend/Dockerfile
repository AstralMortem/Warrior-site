ARG NODE_VERSION=18.0.0
ARG PORT=3000

FROM node:${NODE_VERSION}-slim as base

ENV NODE_ENV=production
WORKDIR /src

FROM base as build

COPY --link ../../frontend/package.json ../../frontend/yarn.lock ./
RUN yarn install --production=false

COPY --link ../../frontend .

RUN yarn nuxt build

FROM base

ENV PORT=$PORT

COPY --from=build /src/.output /src/.output

CMD ["node", ".output/server/index.mjs"]