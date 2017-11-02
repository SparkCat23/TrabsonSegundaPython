from datetime import date

class Pessoa():
    def __init__(self,nome,email,celular):
    	self.nome = nome
    	self.email = email
    	self.celular = celular
    def __str__(self):
        return str(self.nome)
    def altera_celular(self,cel):
        self.celular = cel
    def altera_email(self,email):
        self.email = email
    def altera_nome(self,nome):
        self.nome = nome
    def retorna_celular(self,cel):
        return self.celular
    def retorna_email(self,email):
        return self.email
    def retorna_nome(self,nome):
        return self.nome

class Usuario():
    def __init__(self,ra,senha):
    	self.ra = ra
    	self.senha = senha

    def altera_ra(self,ra):
    	self.ra = ra
        
    def altera_senha(self,senha):
    	self.senha = senha
        
    def retorna_ra(self,ra):
    	return self.ra

    def retorna_senha(self,senha):
    	return self.senha

class Aluno(Pessoa,Usuario):
    def __init__(self,nome,email,celular,ra,senha,sigla_curso):
        Pessoa.__init__(self, nome, email, celular)
        Usuario.__init__(self, ra,senha)
        self.sigla_curso = sigla_curso
        self.matriculas = []

    def disciplinas_aluno(self):
        disciplinas=[]
        for m in self.matriculas:
            disciplinas.append(m.disciplina.nome)
        return disciplinas
	
    def matricular(self,Matricula):
        # carregando nomes das Disciplinas
        disciplinas = []
        for d in self.matriculas:
            disciplinas.append(d.disciplina.nome)
        # validação
        if Matricula.disciplina.nome not in disciplinas:
            self.matriculas.append(Matricula)
            return True
        else:
            print("-- Matrícula já cadastrada --")
            return False
		
    def confirmar_matricula(self,ConfDisciplina):
        # carregando nomes das disciplinas
        disciplinasAluno = []
        for d in self.matriculas:
            disciplinasAluno.append(d.disciplina.nome)
        # se a disciplina estiver na lista do aluno
        if ConfDisciplina.disciplina.nome in disciplinasAluno:
            for c in range(0,len(disciplinasAluno)):
                if ConfDisciplina.disciplina.nome == disciplinasAluno[c]:
                    # alteração da data de confirmação
                    ConfDisciplina.data_confirmacao = date.today()
                    print("-- Matrícula Confirmada --")
                    return True
        else:
            print("-- Matricula Não Existe --")
            return False
		
    def cancelar_matricula(self,disciplina):
	    pass
	
class Professor(Pessoa,Usuario):
	def __init__(self,apelido):
		self.apelido = apelido
		
	def adiciona_disciplina(self,disciplina):
		Disciplina.__init__(nome,carga_horaria,teoria,pratica,ementa,competencias,habilidades,conteudo,bibliografia_basica,bibliografia_complementar)
		
	def remove_disciplina(self,disciplina):
		pass
	
	def disciplinas_professor(self):
		return #lista de disciplinas do professor
		
	def carga_horaria_total(self):
		return #Int com carga horária do professor
		
class Matricula():
    def __init__(self,Aluno,Disciplina,data_matricula):
        y = int(data_matricula[0:4])
        m = int(data_matricula[5:7])
        d = int(data_matricula[9:11])
        self.aluno = Aluno
        self.disciplina = Disciplina
        self.data_matricula = date(y,m,d)
        self.data_confirmacao = None
        self.data_cancelamento = None
    def __str__(self):
        mat = str(self.aluno)+"--"+str(self.disciplina)+".\nData de Matrícula: "+str(self.data_matricula)
        return mat

    def altera_aluno(self,aluno):
	    self.aluno = aluno
	
    def altera_disciplina(self,disciplina):
	    self.disciplina = disciplina
    def retorna_aluno(self):
        return #nome do aluno
    def retorna_disciplina(self):
        return #nome da disciplina matriculada
		
class Disciplina():
    def __init__(self,nome,carga_horaria,teoria,pratica,ementa,competencias,habilidades,conteudo,bibliografia_basica,bibliografia_complementar):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.teoria = teoria
        self.pratica = pratica
        self.ementa = ementa
        self.competencias = competencias
        self.habilidades = habilidades
        self.conteudo = conteudo
        self.bibliografia_basica = bibliografia_basica
        self.bibliografia_complementar = bibliografia_complementar
    
    def __str__(self):
        return str(self.nome)

    def altera_nome(self,nome):
        self.nome = nome
    def	altera_carga_horaria(self,carga_horaria):
        self.carga_horaria = carga_horaria
	
    def	altera_teoria(self,teoria):
        self.teoria = teoria
	
    def	altera_pratica(self,pratica):	
        self.pratica = pratica

    def	altera_ementa(self,ementa):
        self.ementa = ementa

    def	altera_competencias(self,competencias):
        self.competencias = competencias
	
    def	altera_pratica(self,habilidades):
        self.habilidades = habilidades
	
    def	altera_conteudo(self,conteudo):
        self.conteudo = conteudo

    def	altera_bibliografia_basica(self,bibliografia_basica):
        self.bibliografia_basica = bibliografia_basica
	
    def	altera_bibliografia_complementar(self,bibliografia_complementar):
        self.bibliografia_complementar = bibliografia_complementar

    def retorna_nome(self):
        return self.nome

    def	retorna_carga_horaria(self):
        return self.carga_horaria

    def	retorna_teoria(self):
        return self.teoria
	
    def	retorna_pratica(self):	
        return self.pratica

    def	retorna_ementa(self):
        return self.ementa

    def	retorna_competencias(self):
        return self.competencias
	
    def	retorna_pratica(self):
        return self.habilidades
	
    def	retorna_conteudo(self):
        return self.conteudo

    def	retorna_bibliografia_basica(self):
        return self.bibliografia_basica
	
    def	retorna_bibliografia_complementar(self):
        return self.bibliografia_complementar
