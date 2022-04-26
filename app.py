from settings import engine, insp
from db.tables import create_table
from urls import *


if __name__ == "__main__":
    create_table(engine, insp)
    app.run()

