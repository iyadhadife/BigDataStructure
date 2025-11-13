# sharding.py
def shard_distribution(nb_docs, nb_servers):
    """Calcule le nombre moyen de documents par serveur"""
    return nb_docs / nb_servers

def shard_distinct_values(nb_values, nb_servers):
    """Calcule le nombre moyen de valeurs distinctes par serveur"""
    return nb_values / nb_servers

def sharding_stats(collection, collection_name, sharding_key):
    """Affiche les stats de distribution pour une clé de sharding"""
    docs_per_server = shard_distribution(collection.stats[collection_name], collection.stats["servers"])
    values_per_server = shard_distinct_values(collection.stats[sharding_key], collection.stats["servers"])

    print(f"\n=== Sharding {collection_name} - #{sharding_key} ===")
    print(f"Documents par serveur : {docs_per_server:.0f}")
    print(f"Valeurs distinctes par serveur : {values_per_server:.0f}")
