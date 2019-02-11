
# Literature
1. Local BLAST database creation: https://www.ncbi.nlm.nih.gov/books/NBK279688/
2. Local BLAST biopython documentation: https://biopython.readthedocs.io/en/latest/Tutorial/chapter_blast.html
3. TogoWS Rest API: http://togows.org/

# Dependencies
1. BLAST+ suite: https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download
2. Biopython: https://biopython.org/wiki/Download

# How to run
**!! Only change Main.py !!**
```python
from Controllers import BlastController

def main():
    #Change the KEGG organism identifiers to your organisms
    #https://www.genome.jp/kegg/catalog/org_list.html
    blastController = BlastController('hsa',
                                      'bta',
                                      'phd', pathway_id = "00040") (00040 is default)

    #Change the BLAST+ local database name to your created local database name
    #Mine was: C:\\Users\\bram\\PycharmProjects\\\AutomatedKeggBlast\\Data\\Input\\Debaryomyces_occidentalis.fas
    blastController.blastn(database="C:\\Users\\bram\\PycharmProjects\\\AutomatedKeggBlast\\Data\\Input\\Debaryomyces_occidentalis.fas")


if __name__ == '__main__':
    main()
```
# Output
1. The acquired genes and nucleotide sequences will be exported to fasta files grouped on organism
2. The ran BLAST output will be exported as XML files

All files will be saved to the /Data/Output

