# Getting the precomputed ast-assemblies

Using the [Google Cloud SDK](https://cloud.google.com/sdk/?hl=en). The google tools are available individually as well.
We logged into our google account with access to the NCBI codeathon.

## Logging in to google cloud
```
gcloud auth login
```

## Copying the files
```
gsutil -m cp -r gs://ast-assemblies/all-ast/ /output/path
```
 The `-m` flag enables multithreading.
 The `-r` flag allows for recursive file copying. This allows the `cp` command to copy the top level directory as well as any subdirectories and preserve the directory structure.

Data Availability Disclaimer 
You may need to contact the NCBI codeathon hosts for access. It is also possible these data will not be avaialbe on GCP afer the codeathon completes.
