# OBASK Advanced Settings

## Configuring Ontology Files in collectdata

The OBASK pipeline allows you to configure both remote and local ontology files that will be used in your project. These files are configured as part of the `collectdata` module within the `config/collectdata` folder, specifically in the `vfb_fullontologies.txt` file, and are processed as follows:

### Remote Ontology Files

To configure remote ontology files, add the URLs of the ontology files you want to download directly to the `config/collectdata/vfb_fullontologies.txt` file. Each URL should be on a new line.

```text
http://purl.obolibrary.org/obo/go.owl
http://purl.obolibrary.org/obo/cl.owl
```

When the pipeline runs, it will download these ontology files from the specified remote sources and process them accordingly.

### Local Ontology Files

For local ontology files that you want to include in the pipeline, you should follow these steps:

1. **Place the Files**: Copy the local ontology files into the `config/collectdata/local_ontologies` directory. The files should have a `.owl` extension.

2. **No Need to List in `vfb_fullontologies.txt`**: Unlike remote files, you do not need to add the local files to the `vfb_fullontologies.txt` file. The pipeline automatically detects any `.owl` files in the `local_ontologies` directory.

3. **Pipeline Processing**: During the pipeline execution, any `.owl` files found in the `local_ontologies` directory will be copied to the `VFB_DOWNLOAD_DIR`. After this, the pipeline will proceed to download and process any remote ontology files listed in `vfb_fullontologies.txt`.

### Example Configuration

If your project requires both remote and local ontology files, your setup might look like this:

1. **Remote Files in `vfb_fullontologies.txt`:**

2. **Local Files in `config/collectdata/local_ontologies`:**

    Place files like `my_local_ontology.owl` and `custom_terms.owl` directly in the `local_ontologies` directory.

This configuration ensures that your project uses a combination of remote and local ontology files, processed in a seamless and automated way during the pipeline run.
