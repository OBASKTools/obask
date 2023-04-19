from utils.schema_test_tools import test_local

test_local(path_to_schema_dir='config/dumps/',
           schema_file='neo4j2owl_config_schema.json',
           path_to_test_dir='config/prod/')
