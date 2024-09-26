# Getting the AMR data from Microbiggie

This is a is a description of how we accessed the data hosted on the google cloud for the ncbi-amr-codeathon. Note: you may need to contact the hosts for access. It is also possible these data will not be avaialbe on GCP afer the codeathon completes.

| ID | Value |
| -------- | ------- |
| Project ID  | ncbi-2024-amr-codeathon    |
| Project Number | 436758014946     |

We submitted our query via the 'BigQuery' option.


```
SELECT *
FROM `ncbi-pathogen-detect.pdbrowser.microbigge`
WHERE type = 'AMR'
```

We selected all fields for the data with the type "AMR". We limited the data to "AMR" due to the scope of the hackathon.

Our query results were too large for the GCP standard output options. So we created storage buckets with the help of NCBI staff member, Brian Koser.
