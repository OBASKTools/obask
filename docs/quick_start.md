# OBASK Quick start

Prerequisites:
1. Update to docker compose V2 (see [https://docs.docker.com/compose/install/linux/](https://docs.docker.com/compose/install/linux/))



1. create a fork and checkout obask repository? 
1. Customise configs
1. run
```
docker compose up
```

Services are:
http://localhost:8080/rdf4j-server
http://localhost:7474/browser/



TODO:
- delete pipeline-prod project (replaced by obask-kb)
- Can I delete CONF_REPO args from compose?
- which solr image to use (currently virtualflybrain/vfb-solr)?
- Should we use compose v2?
    - From the end of June 2023 Compose V1 won’t be supported anymore and will be removed from all Docker Desktop versions.

