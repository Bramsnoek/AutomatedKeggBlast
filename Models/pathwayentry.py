class PathwayEntry(object):
    def __init__(self, org, genes):
        self.__org = org
        self.__genes = genes

    def get_org(self):
        return self.__org

    def __str__(self):
        return "\n\t Organism: {} \n {}".format(self.__org, ''.join(str(gene) for gene in self.__genes))

    def get_nc_fasta(self):
        return ''.join(">{}:{} {}\n{}\n".format(self.__org, x.get_gene_id(), x.get_description(), x.get_nt_sequence()) for x in self.__genes)

    def get_aa_fasta(self):
        return ''.join(">{}:{} {}\n{}\n".format(self.__org, x.get_gene_id(), x.get_description(), x.get_aa_sequence()) for x in self.__genes)

