class PathwayEntry(object):
    def __init__(self, org, genes):
        self.__org = org
        self.__genes = genes

    def get_org(self):
        return self.__org

    def get_gene_for_id(self, gene_id):
        for gene in self.__genes:
            if gene.get_gene_id() == gene_id:
                return gene

    def __str__(self):
        return "\n\t Organism: {} \n {}".format(self.__org, ''.join(str(gene) for gene in self.__genes))

    def get_fasta(self, protein):
        if protein:
            return self.__get_aa_fasta()
        else:
            return self.__get_nc_fasta()

    def __get_nc_fasta(self):
        return ''.join(">{}\n{}\n".format(x.get_gene_id(), x.get_nt_sequence()) for x in self.__genes)

    def __get_aa_fasta(self):
        return ''.join(">{}\n{}\n".format(x.get_gene_id(), x.get_aa_sequence()) for x in self.__genes)

