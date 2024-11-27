LOWERCASE_PIPELINE = {
    "lowercase": {
        "field": "address",
        "on_failure": [
            {
                "set": {
                    "field": "address",
                    "value": "An error occurred while processing the address field",
                    "ignore_failure": True
                }
            }
        ]
    }
}