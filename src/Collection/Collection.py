class Collection:
    def __init__(self, name, properties,stats):
        self.name = name
        self.properties = properties  # dictionnaire {clé: type}
        self.stats = stats  # ex: {"nb_docs": 100000, "avg_categories": 2}
        self.doc_size = 0
        self.nb_docs = 0
