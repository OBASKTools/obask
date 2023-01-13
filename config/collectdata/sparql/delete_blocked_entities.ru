PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX n2o: <http://n2o.neo/property/>
PREFIX n2oc: <http://n2o.neo/custom/>
PREFIX dct: <http://purl.org/dc/terms/>

DELETE {
  ?s <http://n2o.neo/custom/block> ?blocked .
  ?s ?p ?o .
}
WHERE {
  ?s <http://n2o.neo/custom/block> ?blocked .
  ?s ?p ?o .
  FILTER(?blocked=true) .
  FILTER(isIRI(?s))
}

### EDIT: this was obsoleted in the end in favour of a cypher solution, see process.sh.
