"""

Created by abhimanyu at 14/07/21

"""

from sqlalchemy import Column, Integer, String

from company.project_name.config.db_config import DBConfig


class User(DBConfig.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
