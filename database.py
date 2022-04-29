from datetime import datetime
from email.policy import default
from click import DateTime
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, String, Integer, DateTime 

engine = create_engine("sqlite:///site.db", echo=False)
meta = MetaData()

settings = Table("settings", meta,
    Column("id", Integer, primary_key=True),
    Column("term", Integer, nullable=False),
    Column("week", Integer, nullable=False),
    Column("term_length", Integer, nullable=False),
    Column('date', DateTime, default=datetime.utcnow)
)

