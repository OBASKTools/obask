#!/usr/bin/env python3
# generate_organ_tags.py v2022.09

# ACTION:
#  Generate list of organ cell DL queries and labels derived from UBERON organ_slim and send output to YAML file
#  Output will be used to filter and/or boost search results in Cell Annotation Platform (CAP)

import argparse
import ruamel.yaml
import utils.config_autogenerate_utils as utils


# from config_autogenerate_utils import utils


def generate_organ_cells(output):
    """Generates organ cell semantic tags - DL queries pairs with given list

    Parameters:
    output (list): List that contains a sparql query result. Organ query in this function

    Returns:
    organs (list): Organ list that contains semantic tags - DL queries pairs
    """
    organs = []
    for n in output:
        curie = n['x']['value'].replace("_", ":")
        curie = curie.partition('http://purl.obolibrary.org/obo/')[-1]
        # RO:0002131 = 'overlaps'
        dl_query = "RO:0002131 some " + curie
        label = n['xLabel']['value'].replace(" ", "_")
        organs.append((dl_query, label, curie))
    return organs


parser = argparse.ArgumentParser(description='set destination YAML file for query output')

parser.add_argument('-i', '--inputfile', default='../config/prod/neo4j2owl-config_manual.yaml', help='''
    Use this option to indicate destination (input) file for organ cell DL queries and semantic labels. By default, query output
    is sent to a file named neo4j2owl-config.yaml.
    ''')
parser.add_argument('-o', '--outputfile', default='../config/prod/neo4j2owl-config.yaml', help='''
    Use this option to indicate the final filename for inputfile + organ cell DL queries and semantic labels. By default, the final
    output file is named neo4j2owl-config.yaml.
    ''')

args = parser.parse_args()

input_file_name = args.inputfile
output_file_name = args.outputfile

organ_query = """
PREFIX inSubset: <http://www.geneontology.org/formats/oboInOwl#inSubset>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  ?x ?xLabel
WHERE 
{
      ?x inSubset: 	<http://purl.obolibrary.org/obo/uberon#cap_organ_slim> .
      ?x rdfs:label ?xLabel 
}
    """

# <http://purl.obolibrary.org/obo/uberon/core#organ_slim>
query_output = utils.run_query(organ_query)

# generate list of organ cell DL queries and semantic labels
organ_list = generate_organ_cells(query_output)

# ramuel.yaml initialization and configuration
yaml = ruamel.yaml.YAML()
yaml.indent(sequence=4, offset=2)

with open(input_file_name) as file:
    yaml_config = yaml.load(file)

yaml_config['neo_node_labelling'] = utils.update_neo_node_labelling(yaml_config['neo_node_labelling'], organ_list)

# export populated dictionary to file
with open(output_file_name, 'w') as file:
    documents = yaml.dump(yaml_config, file)
