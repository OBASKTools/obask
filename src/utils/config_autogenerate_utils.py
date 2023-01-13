from SPARQLWrapper import SPARQLWrapper, JSON
from collections import namedtuple
from typing import List, Dict
from ordered_set import OrderedSet

Config = namedtuple('Config', 'classes label')


def run_query(query):
    """Runs given sparql query using SPARQLWrapper and returns the query output

    Parameters:
    query (str): Sparql query to be run

    Returns:
    output (list): Query output
    """
    # "https://ubergraph.apps.renci.org/sparql"
    sparql = SPARQLWrapper(
        "http://localhost:8080/rdf4j-server/repositories/cap"
    )
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)
    ret = sparql.queryAndConvert()
    output = []
    for line in ret["results"]["bindings"]:
        output.append(line)
    return output


def update_neo_node_labelling(neo_node_labelling: List[Dict], item_list: List[List[str]]):
    """Updates given neo_node_labelling list with given item_list list, also removes duplicates. Returns updated list

    Parameters:
    neo_node_labelling (list): Semantic tag configurations in DL, a section in neo4j2owl-config.yaml
    item_list (list): Input list which contains new set of semantic tags and corresponding DLs

    Returns:
    output_list (list): Updated neo_node_labelling list
    """

    # Read the neo_node_labelling into a list of dict
    output_list = neo_node_labelling

    # Initialize list of Config namedtuple
    config_set = []
    for x in output_list:
        append_config(config_set, x)

    # Add given list items which contains classes and label pairs, generated automatically via SPARQL query
    for item in item_list:
        config_set.append(Config(item[0], item[1]))
        config_set.append(Config(item[2], item[1]))

    # Remove duplicates
    config_set = OrderedSet(config_set)

    # Convert list of namedtuple to list of dict
    converter = {}
    for x in config_set:
        if x.label in converter:
            converter.get(x.label).append(x.classes)
        else:
            converter.update({x.label: [x.classes]})

    # Change {'classes': 'UBERON:0010000', 'label': 'Multicellular_anatomical_structure'} to
    # {'classes': ['UBERON:0010000'], 'label': 'Multicellular_anatomical_structure'}
    output_list = list()
    for x in converter:
        output_list.append({'classes': converter.get(x), 'label': x})

    return output_list


def append_config(config_set, x):
    for classes in x['classes']:
        config = Config(classes, x['label'])
        config_set.append(config)
