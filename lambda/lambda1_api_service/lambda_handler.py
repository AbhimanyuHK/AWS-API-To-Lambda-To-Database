"""

Created by abhimanyu at 14/07/21

"""

import json

from company.project_name.service.user_service import UserService


def handler(event, context):
    if event["resource"] == "/user":
        users = UserService().get_all_users()

        return {
            "statusCode": 200,
            "body": json.dumps(users, default=lambda x: str(x))
        }

    return {
        "statusCode": 400,
        "body": json.dumps("Bad Request", default=lambda x: str(x))
    }
