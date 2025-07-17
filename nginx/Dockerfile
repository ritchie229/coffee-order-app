FROM nginx:1.29.0-bookworm
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["sh", "-c", "until getent hosts web; do echo 'Waiting for web...'; sleep 2; done; nginx -g 'daemon off;'"]