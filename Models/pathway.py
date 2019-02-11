class Pathway(object):
    def __init__(self, pathway_id, entries):
        self.__pathway_id = pathway_id
        self.__entries = entries

    def get_pathway_id(self):
        return self.__pathway_id

    def get_entries(self):
        return self.__entries

    def __str__(self):
        return "Pathway ID: {} \n {}".format(self.__pathway_id, ''.join(str(entry) for entry in self.__entries))
