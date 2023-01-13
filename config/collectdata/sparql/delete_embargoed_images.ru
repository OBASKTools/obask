PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX n2o: <http://n2o.neo/property/>
PREFIX n2oc: <http://n2o.neo/custom/>
PREFIX dct: <http://purl.org/dc/terms/>

#Delete all ds:DataSet where ds.production is False
#Delete all i:Individual where (ds)-[:has_source]-(i:Individual)<-[:depicts]-(ch:Individual) WHERE ds.production is False

DELETE {
	?image ?imgrel ?imgval .
	?imgval  ?p1  ?o1 .
}

WHERE {

	?dataset n2o:nodeLabel ?nodelabel . # This selects all datasets

	OPTIONAL {
		?dataset n2oc:production ?production .
		# n2oc:production is a bit brittle because IRI might be changed (risk!)
	}

	?image dct:source ?dataset . #in case a dataset does not have images yet this is an optional clause
	?image ?imgrel ?imgval .
	OPTIONAL {
        ?imgval  ?p1  ?o1  .
        FILTER (isBlank(?imgval)) 
  }

	FILTER(?production=false || !bound(?production)) .
	FILTER(?nodelabel="DataSet") 
}

### EDIT: this was obsoleted in the end in favour of a ROBOT solution, see process.sh. Using SPARQL this way is too memory consuming.
