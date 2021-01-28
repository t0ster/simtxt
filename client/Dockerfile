FROM node:15-slim as base
COPY package.json yarn.lock /app/
WORKDIR /app
# RUN yarn install --prod
RUN yarn install

FROM base as dev
# RUN yarn install
COPY . /app

FROM base as builder
COPY . /app
RUN yarn build

FROM node:15-slim as prod
COPY --from=builder /app/build /app
RUN npm install -g serve
CMD serve -s /app -l 3000
