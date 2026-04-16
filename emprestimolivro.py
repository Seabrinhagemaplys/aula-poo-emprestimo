from bancodedados import bancoDeDados
from emprestimo import Emprestimo

class emprestimoLivro(Emprestimo):
    def __init__(self, nomeUsuario: str, titulo: str):
        super().__init__(nomeUsuario, titulo)
    
    def registrar(self, bancoDados: bancoDeDados):
        bancoDados.registrarLivro(self)
        bancoDados.prazoDevolucao(7)