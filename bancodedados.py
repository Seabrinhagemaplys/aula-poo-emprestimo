from emprestimo import Emprestimo
from emprestimolivro import emprestimoLivro
from emprestimorevista import emprestimoRevista

class bancoDeDados:
    def __init__(self):
        self.listaDeEmprestimos: list[Emprestimo] = []
    
    def registrarLivro(self, emprestimoRecebido: Emprestimo):
            if not self.checarExistenciadeUsuario(emprestimoRecebido) and not self.checarExistenciadeLivro(emprestimoRecebido):
                self.adicionarEmprestimonaLista(emprestimoRecebido)
            else:
                print("Livro já registrado!")
    
    def registrarRevista(self, emprestimoRecebido: Emprestimo):
            if not self.checarExistenciadeUsuario(emprestimoRecebido) and not self.checarExistenciadeEdicao(emprestimoRecebido):
                self.adicionarEmprestimonaLista(emprestimoRecebido)
            else:
                print("Revista já registrada!")

    def checarExistenciadeUsuario(self, emprestimoRecebido: Emprestimo) -> bool:
        for u in self.listaDeEmprestimos:
            if u.nomeUsuario == emprestimoRecebido.nomeUsuario:
                return True
            
    def checarExistenciadeLivro(self, emprestimoRecebido: Emprestimo):
        for u in self.listaDeEmprestimos:
            if u.titulo == emprestimoRecebido.titulo:
                return True
            
    def checarExistenciadeEdicao(self, emprestimoRecebido: emprestimoRevista):
        for u in self.listaDeEmprestimos:
            if u.titulo == emprestimoRecebido.edicao:
                return True
    
    def adicionarEmprestimonaLista(self,emprestimoRecebido: Emprestimo):
        self.listaDeEmprestimos.append(emprestimoRecebido)

    def prazoDevolucao(self, qtdDiasParaDevolucao: int):
        self.prazoDevolucao = qtdDiasParaDevolucao