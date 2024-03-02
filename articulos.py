import sqlite3

class Articulos:

    def abrir(self):
        conexion=sqlite3.connect("C:/Users/Kewsito/Desktop/Dev Projects/Python with sqlite/mi_database.db")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion, bolsa ,precio) values (?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select descripcion, precio from articulos where codigo=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo, descripcion, precio from articulos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()