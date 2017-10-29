from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///info.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


class Info_Data(Base):
    __tablename__ = 'info'
    id = Column(Integer, primary_key = True)
    app_name = Column(String(50))
    active_tab_url = Column(String(200))
    timestamp = Column(DateTime)
    pycharm_project = Column(String(100))
    sublime_path = Column(String(200))
    send_status = Column(Boolean())

    def __init__(self, app_name = None, active_tab_url = None, timestamp = None, pycharm_project = None, sublime_path = None, send_status = 0):
        self.app_name = app_name
        self.active_tab_url = active_tab_url
        self.timestamp = timestamp
        self.pycharm_project = pycharm_project
        self.sublime_path = sublime_path
        self.send_status = send_status

    def __repr__(self):
        return '<info {} {} {} {} {} {}>'.format(self.app_name, self.active_tab_url, self.timestamp, self.pycharm_project, self.sublime_path, self.send_status)

if __name__ == "__main__":
    #Создает базу данных
    Base.metadata.create_all(bind=engine)