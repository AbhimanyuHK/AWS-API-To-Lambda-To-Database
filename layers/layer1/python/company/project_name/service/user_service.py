"""

Created by abhimanyu at 14/07/21

"""

from company.project_name.crud_service.user_dao_service import UserDaoService


class UserService:

    def __init__(self):
        self.user_dao_service = UserDaoService()

    def get_all_users(self):
        return [x.__dict__ for x in self.user_dao_service.get_all_user()]
