from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5434/todoappdb",
    echo=True,
)

with engine.connect() as conn:
    result = conn.execute(text("select * from tasks;"))
    print(result.all())
