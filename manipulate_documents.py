def insert_document(es, index_name, document):
    """
    Insert a document into an index
    :param es:
    :param index_name:
    :param document:
    :return:
    """
    try:
        response = es.index(index=index_name, body=document)
        return response
    except Exception as exception:
        print(f"Error in insert_document: {exception}")
        return None

def insert_document_with_pipeline(es, index_name, document, pipeline_id):
    """
    Insert a document into an index
    :param es:
    :param index_name:
    :param document:
    :return:
    """
    try:
        response = es.index(index=index_name, body=document, pipeline=pipeline_id)
        return response
    except Exception as exception:
        print(f"Error in insert_document: {exception}")
        return None


def delete_document(es, index_name, document_id):
    """
    Delete a document from an index
    :param es:
    :param index_name:
    :param document_id:
    :return:
    """
    try:
        response = es.delete(index=index_name, id=document_id)
        return response
    except Exception as exception:
        print(f"Error in delete_document: {exception}")
        return None

def get_document(es, index_name, document_id):
    """
    Get a document from an index
    :param es:
    :param index_name:
    :param document_id:
    :return:
    """
    try:
        response = es.get(index=index_name, id=document_id)
        return response
    except Exception as exception:
        print(f"Error in get_document: {exception}")
        return None


def update_document(es, index_name, document_id):
    """
    Update a document in an index
    :param es:
    :param index_name:
    :param document_id:
    :return:
    """
    try:
        response = es.update(index=index_name, id=document_id, script={
            "source": "ctx._source.name = params.name",
            "params": {
                "name": "Scarlet Johnson"
            }
        })
        return response
    except Exception as exception:
        print(f"Error in update_document: {exception}")
        return None


def add_new_field(es, index_name, document_id):
    """
    Add a new field to a document in an index
    :param es:
    :param index_name:
    :param document_id:
    :return:
    """
    try:
        response = es.update(index=index_name, id=document_id, script={
            "source": "ctx._source.new_field = 'new_value'"
        })
        return response
    except Exception as exception:
        print(f"Error in add_new_field: {exception}")
        return None


def remove_field(es, index_name, document_id):
    """
    Remove a field from a document in an index
    :param es:
    :param index_name:
    :param document_id:
    :return:
    """
    try:
        response = es.update(index=index_name, id=document_id, script={
            "source": "ctx._source.remove('new_field')"
        })
        return response
    except Exception as exception:
        print(f"Error in remove_field: {exception}")
        return None


def search_documents(es, index_name, query):
    """
    Search documents in an index
    :param es:
    :param index_name:
    :param query:
    :return:
    """
    try:
        response = es.search(index=index_name, body=query)
        return response
    except Exception as exception:
        print(f"Error in search_documents: {exception}")
        return None
