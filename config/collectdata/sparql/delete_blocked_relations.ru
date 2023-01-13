PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX n2o: <http://n2o.neo/property/>
PREFIX n2oc: <http://n2o.neo/custom/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>


DELETE {
  ?s ?p ?o .
  ?r rdf:type owl:Axiom ;
        owl:annotatedSource ?s ;
        owl:annotatedProperty ?p ;
        owl:annotatedTarget ?o ;
        <http://n2o.neo/custom/block> ?blocked;
        ?bp ?bo;

} WHERE {
  ?s ?p ?o .
  ?r rdf:type owl:Axiom ;
      owl:annotatedSource ?s ;
      owl:annotatedProperty ?p ;
      owl:annotatedTarget ?o ;
      <http://n2o.neo/custom/block> ?blocked;
      ?bp ?bo;

  FILTER(?blocked=true) .
}

### EDIT: this was obsoleted in the end in favour of a cypher solution, see process.sh.
