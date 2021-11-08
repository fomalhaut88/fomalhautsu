FROM node:lts-alpine

WORKDIR /code

RUN npm install -g http-server
COPY package.json .
RUN npm install

COPY . .
COPY deploy/.env .

RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist", "--proxy", "http://0.0.0.0:8080?" ]
