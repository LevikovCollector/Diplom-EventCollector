from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind = migrate_engine)
    info = Table('info', meta, autoload = True)
    sublime_path = Column(String(200))
    sublime_path.name = 'sublime_path'
    sublime_path.create(info)
    pass


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass
