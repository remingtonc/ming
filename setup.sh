podman network create ming
podman create --name quick-postgres --network ming -p 5432:5432 -e POSTGRES_PASSWORD=quick postgres:alpine
podman start quick-postgres
sleep 15
podman exec quick-postgres psql -U postgres -c 'CREATE DATABASE ming;'