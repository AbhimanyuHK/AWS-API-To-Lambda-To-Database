"""

Created by abhimanyu at 14/07/21

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


class DBConfig:
    Base = declarative_base()
    session = None

    def __init__(self, session_required=False):
        self.engine = create_engine('sqlite:///:memory:', echo=True)

        if session_required:
            DBConfig.session = self.create_session()

    def create_session(self):
        if not DBConfig.session:
            DBConfig.session = sessionmaker(bind=self.engine)()
        return DBConfig.session
