def calc_doc_size(doc, schema=None):
    size = 0
    for key, value in doc.items():
        size += 12  # clé
        if isinstance(value, int) or isinstance(value, float):
            size += 8
        elif isinstance(value, str):
            if len(value) > 100:  # approximation LongString
                size += 200
            else:
                size += 80
        elif isinstance(value, dict):
            size += calc_doc_size(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    size += calc_doc_size(item)
                else:
                    size += 12 + 80  # approximation des valeurs simples
    return size

def calc_collection_size(doc_size, num_docs):
    return doc_size * num_docs  # en bytes
