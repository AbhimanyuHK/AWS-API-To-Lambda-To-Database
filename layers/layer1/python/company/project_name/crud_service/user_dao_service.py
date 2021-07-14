"""

Created by abhimanyu at 14/07/21

"""

from company.project_name.config.db_config import DBConfig
from company.project_name.model.user import User


class UserDaoService:

    def __init__(self):
        self.session = DBConfig(session_required=True).session

    def get_all_user(self):
        return self.session.query(User).all()

    def get_user_by_id(self):
        return self.session.query(User).filter(User.id == "ed").first()

    def save_user(self, user: User):
        self.session.add(user)
        self.session.commit()

    def get_users_by_dynamic_filters(self, **kwargs):
        user = self.session.query(User)

        if "id" in kwargs and kwargs.get("id"):
            user = user.filter(User.id == kwargs.get("id"))

        if "name" in kwargs and kwargs.get("name"):
            user = user.filter(User.name == kwargs.get("name"))

        return user.all()
