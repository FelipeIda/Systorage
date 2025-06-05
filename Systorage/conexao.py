import mysql.connector

class Conexao:
    def __init__(self): 
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="systorage"
            )
            print("Conexão estabelecida com sucesso.")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            self.db = None

    def gravar(self, sql, params=None):  
        if self.db is None:
            print("Erro: Banco de dados não conectado.")
            return False
        try:
            cur = self.db.cursor()
            cur.execute(sql, params or ())
            self.db.commit()
            cur.close()
            return True
        except mysql.connector.Error as e:
            print(f"Erro ao gravar dados: {e}")
            return False

    def consultar(self, sql, params=None):
        if self.db is None:
            print("Erro: Banco de dados não conectado.")
            return []
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, params or ())
            resultados = cursor.fetchall()
            return resultados if resultados else []
        except mysql.connector.Error as e:
            print(f"Erro ao consultar: {e}")
            return []
        finally:
            cursor.close()

    def consultar_tree(self, sql, params=None):
        if self.db is None:
            print("Erro: Banco de dados não conectado.")
            return []
        try:
            cur = self.db.cursor()
            cur.execute(sql, params or ())
            rs = cur.fetchall()
            return rs if rs else []
        except mysql.connector.Error as e:
            print(f"Erro ao consultar dados: {e}")
            return []
        finally:
            cur.close()

    def fechar(self):
        if self.db:
            self.db.close()
            print("Conexão fechada.")
