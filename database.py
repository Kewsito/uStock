import sqlite3

def crear_tabla(nombre_db):
    conexion = sqlite3.connect(nombre_db)
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articulos(
            id INTEGER PRIMARY KEY NOT NULL,
            descripcion TEXT NOT NULL,
            marca TEXT,
            talle TEXT NOT NULL,
            bolsa TEXT NOT NULL,
            precio DECIMAL NOT NULL
        )
    ''')

    print("Tabla creada con éxito.")
    conexion.close()


