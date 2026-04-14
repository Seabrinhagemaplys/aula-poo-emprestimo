from emprestimo import Emprestimo

class bancoDeDados:
    def __init__(self):
        self.listaDeEmprestimos: list[Emprestimo] = []
    
    def registrar(self, emprestimoRecebido: Emprestimo):
        if not self.checarExistenciadeUsuario(emprestimoRecebido: Emprestimo):
            self.adicionarEmprestimonaLista(emprestimoRecebido: Emprestimo)
            

    def checarExistenciadeUsuario(self, emprestimoRecebido: Emprestimo):
        for u in 
    
    def adicionarEmprestimonaLista(self,emprestimoRecebido: Emprestimo):
        pass