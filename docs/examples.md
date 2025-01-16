# OBASK Examples

## **Explore OBASK in Action**
OBASK has been successfully used to build ontology-driven applications that enable knowledge exploration and data analysis. Below are examples showcasing the tool’s capabilities and its impact on real-world projects.

---

### **1. Virtual Fly Brain**

OBASK drives search and query on the Fruit Fly Brain atlas, [Virtual Fly Brain](https://v2.virtualflybrain.org/) (VFB), where it integrates hundreds of thousands of images, connectomics data representing millions of synapses, BLAST type similarity matrices and curated annotation of neuron types and genetic reagents.  Ontologies used include the [Drosophila Anatomy Ontology](https://www.ebi.ac.uk/ols4/ontologies/fbbt).

### **2. Cell Knowledge Graph**
#### Overview
The **Cell Knowledge Graph (CL_KG)** is an ontology-driven application that integrates multiple biological ontologies with annotations of single cell transcriptomics data from [CELLxGENE](https://cellxgene.cziscience.com/). The project integrates the following ontologies:
- **Cell Ontology (CL)**
- **UBERON (Anatomical Structures)**
- **Gene Ontology (GO)**
- **MONDO (Diseases)**
- **PATO (Phenotypes)**

#### Outputs Generated Using OBASK
1. **Neo4j Knowledge Graph**:
   - The processed ontologies are integrated into a Neo4j property graph.
   - Researchers can perform graph-based queries to explore relationships and analyze data interactively.
   - Experiment with the Neo4j endpoint by following the access guide:
     [CL_KG Neo4j Access Guide](https://cellular-semantics.github.io/CL_KG/access_guide/)

2. **Solr Search Endpoint**:
   - A powerful search endpoint is generated, allowing users to perform text-based queries and leverage boosting and filtering capabilities.
   - The Swagger documentation for the search endpoint is available at:  
     [CL_KG Search Endpoint Swagger](https://cellular-semantics.sanger.ac.uk/cl-kg/)

#### Source Code
The full pipeline and configuration files for this project are publicly available. Explore the repository here:  
[CL_KG GitHub Repository](https://github.com/Cellular-Semantics/CL_KG/tree/main/cl_kb_pipeline)

---

### **3. Cell Type Knowledge Explorer**
#### Overview
The **Cell Type Knowledge Explorer** is anapplication powered by OBASK that serves as the backbone of the explorer tool available at:  
[Cell Type Knowledge Explorer](https://knowledge.brain-map.org/celltypes)

#### Key Highlights
1. **Runtime Search API Performance**:
   - Demonstrates the high performance and scalability of OBASK-generated search APIs in real-time.
2. **Innovative Application Showcase**:
   - Illustrates how OBASK enables the creation of advanced applications for data exploration and analysis.

#### Impact
This tool exemplifies OBASK’s ability to power robust and user-friendly platforms for knowledge discovery, providing insights into cell types and their relationships.

---

### **Create Your Own Knowledge Graph**
Interested in building a knowledge graph or search application like CL_KG or the Cell Type Knowledge Explorer? OBASK makes it easy:
1. Define your input ontologies, annotated data and configuration parameters in a YAML file.
2. Run OBASK to process and integrate your data.
3. Experiment with the generated Neo4j and search endpoints.

Start your journey today with [OBASK](quick_start.md) and unlock the power of your ontology-annotated data.

