import sqlite3
import argparse

def create_db(conn):
    pp = conn.cursor()
    pp.executescript('drop table if exists users;')

    try:
        pp.executescript("begin")
        pp.executescript("""
        CREATE TABLE uv
            (id INTEGER PRIMARY KEY, variant VARCHAR(100), time INTEGER , uvlevel INTEGER, type VARCHAR(100));
        """)
        pp.executescript("commit")
        return True
    except conn.Error as e:
        pp.executescript("rollback")
        print(e.args[0])
        return False



def main():
    parser = argparse.ArgumentParser(description='creates db tables required for primer program')
    parser.add_argument('--db')

    args = parser.parse_args()

    db = args.db
    print(db)

    conn_main = sqlite3.connect(db)
    complete = create_db(conn_main)


if __name__ == '__main__':
    main()