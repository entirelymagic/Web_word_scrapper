from database.databaseConnection import DatabaseConnections


def create_table_webpages_if_not_exist(db):
    """Create a table webpages if it doesnt exist"""
    with DatabaseConnections(f"{db}.db") as connection:
        cursor = connection.cursor()
        sql = f"CREATE TABLE IF NOT EXISTS webpages(" \
              "id integer primary key NOT NULL," \
              "url text NOT NULL," \
              "title text NOT NULL)"
        cursor.execute(sql)


def create_table_keywords_if_not_exist(db):
    """Create a table keywords if it doesnt exist"""
    with DatabaseConnections(f"{db}.db") as connection:
        cursor = connection.cursor()
        sql = "CREATE TABLE IF NOT EXISTS keywords(" \
              "page_id integer primary key NOT NULL ," \
              "word text NOT NULL," \
              "count integer NOT NULL," \
              "significance integer NOT NULL," \
              "FOREIGN KEY (page_id) " \
              "REFERENCES keywords (id) " \
              "ON UPDATE SET NULL ON DELETE NO ACTION)"
        cursor.execute(sql)


def add_to_keywords(db, page_id, word, count, significance):
    """add to table keywords having in"""
    with DatabaseConnections(f"{db}.db") as connection:
        cursor = connection.cursor()

        sql = "INSERT INTO keywords VALUES (?, ?, ?, ?)"
        cursor.execute(sql, (page_id, word, count, significance))


def add_to_webpages(db, url, title):
    with DatabaseConnections(f"{db}.db") as connection:
        cursor = connection.cursor()
        sql = "INSERT INTO webpages VALUES (null, ?, ?)"
        cursor.execute(sql, (url, title))


def search_if_db_empty(db):
    """Check if the DB is empty given a db name.
    If it empty it will return 0"""
    with DatabaseConnections(f"{db}.db") as connection:
        cursor = connection.cursor()
        sql = f"SELECT * FROM webpages, keywords "
        cursor.execute(sql)
        result = [r for r in cursor.fetchall()]
    if not result:  # check if result return a None or a full object
        print(0)
