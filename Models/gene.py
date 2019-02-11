class Gene(object):
    def __init__(self, gene_id, description, nt_sequence):
        self.__gene_id = gene_id
        self.__description = description
        self.__nt_sequence = nt_sequence

    def get_gene_id(self):
        return self.__gene_id

    def get_description(self):
        return self.__description

    def get_nt_sequence(self):
        return self.__nt_sequence

    def __str__(self):
        return "\t\t Gene id: {} | {} \n".format(self.__gene_id, self.__description)