class PathwayEntry(object):
    def __init__(self, org, genes):
        self.__org = org
        self.__genes = genes

    def __get_org(self):
        return self.__org

    def __str__(self):
        return "\n\t Organism: {} \n {}".format(self.__org, ''.join(str(gene) for gene in self.__genes))