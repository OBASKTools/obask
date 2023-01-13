### Adding semantic tags via SPARQL queries


1. Create new sparql construct statement in sparql/, naming it 'construct_{name}.sparql', where {name} indicates the semantic tag to add e.g. sparql/construct_Metazoan.sparql.  The sparql construct should add the semantic tag via the annotation property http://n2o.neo/property/nodeLabel
2. Add the label name to the to the correct DUMPS variable for the service is should appear in (DUMPS_SOLR, DUMPS_PDB, DUMPS_OWLERY) in dumps/config.env

e.g. 

construct_has_image.sparql file has content

```sparql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

CONSTRUCT {
	?x <http://n2o.neo/property/nodeLabel> "has_image" .
}
WHERE {
  # Some SELECT criteria in here.
}
```

dumps/config.env has

DUMPS_SOLR="all deprecation has_image"

=> `has_image` and `deprecation` (obsolete) semantics tags loaded along with complete dump of triplestore content (all) to SOLR
