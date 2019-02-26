from Controllers import BlastController
from Enums import BlastType

def main():
    #Change these to the actual organism id's of the 6 biodiesel project bacteria
    #Y. lipolytica => yli
    #D. hansenii => bhan
    #K. lactis => kla
    #C. albicans => cal
    blastController = BlastController('yli', 'bhan', 'kla', 'cal')
    blastController.blast(blast_type=BlastType.tblastn, database="C:\\Users\\brams\\Documents\\AutomatedKeggBlast\\Data\\Input\\Debaryomyces_occidentalis.fas")


if __name__ == '__main__':
    main()
