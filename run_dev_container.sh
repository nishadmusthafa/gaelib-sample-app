#! /bin/bash

DS_IP=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' gaelib_ds)
docker run  -it --entrypoint /bin/sh -p 127.0.0.1:10000:8080/tcp  -v $(pwd):/sample_app -e DATASTORE_EMULATOR_HOST="$DS_IP:8888" -e DATASTORE_PROJECT_ID="sample_gaelib_app" sample_gaelib_app
