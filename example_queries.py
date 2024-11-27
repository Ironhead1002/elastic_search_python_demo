"""
This file contains example queries that can be used to query the database, Keeping following document in mind:
{
    "name": "John Doe",
    "age": 25,
    "address": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip": "10001",
    "created_at": "2022-01-01T00:00:00"
}
"""

# Will Return All Documents
QUERY_ONE = {}

# Will Return All Documents with name John Doe
QUERY_TWO = {
    "query": {
        "match": {
            "name": "John Doe"
        }
    }
}

# Will Return All Documents with name John in them
QUERY_THREE = {
    "query": {
        "match": {
            "name": "John"
        }
    }
}

# Will Return All Documents with created_at date greater than or equal to 2022-01-01T00:00:00
QUERY_FOUR = {
    "query": {
        "range": {
            "created_at": {
                "gte": "2022-01-01T00:00:00"
            }
        }
    }
}

# Will Return All Documents with bool query with name John Doe and created_at date greater than or equal to 2022-01-01T00:00:00
QUERY_FIVE = {
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "name": "John"
                    }
                },
                {
                    "range": {
                        "created_at": {
                            "gte": "2022-01-01T00:00:00"
                        }
                    }
                }
            ]
        }
    }
}

# Will Return All documents with size and skip 10 documents with timeout 10 seconds
QUERY_SIX = {
    "query": {
        "match_all": {}
    },
    "from": 10,
    "size": 10,
    "timeout": "10s"
}

# Will Return All average age of all documents
QUERY_SEVEN = {
    "query": {
        "match_all": {}
    },
    "aggs": {
        "average_age": {
            "avg": {
                "field": "age"
            }
        }
    }
}

FINAL_QUERY = QUERY_SEVEN