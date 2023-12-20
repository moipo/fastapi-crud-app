from datetime import datetime, UTC

from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, DateTime, ForeignKey, Text

from database import engine

metadata_obj = MetaData()

users = Table(
    'users',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('created_at', DateTime(), default=datetime.now(tz=UTC)),
)

tasks = Table(
    'tasks',
    metadata_obj,
    Column('task_id', Integer, primary_key=True),
    Column('title', String(50), nullable=False),
    Column('description', Text),
    Column('is_checked', Boolean, default=False),
    Column('user_id', Integer, ForeignKey('users.user_id'), nullable=False ),
    Column('created_at', DateTime(), default=datetime.now(tz=UTC)),
    Column('updated_at', DateTime()),
)

metadata_obj.create_all(engine)