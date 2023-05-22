# Ontology Based Application Starter Kit (OBASK)

Ontology Based Application Starter Kit (OBASK) is an innovative tool that empowers users to easily create search and knowledge exploration applications using their ontologies, without the need for any programming skills. With OBASK, users can quickly kickstart an ontology-driven application by simply defining their input ontologies and providing gross classifications via configuration files.

_OBASK tools originated with work carried out to support the [Virtual Fly Brain](virtualflybrain.org) project, the [Allen Cell-Type Knowledge Explorer](https://knowledge.brain-map.org/celltypes) and the [Cell Annotation Platform](celltype.info). Code on this collection of repos should be considered a first beta release.  Work is ongoing to improve documentation and testing of user config._

Once the configuration is set up, OBASK takes care of the heavy lifting, automatically generating knowledge search endpoints, Solr indexes, and materialized knowledge graphs with a single command. This means that users can focus on exploring and analyzing their data without getting bogged down in technical details.

With OBASK, users can harness the full potential of their ontologies to create powerful and insightful applications that enable them to better understand and analyze their data.

OBASK pipeline comprises three servers/services and four data pipelines:

- Pipeline _servers_:
  - Triplestore
  - SOLr + preconfigured SOLr core
  - Search API (`ontology-search`)
  - Neo4J production instance (`obask-kb`)
- Pipeline _data pipelines_:
  - Data collection (`pipeline-collectdata`)
  - Triple store ingestion (`pipeline-updatetriplestore`)
  - Data transformation and dumps for production instances (`pipeline-dumps`)
  - KG production instance ingestion (`pipeline-updateprod`)

Server and data pipelines are combined into 3 general sub-pipelines which are configured as Docker compose services. This documentation describes all 3 sub-pipelines in detail, including which role the individual servers and data pipelines play.

![Pipeline Overview](docs/pipeline-overview.png)

## Start using OBASK

Please follow the [quick start guide](https://obasktools.github.io/obask/quick_start/).

## OBASK Architecture

See the [architecture documentation](https://obasktools.github.io/obask/architecture/).



