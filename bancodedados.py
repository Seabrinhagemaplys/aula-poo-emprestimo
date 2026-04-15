from emprestimo import Emprestimo

class bancoDeDados:
    def __init__(self):
        self.listaDeEmprestimos: list[Emprestimo] = []
    
    def registrar(self, emprestimoRecebido: Emprestimo):
        if not self.checarExistenciadeUsuario(emprestimoRecebido):
            self.adicionarEmprestimonaLista(emprestimoRecebido)

    def checarExistenciadeUsuario(self, emprestimoRecebido: Emprestimo) -> bool:
        for u in self.listaDeEmprestimos:
            if u.nomeUsuario == emprestimoRecebido.nomeUsuario:
                return True
    
    def adicionarEmprestimonaLista(self,emprestimoRecebido: Emprestimo):
        self.listaDeEmprestimos.append(emprestimoRecebido)