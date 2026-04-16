from emprestimolivro import emprestimoLivro

class emprestimoRevista(emprestimoLivro):
    def __init__(self, nomeUsuario: str, titulo: str, edicao: str):
        super.__init__(nomeUsuario, titulo)
        self.checarEdicao(edicao)
        self.adicionarEdicao(edicao)

    def checarEdicao(self, edicao: str):
        if not isinstance(edicao, str):
            raise TypeError("Edição Não é string!")
        
    def adicionarEdicao(self, edicao: str):
        self.edicao = edicao

    def registrar(self, bancoDados):
        bancoDados.registrarRevista(self)
        bancoDados.prazoDevolucao(2)