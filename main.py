from elastic_search_connection import connect_elasticsearch
from manipulate_indexes import create_elasticsearch_index, get_mapping_of_index
from manipulate_documents import (
    insert_document,
    delete_document,
    get_document,
    update_document,
    add_new_field,
    remove_field,
    search_documents,
    insert_document_with_pipeline
)
from manipulate_pipelines import create_pipeline, delete_pipeline, get_pipeline
from example_queries import FINAL_QUERY
from example_mapping import VECTOR_FIELD_MAPPING
from example_documents import DOCUMENT, DENSE_VECTOR_DOCUMENT
from example_pipelines import LOWERCASE_PIPELINE
import pprint

INDEX = "my_index"
VECTOR_INDEX = "my_vector_index"
PIPELINE = "lowercase_pipeline"

elasticsearch_connection = connect_elasticsearch()


def index_create_example():
    """
    This function is used to demonstrate the index create example
    :return:
    """
    if not elasticsearch_connection.indices.exists(index=INDEX):
        create_elasticsearch_index(elasticsearch_connection, INDEX, 3, 2)


def index_create_with_vector_field_example():
    """
    This function is used to demonstrate the index create example with vector field
    :return:
    """
    if not elasticsearch_connection.indices.exists(index=VECTOR_INDEX):
        create_elasticsearch_index(elasticsearch_connection, VECTOR_INDEX, 3, 2, VECTOR_FIELD_MAPPING)


def document_create_example():
    """
    This function is used to demonstrate the document create example
    :return:
    """
    response = insert_document(elasticsearch_connection, INDEX, DOCUMENT)
    print(response)


def document_create_example_with_pipeline():
    """
    This function is used to demonstrate the document create example
    :return:
    """
    response = insert_document_with_pipeline(elasticsearch_connection, INDEX, DOCUMENT, PIPELINE)
    print(response)


def dense_vector_document_create_example():
    """
    This function is used to demonstrate the document create example with dense vector
    :return:
    """
    response = insert_document(elasticsearch_connection, VECTOR_INDEX, DENSE_VECTOR_DOCUMENT)
    print(response)


def document_delete_example():
    """
    This function is used to demonstrate the document delete example
    :return:
    """
    response = insert_document(elasticsearch_connection, INDEX, DOCUMENT)

    response = delete_document(elasticsearch_connection, INDEX, response["_id"])
    print(response)


def get_mapping_example():
    """
    This function is used to demonstrate the get mapping example
    :return:
    """
    insert_document(elasticsearch_connection, INDEX, DOCUMENT)

    mapping = get_mapping_of_index(elasticsearch_connection, INDEX)
    pprint.pprint(mapping)


def get_document_example():
    """
    This function is used to demonstrate the get document example
    :return:
    """
    response = insert_document(elasticsearch_connection, INDEX, DOCUMENT)

    response = get_document(elasticsearch_connection, INDEX, response["_id"])
    pprint.pprint(response)


def update_document_example():
    """
    This function is used to demonstrate the update document example
    :return:
    """
    response = insert_document(elasticsearch_connection, INDEX, DOCUMENT)
    response = get_document(elasticsearch_connection, INDEX, response["_id"])

    response = update_document(elasticsearch_connection, INDEX, response["_id"])
    response = get_document(elasticsearch_connection, INDEX, response["_id"])
    pprint.pprint(response)


def check_document_exists():
    """
    This function is used to check if a document exists
    :return:
    """
    response = insert_document(elasticsearch_connection, INDEX, DOCUMENT)
    response = get_document(elasticsearch_connection, INDEX, response["_id"])
    pprint.pprint(response)


def add_new_field_example():
    """
    This function is used to add a new field to a document
    :return:
    """
    response = insert_document(elasticsearch_connection, INDEX, DOCUMENT)
    response = add_new_field(elasticsearch_connection, INDEX, response["_id"])
    pprint.pprint(response)


def remove_field_example():
    """
    This function is used to remove a field from a document
    :return:
    """
    response = insert_document(elasticsearch_connection, INDEX, DOCUMENT)
    response = remove_field(elasticsearch_connection, INDEX, response["_id"])
    pprint.pprint(response)


def search_documents_example():
    """
    This function is used to search documents
    :return:
    """
    response = search_documents(elasticsearch_connection, INDEX, FINAL_QUERY)
    print(f"The query returned {response['hits']['total']['value']} Documents")


def create_pipeline_example():
    """
    This function is used to demonstrate the create pipeline example
    :return:
    """
    response = create_pipeline(elasticsearch_connection, PIPELINE, [LOWERCASE_PIPELINE])
    print(response)


def stimulate_pipeline_example():
    """
    This function is used to stimulate the pipeline example
    :return:
    """
    response = insert_document(elasticsearch_connection, INDEX, DOCUMENT)
    print(response)

    response = elasticsearch_connection.index(index=INDEX, body=DOCUMENT, pipeline=PIPELINE)
    print(response)


def get_pipeline_example():
    """
    This function is used to demonstrate the get pipeline example
    :return:
    """
    response = get_pipeline(elasticsearch_connection, PIPELINE)
    print(response)


def delete_pipeline_example():
    """
    This function is used to demonstrate the delete pipeline example
    :return:
    """
    response = delete_pipeline(elasticsearch_connection, PIPELINE)
    print(response)


def work_with_simple_indexes():
    index_create_example()
    document_create_example()
    document_delete_example()
    get_mapping_example()
    get_document_example()
    check_document_exists()
    update_document_example()
    add_new_field_example()
    remove_field_example()
    search_documents_example()


def work_with_vector_indexes():
    index_create_with_vector_field_example()
    dense_vector_document_create_example()


def work_with_pipelines():
    create_pipeline_example()
    stimulate_pipeline_example()
    get_pipeline_example()
    document_create_example_with_pipeline()
    delete_pipeline_example()


if __name__ == "__main__":
    work_with_simple_indexes()
    work_with_vector_indexes()
    work_with_pipelines()