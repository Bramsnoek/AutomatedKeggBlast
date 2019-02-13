import os
from Client import KeggClient
from Enums import BlastType
from Constants import PENTOSE_AND_GLUCURONATE_INTERCONVERSIONS
import concurrent.futures
import subprocess

class BlastController(object):
    def __init__(self, *organisms, pathway_id = PENTOSE_AND_GLUCURONATE_INTERCONVERSIONS):
        self.__client = KeggClient(*organisms)
        self.__pathway = self.__client.get_pathway(pathway_id)
        
        for entry in self.__pathway.get_entries():
            print(entry.get_aa_fasta())

    def blast(self, blast_type: BlastType, database = "nr", evalue = 0.01, output_dir = "Data/Output"):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.__pathway.get_entries())) as executor:
            blast_result_to_future = {
                executor.submit(self.__blast, blast_type.name, entry, database, evalue, output_dir): entry for entry in self.__pathway.get_entries()
            }

            for future in concurrent.futures.as_completed(blast_result_to_future):
                blastn_future = blast_result_to_future[future]

                try:
                    data = future.result()
                except Exception as e:
                    print("Exception occurred at {}, {}".format(blastn_future, e))
                else:
                    print(data)

    def __blast(self, blast_type, entry, database, evalue, output_dir):
            fasta_dir = "{}/{}_genes.fasta".format(output_dir, entry.get_org())
            with open(fasta_dir, "w+") as file:
                file.writelines(entry.get_nc_fasta())

            blastn = "{} -out {}/{}_blast_result.xml -outfmt 5 -query {}/{}_genes.fasta -db {} -evalue {}".format(
                blast_type, output_dir, entry.get_org(), output_dir, entry.get_org(), database, evalue
            )

            process = subprocess.Popen(blastn, env=os.environ.copy(), stdout=subprocess.PIPE)

            return "{}/{}_blast_result_{}.xml".format(output_dir, entry.get_org(), blast_type)
   