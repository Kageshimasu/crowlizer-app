# FROM node:10.17.0-alpine3.9
# WORKDIR /usr/src/app
# COPY . /usr/src/app/
# RUN npm install
FROM httpd:latest
COPY ./dist/ /usr/local/apache2/htdocs/
