# OBASK Quick start

## Prerequisites:

1. Update to docker compose V2 (>= Docker Compose version v2.17) (see [https://docs.docker.com/compose/install/linux/](https://docs.docker.com/compose/install/linux/))

## Create your project:

1. Checkout obask repository, `git clone https://github.com/OBASKTools/obask.git`.

2. Customise your configs:

    Mandatory:
    - customize config/collectdata/vfb_fullontologies.txt
    - config/prod/neo4j2owl_config.yaml
    
    Advanced:
    - collect /sparqls
    - dumps /sparqls for labels

## Run your project:

When ready, run: 

`docker-compose up -d`

Once the pipeline is complete, your services will be live at:  
- Neo4J, [http://localhost:7474/browser/](http://localhost:7474/browser/)   
- Solr, [http://localhost:8993/solr](http://localhost:8993/solr)  
- Ontology API, [http://localhost:8007/ontology](http://localhost:8007/ontology)        
- Triplestore, [http://localhost:8080/rdf4j-workbench/repositories/obask/summary](http://localhost:8080/rdf4j-workbench/repositories/obask/summary)       


## Re-run your project

If you are not 100% happy with the output and want to do further configurations, you can safely shutdown and clean all services through:

`docker-compose down`

Then you can continue customizing your configurations and run the pipeline again to see them in action via:

`docker-compose up -d`

## Troubleshooting


