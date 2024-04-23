from data.schema import Patient, database
def create_tables():
    with database:
        database.create_tables([Patient])

def drop_tables():
    with database:
        database.drop_tables([Patient])

if __name__ == '__main__':
    create_tables()
