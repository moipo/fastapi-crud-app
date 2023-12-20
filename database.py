from sqlalchemy import create_engine, insert, Insert, Compiled
from tables import tasks
engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5434/todoappdb",
    connect_args={"options": "-c timezone=utc"},
    echo=True,
)

stmt: Insert = insert(tasks).values(title='titile', description='description')
compiled: Compiled = stmt.compile()
params: dict = compiled.params



