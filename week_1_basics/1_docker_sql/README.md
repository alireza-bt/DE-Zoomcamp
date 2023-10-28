create VM OCI

generate SSH keys:
ssh-keygen ...

install:
- Anaconda (with binary) 
- Docker (with dnf) (https://www.atlantic.net/dedicated-server-hosting/how-to-install-docker-and-docker-compose-on-oracle-linux-8/)
- Docker-compose (https://github.com/docker/compose/releases/tag/v2.22.0)

config docker to use without sudo:
https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md

if still not works:
newgrp docker (new group)
and
reboot

go to week_1/2_docker:
- first running postgres and pgAdmin separately using Docker:
### Running Postgres with Docker

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

If you see that `ny_taxi_postgres_data` is empty after running
the container, try these:

* Deleting the folder and running Docker again (Docker will re-create the folder)
* Adjust the permissions of the folder by running `sudo chmod a+rwx ny_taxi_postgres_data`

### CLI for Postgres

Installing `pgcli`

```bash
pip install pgcli
```

If you have problems installing `pgcli` with the command above, try this:

```bash
conda install -c conda-forge pgcli
pip install -U mycli
```

Using `pgcli` to connect to Postgres

```bash
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

### pgAdmin

Running pgAdmin

```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  dpage/pgadmin4
```

For connecting to pgAdmin using GUI on local machine or using port-forwarding and remote machine:
for configuration of new server, we need the name of postgres in docker or docker-compose file (that's the host name of postgres, instead of localhost)


### Running Postgres and pgAdmin together (docker-compose)

Create a network

```bash
docker network create pg-network
```

Run Postgres (change the path)

```bash
docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v c:/Users/alexe/git/data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13
```

Run pgAdmin

```bash
docker run -it \
  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
  -e PGADMIN_DEFAULT_PASSWORD="root" \
  -p 8080:80 \
  --network=pg-network \
  --name pgadmin-2 \
  dpage/pgadmin4
```

port forwarding works in vscode:
    For connecting to pgAdmin using GUI on local machine or using port-forwarding and remote machine:
    for configuration of new server, we need the name of postgres in docker-compose file (that's the host name of postgres, instead of localhost)

Check this repo for more docker-compose configs and ideas:
https://github.com/docker/awesome-compose

### NY Trips Dataset

Dataset:

* https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
* https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf


### Data ingestion

Build the image


Running locally

```bash
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"

python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url=${URL} \
  --restart=no
```

Run the script with Docker

```bash
docker build -t taxi_ingest:v001 .
```

```bash
URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"

docker run -it \
  --network=postgres-pgadmin-net \ #add it to the network of postgres and pgadmin
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL} \
    --restart=no
```

### Docker-Compose 

Run it:

```bash
docker-compose up
```

Run in detached mode (running in background):

```bash
docker-compose up -d
```

Shutting it down:

```bash
docker-compose down
```

Note: to make pgAdmin configuration persistent, create a folder `data_pgadmin`. Change its permission via

```bash
sudo chown 5050:5050 data_pgadmin
```

and mount it to the `/var/lib/pgadmin` folder:

```yaml
services:
  pgadmin:
    image: dpage/pgadmin4
    volumes:
      - ./data_pgadmin:/var/lib/pgadmin
    ...
```
