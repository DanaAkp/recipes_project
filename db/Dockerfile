FROM postgres:14

# run create.sql on init
COPY create.sql /docker-entrypoint-initdb.d/init.sql
RUN /docker-entrypoint-initdb.d/init.sql