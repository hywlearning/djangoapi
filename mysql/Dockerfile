FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD gnoliew
ENV MYSQL_DATABASE db_shop
EXPOSE 3306
COPY ./db_shop.sql /docker-entrypoint-initdb.d/db_shop.sql
VOLUME /var/lib/mysql
