from bancodedados import bancoDeDados
from abc import ABC, abstractmethod

class Emprestimo(ABC):
    def __init__(self, nomeUsuario: str, titulo: str):
        self.checarNomeUsuarioeTitulo(nomeUsuario, titulo)
        self.adicionarNomeUsuario(nomeUsuario, titulo)

    def checarNomeUsuarioeTitulo(self, nomeUsuario: str, titulo: str):
        if not isinstance(nomeUsuario, str):
            raise TypeError("Edição Não é string!")
        
        if not isinstance(titulo, str):
            raise TypeError("Título Não é string!")
        
    def adicionarNomeUsuario(self, nomeUsuario: str, titulo: str):
        self.nomeUsuario = nomeUsuario
        self.titulo = titulo

    def registrar(self, bancoDados: bancoDeDados):
        bancoDados.registrar(self)
        
    
    @abstractmethod
    def registrar(self):
        pass