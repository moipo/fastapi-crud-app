from sqlalchemy import MetaData, Table
from database import engine

metadata_obj = MetaData()
some_table = Table("tasks", metadata_obj, autoload_with=engine)
print(repr(some_table))
