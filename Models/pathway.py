from .gene import Gene

class Pathway(object):
    def __init__(self, pathway_id, entries):
        self.__pathway_id = pathway_id
        self.__entries = entries

    def get_pathway_id(self):
        return self.__pathway_id

    def get_entries(self):
        return self.__entries

    def get_gene_for_id(self, gene_id):
        for entry in self.__entries:
            gene = entry.get_gene_for_id(gene_id)

            if gene is not None:
                return gene, entry.get_org()

        return Gene("", "", "", "")

    def __str__(self):
        return "Pathway ID: {} \n {}".format(self.__pathway_id, ''.join(str(entry) for entry in self.__entries))
