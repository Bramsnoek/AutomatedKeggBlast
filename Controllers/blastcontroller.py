import os
from Client import KeggClient
from Enums import BlastType
from Constants import PENTOSE_AND_GLUCURONATE_INTERCONVERSIONS
from Bio.Blast import NCBIXML
import concurrent.futures
import subprocess

class BlastController(object):
    def __init__(self, *organisms, pathway_id = PENTOSE_AND_GLUCURONATE_INTERCONVERSIONS):
        self.__client = KeggClient(*organisms)
        self.__pathway = self.__client.get_pathway(pathway_id)

    def blast(self, blast_type: BlastType, database = "nr", evalue = 0.01, output_dir = "Data/Output"):
        os.makedirs(output_dir, exist_ok=True)
        with open("{}/{}_results.tsv".format(output_dir, blast_type.name), "a") as result_file:
            result_file.write("query\tquery description\torganism\ttitle\tlength\tscore\tbits\texpect\tnum_alignments\tidentities\tpositives\tgaps\tstrand\tframe\tquery\tquery_start\tmatch\tsubject\tsubject_start\talign_length\n")

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.__pathway.get_entries())) as executor:
            blast_result_to_future = {
                executor.submit(self.__blast, blast_type.name, entry, database, evalue, output_dir, blast_type == BlastType.tblastn): entry for entry in self.__pathway.get_entries()
            }

            for future in concurrent.futures.as_completed(blast_result_to_future):
                blastn_future = blast_result_to_future[future]

                try:
                    data = future.result()
                except Exception as e:
                    print("Exception occurred at {}, {}".format(blastn_future, e))
                else:
                    with open("{}/{}_results.tsv".format(output_dir, blast_type.name), "a") as result_file:
                        with open(data, "r") as result_handle:
                            blast_records = NCBIXML.parse(result_handle)

                            for blast_record in blast_records:
                                gene, org = self.__pathway.get_gene_for_id(blast_record.query)
                                print(gene.get_description())
                                for alignment in blast_record.alignments:
                                    for hsp in alignment.hsps:
                                        result_file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n"
                                        .format(blast_record.query, gene.get_description(), org, alignment.title, alignment.length, hsp.score, hsp.bits, hsp.expect, hsp.num_alignments,
                                        hsp.identities, hsp.positives, hsp.gaps, hsp.strand, hsp.frame, hsp.query, hsp.query_start, hsp.match,
                                        hsp.sbjct, hsp.sbjct_start, hsp.align_length))


    def __blast(self, blast_type, entry, database, evalue, output_dir, protein):
            fasta_dir = "{}/{}_genes.fasta".format(output_dir, entry.get_org())
            if protein:
                fasta_dir = "{}/{}_proteins.fasta".format(output_dir, entry.get_org())

            with open(fasta_dir, "w+") as file:
                file.writelines(entry.get_fasta(protein))

            blast = "{} -out {}/{}_blast_result_{}.xml -outfmt 5 -query {}/{}_genes.fasta -db {} -evalue {}".format(
                blast_type, output_dir, entry.get_org(), blast_type, output_dir, entry.get_org(), database, evalue
            )

            process = subprocess.Popen(blast, env=os.environ.copy(), stdout=subprocess.PIPE)
            process.wait()

            return "{}/{}_blast_result_{}.xml".format(output_dir, entry.get_org(), blast_type)
   