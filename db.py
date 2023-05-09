import os
import psycopg2
import psycopg2.extras
import urllib.parse

class numDB:

    def __init__(self):
        #self.connection = sqlite3.connect("cart_db.db")
        #self.connection.row_factory = dict_factory

        urllib.parse.uses_netloc.append("postgres")
        url = urllib.parse.urlparse(os.environ["DATABASE_URL"])

        self.connection = psycopg2.connect(
            cursor_factory=psycopg2.extras.RealDictCursor,
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def createTable(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS db (num INTEGER)")
        self.connection.commit()

    def createItem(self, num):
        # INSERT record into table
        data = [num]
        self.cursor.execute("INSERT INTO db (num) VALUES (%s)", data)
        self.connection.commit()

    def getDB(self):
        # read all records from table
        self.cursor.execute("SELECT * FROM db")
        records = self.cursor.fetchall()
        return records
    
    def getOne(self, num):
        data = [num]
        # Query the database for a matching record
        self.cursor.execute("SELECT * FROM db WHERE num = (%s)", data)

        # Fetch the result
        result = self.cursor.fetchone()

        # Check if a matching record was found
        if result is not None:
            #A record with the same num already exists in the database
            return True
        else:
            # it is a new record
            return False
