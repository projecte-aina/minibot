FROM node:12.22.12-alpine3.15 AS build

RUN apk update && apk upgrade && adduser -D vueuser

USER vueuser

WORKDIR /app

COPY ./package.json .
RUN npm install 

COPY --chown=vueuser:vueuser . /app

RUN npm run build 


FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

COPY ./docker/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

# CMD /entrypoint.sh && nginx -g 'daemon off;'

ENTRYPOINT [ "/entrypoint.sh" ]