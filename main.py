from Controllers import BlastController

def main():
    #Change these to the actual organism id's of the 6 biodiesel project bacteria
    blastController = BlastController('hsa',
                                      'bta',
                                      'phd')

    blastController.blastn(database="C:\\Users\\bram\\PycharmProjects\\\AutomatedKeggBlast\\Data\\Input\\Debaryomyces_occidentalis.fas")


if __name__ == '__main__':
    main()
