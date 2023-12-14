SQL_CRIAR_TABELA = """
 CREATE TABLE IF NOT EXISTS produto (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL,
 descricao TEXT NOT NULL,
 preco DECIMAL(10, 2) NOT NULL
 )
"""
SQL_INSERIR = """
 INSERT INTO produto (nome, descricao, preco)
 VALUES (?, ?, ?)
"""
SQL_ALTERAR = """
 UPDATE produto
 SET nome=?, descricao=?, preco=?
 WHERE id=?
"""
SQL_EXCLUIR = """
 DELETE FROM produto
 WHERE id=?
"""
SQL_OBTER_TODOS = """
 SELECT id, nome, descricao, preco
 FROM produto
 ORDER BY nome
"""
SQL_OBTER_POR_ID = """
 SELECT id, nome
 FROM produto
 WHERE id=?
"""
