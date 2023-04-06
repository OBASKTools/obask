# OBASK Quick start

## Prerequisites:
1. Update to docker compose V2 (>= Docker Compose version v2.17) (see [https://docs.docker.com/compose/install/linux/](https://docs.docker.com/compose/install/linux/))



1. create a fork and checkout obask repository? 
1. Customise configs
    Mandatory:
    1. customize config/collectdata/vfb_fullontologies.txt
    1. config/prod/neo4j2owl_config.yaml
    Advanced:
    1. collect sparqls
    1. dumps sparqls for labels

1. update all OBASK images (add a script ??)
1. run
```
docker-compose up  (--force-recreate ?)
```

Services are:
http://localhost:8080/rdf4j-server
http://localhost:7474/browser/


## Re-run Pipeline

- docker-compose down

docker-compose build --no-cache

- clean triplestore (remove container)
- clean solr
- clean neo4j
- 



## TODO:
- delete pipeline-prod project (replaced by obask-kb)
- Can I delete CONF_REPO args from compose?
- which solr image to use (currently virtualflybrain/vfb-solr)?
- clean dumps sparqls
- **** modules read config from volume
- dumps read neo4j2owl config from local files
- obask/src altındaki scriptler lazım mı (write_organ_tags.py etc.)
