import DB as database

def main():
    db = database.DB() # Se crea si no existe la DB
    db.create_tables() # Se cargan las tablas si no existen
    db.close_connection()
    
if __name__ == "__main__":
    main()