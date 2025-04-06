import sqlite3



class ConnectionDB():
    def __init__(self):
        self.db = r"path a tu db" #Si no existe crea la db en el path que se le pase
        
       
    def create_connection(self):
       
        conn = None
        try:
            conn = sqlite3.connect(self.db)
            return conn
        except sqlite3.Error as e:
            print(e)

        return conn

    def commit_and_close_connection(self, connection):
        try:
            if connection:
                connection.commit()
                connection.close()
                print("La conexión se cerró correctamente.")
        except sqlite3.Error as e:
            print(e)    
            
class DB():
    def __init__(self):
        self.connection = ConnectionDB()
        self.conn = self.connection.create_connection()
        self.cur = self.conn.cursor()
   
    def close_connection(self):
        self.connection.commit_and_close_connection(self.conn)
   
    def create_table(self, create_table_sql):
        try:
            self.cur.execute(create_table_sql)
            print(f"Se creo la tabla {create_table_sql} correctamente")
        except sqlite3.Error as e:
            print(e)

    def delete_content_table(self, tabla):
        try:
            self.cur.execute(f"DROP TABLE {tabla}")
        except sqlite3.Error as e:
            print(e)
           
    def delete_table(self, tabla):
        try:
            self.cur.execute(f"DELETE FROM {tabla}")
        except sqlite3.Error as e:
            print(e)
            
            
    def create_table_servidor(self):
        servidor =  """CREATE TABLE IF NOT EXISTS Servidor (
                                                id TEXT PRIMARY KEY,
                                                nombre TEXT
                                            );"""
        self.create_table(servidor)
        
    def create_table_canal_servidor(self):
        canal =  """CREATE TABLE IF NOT EXISTS Canal_Servidor (
                                                id TEXT PRIMARY KEY,
                                                nombre TEXT,
                                                id_servidor TEXT,
                                                FOREIGN KEY (id_servidor) REFERENCES Servidor(id)
                                            );"""
        self.create_table(canal)
    
    def create_table_token(self):
        token =  """CREATE TABLE IF NOT EXISTS Token (
                                                id TEXT PRIMARY KEY,
                                                nombre_bot TEXT
                                            );"""
        self.create_table(token)
        

    def create_tables(self):
        try:
            self.create_table_servidor()
            self.create_table_canal_servidor()
            self.create_table_token()
        except sqlite3.Error as e:
            print(e)
        
    
    def load_servidor(self, id_servidor, nombre_servidor):
        try:
            self.cur.execute('''
                    INSERT INTO Servidor (id, nombre)
                    VALUES (?, ?)
            ''', (id_servidor, nombre_servidor))
        except sqlite3.Error as e:
            print(e)

    def load_canal_servidor(self, id_canal, nombre_canal, id_serv):
        try:
            id_servidor = self.get_id_servidor(id_serv)
            self.cur.execute('''
                    INSERT INTO Canal_Servidor (id, nombre, id_servidor)
                    VALUES (?, ?, ?)
            ''', (id_canal, nombre_canal, id_servidor))
        except sqlite3.Error as e:
            print(e)
            
    def load_token(self, id_token, nombre_bot):
        try:
            self.cur.execute('''
                    INSERT INTO TOKEN (id, nombre_bot)
                    VALUES (?, ?)
            ''', (id_token, nombre_bot))
        except sqlite3.Error as e:
            print(e)
            
    def get_id_servidor(self, id_servidor):
        try:
            self.cur.execute('''
                    SELECT id FROM Servidor WHERE id = ?
            ''', (id_servidor,))
            row = self.cur.fetchone()
            id = row[0]
            return id
        except sqlite3.Error as e:
            print(e)
            
    def get_id_canal_servidor(self, nombre_canal, id_servidor):
        try:
            self.cur.execute('''
                    SELECT id FROM Canal_Servidor WHERE nombre = ? AND id_servidor = ?
            ''', (nombre_canal, id_servidor))
            row = self.cur.fetchone()
            id = row[0]
            return id
        except sqlite3.Error as e:
            print(e)
            
    def get_token(self, nombre_bot):
        try:
            self.cur.execute('''
                    SELECT id FROM Token WHERE nombre_bot = ?
            ''', (nombre_bot, ))
            row = self.cur.fetchone()
            id = row[0]
            return id
        except sqlite3.Error as e:
            print(e)