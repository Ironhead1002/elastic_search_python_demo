def create_elasticsearch_index(es, index_name, number_of_shards, number_of_replicas, mapping=None):
    """
    Create an index in Elasticsearch
    :param es:
    :param index_name:
    :param number_of_shards:
    :param number_of_replicas:
    :param mapping:
    :return:
    """
    try:
        # Delete and Create index with 3 shards and 2 replicas
        es.indices.delete(index=index_name, ignore_unavailable=True)

        if mapping:
            es.indices.create(
                index=index_name,
                settings={
                    "index": {
                        "number_of_shards": number_of_shards,
                        "number_of_replicas": number_of_replicas
                    }
                },
                mappings=mapping
            )
        else:
            es.indices.create(
                index=index_name,
                settings={
                    "index": {
                        "number_of_shards": number_of_shards,
                        "number_of_replicas": number_of_replicas
                    }
                }
            )
        print(f"Index {index_name} created successfully")
    except Exception as exception:
        print(f"Error in create_elasticsearch_index: {exception}")


def delete_index(es, index_name):
    """
    Delete an index in Elasticsearch
    :param es:
    :param index_name:
    :return:
    """
    try:
        response = es.indices.delete(index=index_name, ignore_unavailable=True)
        return response
    except Exception as exception:
        print(f"Error in delete_index: {exception}")
        return None


def get_mapping_of_index(es, index_name):
    """
    Get the mapping of an index
    :param es:
    :param index_name:
    :return:
    """
    try:
        mapping = es.indices.get_mapping(index=index_name)
        return mapping
    except Exception as exception:
        print(f"Error in get_mapping_of_index: {exception}")
