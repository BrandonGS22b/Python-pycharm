import mysql.connector

conexion = mysql.connector.connect(user='root', password='root',
                                    host='localhost',
                                    database='base_peliculas',
                                    port='3307')




print(conexion)