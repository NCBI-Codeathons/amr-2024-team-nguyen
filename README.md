# Team Project Name

List of participants and affiliations:
- (Team Leader) Marcus Nguyen, [ANL](https://www.anl.gov/) (Argonne National Lab)
- (Writer) Nicole Bowers, [ANL](https://www.anl.gov/) (Argonne National Lab)
- (Tech Lead) Clark Cucinell, [ANL](https://www.anl.gov/) (Argonne National Lab)
- ( <img src="https://github.com/user-attachments/assets/e498c0a6-5641-487d-b346-624ff7a6d922" width="24"> ) Curtis Hendrickson, [UAB](https://uab.edu) (University of Alabama at Birmingham)
- ( <img src="https://github.com/user-attachments/assets/e498c0a6-5641-487d-b346-624ff7a6d922" width="24"> ) Don Dempsey, [UAB](https://uab.edu) (University of Alabama at Birmingham)
- ( <img src="https://github.com/user-attachments/assets/e498c0a6-5641-487d-b346-624ff7a6d922" width="24"> ) Andrew Warren, [BII](https://biocomplexity.virginia.edu/) (University of Virginia Biocomplexity Institute and Initiative)

<!-- [ICTV](https://ictv.global), [BV-BRC](https://bv-brc.org), [Kaizen-Education](https://www.uab.edu/ccts/training-academy/kaizen)-->


## Project Goals

The primary goal of this project is to establish robust correlations between the results of Antimicrobial Susceptibility Testing (AST) and the presence of Antimicrobial Resistance (AMR) genes, both plasmid-borne and chromosomal. By systematically analyzing bacterial isolates, we aim to identify specific patterns in resistance profiles that correspond to the presence of particular AMR genes and their location on plasmids or the chromosome. This will provide valuable insights into the mechanisms by which resistance is conferred and transmitted within microbial populations, potentially informing future therapeutic strategies and public health interventions aimed at combating the spread of antimicrobial resistance.

## Approach

This project will employ a 3-pronged approach to systematically identify AMR genes on both plasmids and chromosomal DNA, and correlate them with antimicrobial resistance phenotypes. Using open-source data, including sequences from NCBI, we will first predict whether genomic sequences or contigs originate from plasmids or chromosomal regions. Next, we will apply AMR gene identification algorithms to detect the presence of resistance genes. Additionally, we augment the AST data using phenotype prediction models, thereby increasing our set of antimicrobial resistance profiles. By integrating plasmid predictions with AMR gene data, we will categorize AMR genes based on their genomic location (plasmid vs. chromosomal). These results will then be correlated with the phenotypic resistance data to assess the relationship between the genetic context of AMR genes and observed antimicrobial susceptibility. This approach will enable a detailed analysis of the genomic architecture of resistance and its phenotypic expression.

![Data Pipeline](https://github.com/user-attachments/assets/a5da2130-1dba-43d6-bce2-2de54c97899c)

## Tools

### AMR Finder
- [AMRFinderPlus](https://www.ncbi.nlm.nih.gov/pathogens/antimicrobial-resistance/AMRFinder/)

### AMR Models
- Private
- [A genomic data resource for predicting antimicrobial resistance from laboratory-derived antimicrobial susceptibility phenotypes](https://academic.oup.com/bib/article/22/6/bbab313/6347947)

### KMC
- [Github](https://github.com/refresh-bio/KMC)

### Plasmid Prediction
- [Classification of bacterial plasmid and chromosome derived sequences using machine learning](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0279280)
#### PlasmidFinder
- [Bioconda link](https://anaconda.org/bioconda/plasmidfinder)
- [Website](https://cge.food.dtu.dk/services/PlasmidFinder/)
- [In Silico Detection and Typing of Plasmids using PlasmidFinder and Plasmid Multilocus Sequence Typing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4068535/)

## Results

### AMR Phenotype Prediction Accuracies

Full breakdown on species and individual antibiotics available in the AMR Phenotypes directory.  

**Species-antibiotic summary**

| |Ground Truth| |Expected| | |
|-|------------|-|--------|-|-|
|Species|F1 Score|Samples|F1 Score|95% CI||
|acinetobacter baumannii|0.8975|920|0.9328|0.9321|0.9335|
|campylobacter jejuni|0.9948|2138|0.9849|0.9847|0.9852|
|clostridioides difficile|0.0000|1|0.9678|#DIV/0!|#DIV/0!|
|enterococcus faecium|0.3406|14|0.9711|0.9707|0.9716|
|klebsiella pneumoniae|0.8497|469|0.8960|0.8952|0.8969|
|neisseria gonorrhoeae|0.5939|458|0.9640|0.9635|0.9645|
|pseudomonas aeruginosa|0.8398|324|0.7894|0.7873|0.7914|
|salmonella enterica|0.9230|7032|0.9319|0.9311|0.9327|
|staphylococcus aureus|0.8324|456|0.9764|0.9761|0.9767|
|streptococcus pneumoniae|0.9281|132|0.9629|0.9623|0.9634|

## Future Work

TODO

## NCBI Codeathon Disclaimer
This software was created as part of an NCBI codeathon, a hackathon-style event focused on rapid innovation. While we encourage you to explore and adapt this code, please be aware that NCBI does not provide ongoing support for it.

For general questions about NCBI software and tools, please visit: [NCBI Contact Page](https://www.ncbi.nlm.nih.gov/home/about/contact/)


