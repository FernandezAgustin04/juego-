import sqlite3
def crear_tabla():
    with sqlite3.connect("SQL/personaje.db") as conexion:
        try:
            sentencia = ''' create table personajes
            (
            id integer primary key autoincrement,
            nombre text,
            puntaje integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla personajes")
        except sqlite3.OperationalError:
            print("La tabla personajes ya existe")

def crear_personaje():
    with sqlite3.connect("SQL/personaje.db") as conexion:
        try:
            conexion.execute("insert into personajes(nombre,puntaje)values (?,?)", ("jugador",0))
        except sqlite3.OperationalError:
            print("La tabla personajes ya existe")

def traer_id_ultimo():
    try:
        with sqlite3.connect("SQL/personaje.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT MAX(id) FROM personajes')
            resultado = cursor.fetchone()
            id_mayor = resultado[0]
            return(id_mayor)
    except:
        print("Error al traer ultimo id de la tabla")

def ultimo_puntaje(id):
    try:
        with sqlite3.connect("SQL/personaje.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute(f'SELECT puntaje FROM personajes WHERE id={id}')
            resultado = cursor.fetchone()
            ultimo_puntaje = resultado[0]
            return(ultimo_puntaje)
    except:
        print("Error al traer ultimo id de la tabla")

def actualizar_nombre(nombre,id):
    try:
        with sqlite3.connect("SQL/personaje.db") as conexion:
            sentencia = "UPDATE personajes SET nombre = ?  WHERE id=?"
            conexion.execute(sentencia,(nombre,id,))
    except:
        print("Error al actualizar el nombre")

def actualizar_puntos(puntos,id):
    try:
        with sqlite3.connect("SQL/personaje.db") as conexion:
            sentencia = "UPDATE personajes SET puntaje = ?  WHERE id=?"
            conexion.execute(sentencia,(puntos,id,))
    except:
        print("Error al actualizar el nombre")

def ver_puntuacion():
    with sqlite3.connect("SQL/personaje.db") as conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute('SELECT nombre,puntaje FROM personajes ORDER BY puntaje DESC LIMIT 4')
            resultado = cursor.fetchall()
            return resultado
        except :
            print("Error obteniendo puntuacion")
    

crear_tabla()



