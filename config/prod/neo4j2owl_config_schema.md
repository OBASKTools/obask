# neo4j2owl-config schema

*A JSON schema for documenting and validating the neo4j2owl configuration YAML.*

## Properties

- **`allow_entities_without_labels`** *(boolean)*: Allow loading of entities without rdfs:label.
- **`index`** *(boolean)*: ?
- **`testmode`** *(boolean)*: ?
- **`batch`** *(boolean)*: Create and load CSVs in batches (?).
- **`batch_size`** *(integer)*: Size of batches to load.
- **`safe_label`** *(string)*: ? Must be one of: `['loose']`.
- **`relation_type_threshold`** *(number)*: neo2owl attempts to consistently cast annotation value types (property value types).  To do this it uses the threshold set here (more details TBA).
- **`represent_values_and_annotations_as_json`** *(object)*: Use this to record the IRIs of annotation properties whose values should be recorded as JSON, allowing the representation of axiom annotations on annotation axioms. Cannot contain additional properties.
  - **`iris`** *(array)*
    - **Items** *(string)*
- **`neo_node_labelling`** *(array)*
  - **Items**: Refer to *#/definitions/semantic_tag*.
- **`curie_map`** *(object)*: A map of prefixes to base IRIs.
- **`filters`** *(object)*: .
## Definitions

- **`semantic_tag`** *(object)*: Specifies a set of Manchester syntax class expressions and a label. Annotates all entities that are equivalent_to or subclasses of these expression with the label using the AP: {TBA} .  In conversion to Neo4J these become neo4j:labels. Cannot contain additional properties.
  - **`classes`** *(array)*: A list of Manchester syntax class expressions in which OWL entities are expressed as CURIEs.
    - **Items** *(string)*
  - **`label`** *(string)*: Semantic tag name.
  - **`description`** *(string)*: Short description to give general information about the semantic tag, and state its purpose.
