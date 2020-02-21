import conn

class Conta:
    numero = 0
    tipo = 0
    dono = ''
    saldo = 0
    status = False
    pass


def pegaRegistro(obj):
    cursor = conn.connection()
    cursor.execute('SELECT * FROM Conta WHERE numero = ?',obj.numero)

    reader = cursor.fetchone()
    if reader:
        obj.tipo = reader[1]
        obj.dono = reader[2]
        obj.saldo = reader[3]
        obj.status = reader[4]

    cursor.close()
        
    
def checaNumero(obj):
    cursor = conn.connection()
    cursor.execute('SELECT numero FROM Conta WHERE numero = ?',obj.numero)

    reader = cursor.fetchone()

    x = False
    if reader:
        x = True
        
    cursor.close()
    return x

def criarConta(obj):
    cursor = conn.connection()
    cursor.execute('INSERT INTO Conta VALUES (?,?,?,?,?)',
                   obj.numero, obj.tipo, obj.dono, obj.saldo, obj.status)

    cursor.commit()
    cursor.close()

def abrirConta(obj):
    if (obj.status == False):
        obj.status = True

        if (obj.tipo == 1):
            obj.saldo = 50
        else:
            obj.saldo = 150

        cursor = conn.connection()
        cursor.execute('UPDATE Conta SET status = 1, saldo = ? WHERE numero = ?',
                       obj.saldo, obj.numero)

        cursor.commit()
        cursor.close()
    
        return True
    return False
    
def fecharConta(obj):
    if (obj.saldo == 0):
        obj.status = False

        cursor = conn.connection()
        cursor.execute('UPDATE Conta SET status = 0 WHERE numero = ?', obj.numero)

        cursor.commit()
        cursor.close()
        
        return True
    return False

def depositar(obj, x):
    if (x > 0):
        obj.saldo += x

        cursor = conn.connection()
        cursor.execute('UPDATE Conta SET saldo = ? WHERE numero = ?',
                       obj.saldo, obj.numero)

        cursor.commit()
        cursor.close()
        
        return True
    return False
    
def sacar(obj, x):
    if (x <= obj.saldo):
        obj.saldo -= x

        cursor = conn.connection()
        cursor.execute('UPDATE Conta SET saldo = ? WHERE numero = ?',
                       obj.saldo, obj.numero)

        cursor.commit()
        cursor.close()
        
        return True
    return False
    
def pagarMensal(obj):
    if (obj.tipo == 1):
        obj.saldo -= 12
    else:
        obj.saldo -= 20

    cursor = conn.connection()
    cursor.execute('UPDATE Conta SET saldo = ? WHERE numero = ?',
                       obj.saldo, obj.numero)
    cursor.commit()
    cursor.close()
