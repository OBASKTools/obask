# OBASK Quick start

## Prerequisites:
1. Update to docker compose V2 (>= Docker Compose version v2.17) (see [https://docs.docker.com/compose/install/linux/](https://docs.docker.com/compose/install/linux/))



1. Checkout obask repository, `git clone https://github.com/OBASKTools/obask.git`.

2. Customise configs
    Mandatory:
    1. customize config/collectdata/vfb_fullontologies.txt
    1. config/prod/neo4j2owl_config.yaml
    Advanced:
    1. collect sparqls
    1. dumps sparqls for labels

3. run `docker-compose up -d`

Services are:  
* Triplestore, [http://localhost:8080/rdf4j-workbench/repositories/obask/summary](http://localhost:8080/rdf4j-workbench/repositories/obask/summary)
* Neo4J, [http://localhost:7474/browser/](http://localhost:7474/browser/)  
* Solr, [http://localhost:8993/solr](http://localhost:8993/solr)  
* Ontology API, [http://localhost:8007/ontology](http://localhost:8007/ontology)


## Re-run Pipeline

Run following commands to re-run the pipeline.

1. `docker-compose down`

2. `docker-compose build --no-cache`

3. `docker-compose up -d`
