from db_utils import Database

def make_tables():
    db = Database()
    db.execute("DROP TABLE IF EXISTS word_info;", 0)
    db.execute("""CREATE TABLE word_info
                    (word_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    word TEXT, 
                    definition TEXT,
                    updater TEXT);
                           """, 0)
    db.execute("DROP TABLE IF EXISTS examples;", 0)
    db.execute("""CREATE TABLE examples
                    (word_id INTEGER, 
                    example TEXT);
                            """, 0)
    db.execute("DROP TABLE IF EXISTS updaters;", 0)
    db.execute("""CREATE TABLE updaters
                    (author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT,
                    date DATE);
                            """, 0)
    db.commit()


if __name__ == '__main__':
    make_tables()
