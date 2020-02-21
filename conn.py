import pyodbc

def connection():
    server = 'LAPTOP-JJ2FBRH8\SQLEXPRESS'
    database = 'db_contaBanco'

    stringConexao = 'Driver={SQL Server Native Client 11.0}; Server=' + server + ';Database=' + database + ';Trusted_Connection=yes;'

    cn = pyodbc.connect(stringConexao)
    return cn.cursor()
