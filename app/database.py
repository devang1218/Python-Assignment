import sqlite3

class database():
    def __init__(self, path):
        # Connect to SQLite database (create if necessary)
        self.path = path
        try:
            self.conn = sqlite3.connect(path)
            self.cur = self.conn.cursor()
            self.cur.execute('''CREATE TABLE IF NOT EXISTS addresses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                street TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                zip TEXT NOT NULL,
                latitude REAL NOT NULL,
                longitude REAL NOT NULL
            )''')
            self.conn.commit()
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            exit(1)

    # # Close connection on app exit
    def close_connection(self):
        self.conn.close()
    
    def insert_data(self, address):
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()
        print(address)
        self.cur.execute("INSERT INTO addresses (name, street, city, state, zip, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (address.name, address.street, address.city, address.state, address.zip, address.latitude, address.longitude))
        self.conn.commit()
        
        last_row_id = self.cur.lastrowid
        self.cur.execute("SELECT * FROM addresses WHERE id = ?", (last_row_id,))
        res = self.cur
        
        columns = [column[0] for column in res.description]
        data = [dict(zip(columns, row)) for row in res.fetchall()]

        self.conn.close()
        return data
    
    def get_addresses(self, ids):
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()
        if len(ids) == 1:
            i = f'({ids[0]})'
        else:
            i = str(tuple(ids))
        res = self.cur.execute(f"Select * from Addresses where id in {i}")
        
        columns = [column[0] for column in res.description]
        data = [dict(zip(columns, row)) for row in res.fetchall()]
        self.conn.close()
        return data
    
    def get_lat_lon_list(self):
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()

        res = self.cur.execute("Select id, latitude, longitude from Addresses").fetchall()
        self.conn.close()
        return res