shared_responses = {
    401: {
        "description": "Authentication Error",
        "content": {
            "application/json": {
                "example": {"message": "Could not authenticate user."}
            }
        },
    },
    404: {
        "description": "User Not Found Error",
        "content": {
            "application/json": {"example": {"message": "User not found."}}
        },
    },
}

get_profile_responses = {401: shared_responses[401]}

update_password_responses = {
    400: {
        "description": "Bad Request Error",
        "content": {
            "application/json": {
                "example": {
                    "message": "Please check your credentials and try again."
                }
            }
        },
    },
    401: shared_responses[401],
    404: shared_responses[404],
}

update_profile_responses = {401: shared_responses[401]}
