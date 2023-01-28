import sqlite3
#criar banco
conn = sqlite3.connect('/aula-1/clientes.db')
cursor = conn.cursor()

def criar_tabela():
    #criar tabela, caso não exista
    cursor.execute(""" 
    CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(11) NOT NULL
    );
    """
)
#criar_tabela()

def add_cliente():
    #adicionar informações ao banco
    cursor.execute(
        """
        INSERT INTO clientes(nome,idade,cpf)
        VALUES('Bianca',21,12345675433);
        """
    )
    conn.commit()
#add_cliente()    

def ler_dados():
    #lê informações do banco
    cursor.execute(
        """
        SELECT * FROM clientes 
        """
    )
    for cliente in cursor.fetchall():
        print(cliente)
#ler_dados()

def atualizar():
    #atualizar dados do banco
    id = 1
    novo_nome = 'Jonny'
    nova_idade = 45
    novo_cpf = 987654321
    cursor.execute(
        """
        UPDATE clientes
        SET nome = ?, idade = ?, cpf = ? WHERE id = ?
        """, (novo_nome, nova_idade, novo_cpf, id)
    )
    conn.commit()
#atualizar()

def remover():
    #deletar informações do banco
    cursor.execute(
        """
        DELETE FROM clientes WHERE nome = 'Jonny' 
        """
    )
    conn.commit()
remover()
