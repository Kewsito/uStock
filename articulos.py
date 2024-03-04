import sqlite3

class Articulos:

    def abrir(self):
        conexion=sqlite3.connect("C:/Users/Kewsito/Desktop/CODIGO/uStock/mi_database.db")
        print(conexion)
        if conexion!=None:
            print("Conexión establecida")
        else:
            print("Conexión no establecida")
        return conexion

    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulos(descripcion,marca ,talle, precio ,bolsa) values (?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select descripcion, precio from articulos where id=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select * from articulos"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
    
    def modificar_precio(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "update articulos set precio=? where id=?"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    
    def detalles_producto(self, id):
        try:
            cone = self.abrir()
            
            cursor = cone.cursor()
            sql = "select * from articulos where id=?"
            cursor.execute(sql, (id,))
            return cursor.fetchall()
        finally:
            cone.close()