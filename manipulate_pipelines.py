from example_documents import PIPELINE_STIMULATE_DOCUMENT


def create_pipeline(es, pipeline_id, pipeline, description=""):
    """
    Create a pipeline in Elasticsearch
    :param es:
    :param pipeline_id:
    :param pipeline:
    :param description:
    :return:
    """
    try:
        response = es.ingest.put_pipeline(
            id=pipeline_id,
            description=description,
            processors=pipeline
        )
        return response
    except Exception as exception:
        print(f"Error in create_pipeline: {exception}")
        return None


def delete_pipeline(es, pipeline_id):
    """
    Delete a pipeline in Elasticsearch
    :param es:
    :param pipeline_id:
    :return:
    """
    try:
        response = es.ingest.delete_pipeline(id=pipeline_id)
        return response
    except Exception as exception:
        print(f"Error in delete_pipeline: {exception}")
        return None


def get_pipeline(es, pipeline_id):
    """
    Get a pipeline in Elasticsearch
    :param es:
    :param pipeline_id:
    :return:
    """
    try:
        response = es.ingest.get_pipeline(id=pipeline_id)
        return response
    except Exception as exception:
        print(f"Error in get_pipeline: {exception}")
        return None


def stimulate_pipeline(es, pipeline_id):
    """
    Stimulate a pipeline in Elasticsearch
    :param es:
    :param pipeline_id:
    :return:
    """
    try:
        response = es.ingest.stimulate(id=pipeline_id, docs=[PIPELINE_STIMULATE_DOCUMENT])
        return response
    except Exception as exception:
        print(f"Error in stimulate_pipeline: {exception}")
        return None