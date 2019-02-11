from Client import KeggClient
from Constants import PENTOSE_AND_GLUCURONATE_INTERCONVERSIONS
from Bio.Blast.Applications import NcbiblastnCommandline
import concurrent.futures

class BlastController(object):
    def __init__(self, *organisms, pathway_id = PENTOSE_AND_GLUCURONATE_INTERCONVERSIONS):
        self.__client = KeggClient(*organisms)
        self.__pathway = self.__client.get_pathway(pathway_id)

        print(str(self.__pathway))
