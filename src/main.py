from schema_parser import load_schema, load_stats
from size_calculator import calc_doc_size, calc_collection_size
from sharding import shard_distribution, shard_distinct_values
from Collection.Collection import Collection
from sharding import sharding_stats



def main():


    # Charger le schema JSON
    product_schema = load_schema("schema.json")
    stats = load_stats("stats.json")

    #print("Schema chargé:", product_schema["properties"])
    product_struct = Collection(
        name="Product",
        properties=product_schema["properties"],
        stats=stats
    )    
    print("Propriétés :", list(product_struct.properties.keys()))

    print(stats["clients"])

    # Exemple de sharding : OrderLine shardée par IDP
    sharding_stats(product_struct,"orderlines", "clients")



if __name__ == "__main__":
    main()