SQL_CRIAR_TABELA = """
 CREATE TABLE IF NOT EXISTS produto (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 nome TEXT NOT NULL
 )
"""
SQL_INSERIR = """
 INSERT INTO produto (nome)
 VALUES (?)
"""
SQL_ALTERAR = """
 UPDATE produto
 SET nome=?
 WHERE id=?
"""
SQL_EXCLUIR = """
 DELETE FROM produto
 WHERE id=?
"""
SQL_OBTER_TODOS = """
 SELECT id, nome
 FROM produto
 ORDER BY nome
"""
SQL_OBTER_POR_ID = """
 SELECT id, nome
 FROM produto
 WHERE id=?
"""
