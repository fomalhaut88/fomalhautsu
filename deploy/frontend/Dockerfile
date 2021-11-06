FROM node:lts-alpine

WORKDIR /code

RUN npm install -g http-server
COPY frontend/package.json .
RUN npm install

COPY frontend .
COPY deploy/frontend/.env .
RUN rm -f .env.local

RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist", "--proxy", "http://0.0.0.0:8080?" ]
