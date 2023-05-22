# OBASK Quick start

## Prerequisites:

1. Update to docker compose V2 (>= Docker Compose version v2.17) (see [https://docs.docker.com/compose/install/linux/](https://docs.docker.com/compose/install/linux/))

## Create your project:

1. [Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter)

`python3 -m pip install --user cookiecutter`

or

`conda install cookiecutter`

2. Navigate to a folder where you want to create your new pipeline project and run the OBASK project template

`cookiecutter gh:OBASKTools/obask-template`

Then provide your `project_name` when asked.

3. Commit your project to GitHub. Be bold, if you are not satisfied with the result, you can delete the repository and create it again as many times as you want.

    - Navigate to your newly created project folder and initialize the git repository.
    ```
    git init -b main
    git add .
    git commit -m "First commit"
    ```

    - [Create a new repository](https://github.com/new). Repo name should be same with the `project_name` you provided to the template.

    - Do not initialize with a README (you already have one)

    - Click Create

    - See the section under "…or push an existing repository from the command line". Follow the instructions there. E.g. (make sure the location of your remote is exactly correct!).
    ```
    git remote add origin https://github.com/MyRepo/my_project_name.git
    git branch -M main
    git push -u origin main
    ```

4. Customise your configs:

    Mandatory:
    - customize config/collectdata/vfb_fullontologies.txt
    - config/prod/neo4j2owl_config.yaml
    
    Advanced:
    - collect /sparqls
    - dumps /sparqls for labels

## Run your project:

When ready, run: 

`docker-compose up -d`

Once the pipeline is complete, your services will be live at:  
- Neo4J, [http://localhost:7474/browser/](http://localhost:7474/browser/)   
- Solr, [http://localhost:8993/solr](http://localhost:8993/solr)  
- Ontology API, [http://localhost:8007/ontology](http://localhost:8007/ontology)        
- Triplestore, [http://localhost:8080/rdf4j-workbench/repositories/obask/summary](http://localhost:8080/rdf4j-workbench/repositories/obask/summary)       


## Re-run your project

If you are not 100% happy with the output and want to do further configurations, you can safely shutdown and clean all services through:

`docker-compose down`

Then you can continue customizing your configurations and run the pipeline again to see them in action via:

`docker-compose up -d`

## Troubleshooting


