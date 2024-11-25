"""
Execute elasticsearch in local using docker command:

docker run -p 127.0.0.1:9200:9200 -d --name elasticsearch \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  -v "elasticsearch-data:/usr/share/elasticsearch/data" \
  docker.elastic.co/elasticsearch/elasticsearch:8.15.0
"""

# Connect with Elasticsearch using python

from elasticsearch import Elasticsearch


def connect_elasticsearch():
    """
    Connect with Elasticsearch
    :return: object
    """
    elasticsearch_connection_object = Elasticsearch("http://localhost:9200")
    if not elasticsearch_connection_object:
        print("It could not connect")
    return elasticsearch_connection_object