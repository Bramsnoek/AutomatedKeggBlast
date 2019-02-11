from Controllers import BlastController
#https://www.ncbi.nlm.nih.gov/books/NBK279688/

def main():
    blastController = BlastController('hsa',
                                      'bta',
                                      'phd')

    blastController.Blastn(database="C:\\Users\\bram\\PycharmProjects\\\AutomatedKeggBlast\\Data\\Input\\Debaryomyces_occidentalis.fas")


if __name__ == '__main__':
    main()
