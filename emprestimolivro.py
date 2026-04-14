from emprestimo import Emprestimo

class emprestimoLivro(Emprestimo):
    def __init__(self, nomeUsuario: str, titulo: str):
        super().__init__()
        self.verificarUsuarioeTitulo()
        self.nomeUsuario = nomeUsuario
        self.titulo = titulo
    
    def