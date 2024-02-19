FROM node:18-alpine

WORKDIR /app

COPY ../../frontend/. /app/

RUN yarn install

EXPOSE 3000

RUN yarn build