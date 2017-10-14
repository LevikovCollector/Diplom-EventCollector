from sqlalchemy import MetaData, Table, Column, Boolean



def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(migrate_engine)
    info = Table('info', meta, autoload = True)
    send_status = Column('send_status', Boolean())
    send_status.create(info)



def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass
