FROM node:16-alpine
WORKDIR /app
COPY uptime-kuma /app
RUN npm install
EXPOSE 3001
CMD ["npm", "start"]
