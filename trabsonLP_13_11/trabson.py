from datetime import date

class Pessoa():
    def __init__(self,nome,email,celular):
    	self.nome = nome
    	self.email = email
    	self.celular = celular
    def __str__(self):
        return str(self.nome)
    def altera_celular(self,cel):
        if type(cel) == str:
            self.celular = cel
            return True
        else:
            return False
    def altera_email(self,email):
        if type(email) == str:
            self.email = email
            return True
        else:
            return False
    def altera_nome(self,nome):
        if type(nome) == str:
            self.nome = nome
            return True
        else:
            return False
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
        if type(ra) == str:
            self.ra = ra
            return True
        else:
            return False
        
    def altera_senha(self,senha):
        if type(senha) == str:
            self.senha = senha
            return True
        else:
            return False
        
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
		
    def cancelar_matricula(self,CancelDisciplina):
	    # carregando nomes das disciplinas
        disciplinasAluno = []
        for d in self.matriculas:
            disciplinasAluno.append(d.disciplina.nome)
        # se a disciplina estiver na lista do aluno
        if CancelDisciplina.disciplina.nome in disciplinasAluno:
            for c in range(0,len(disciplinasAluno)):
                if CancelDisciplina.disciplina.nome == disciplinasAluno[c]:
                    # alteração da data de confirmação
                    CancelDisciplina.data_cancelamento = date.today()
                    print("-- Matrícula Cancelada --")
                    return True
        else:
            print("-- Matricula Não Existe --")
            return False
	
class Professor(Pessoa,Usuario):
    def __init__(self,nome,email,celular,ra,senha,apelido):
        Pessoa.__init__(self,nome,email,celular)
        Usuario.__init__(self,ra,senha)
        self.apelido = apelido
        self.disciplinasProf = []
	
    def adiciona_disciplina(self,addDisciplina):
        # carregando nomes das disciplinas
        discProf = []
        for d in self.disciplinasProf:
            discProf.append(d.nome)
        # se a disciplina não estiver cadastrada ainda
        if addDisciplina.nome not in discProf:
            self.disciplinasProf.append(addDisciplina)
            return True
        else:
            print("-- Disciplina já cadastrada --")
            return False
	
    def remove_disciplina(self,delDisciplina):
        # carregando nomes das disciplinas
        discProf = []
        for d in self.disciplinasProf:
            discProf.append(d.disciplina.nome)
        # se a disciplina estive cadastrada para o professor
        if delDisciplina.disciplina.nome in discProf:
            for x in range(0,len(discProf)):
                if delDisciplina.disciplina.nome == discProf[x]:
                    # alteração da data de confirmação
                    discProf.remove(x)
                    print("-- Disciplina Removida --")
                    return True
        else:
            print("-- Disciplina não Ecziste --")
            return False

    def disciplinas_professor(self):
        disciplinas=[]
        for d in self.disciplinasProf:
            disciplinas.append(d.nome)
        return disciplinas
	
    def carga_horaria_total(self):
        total = 0
        for d in self.disciplinasProf:
            total += d.carga_horaria
        return total
		
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
        if type(aluno) == Aluno:
            self.aluno = aluno
            return True
        else:
            return False
	
    def altera_disciplina(self,disciplina):
        if type(disciplina) == Disciplina:
            self.disciplina = disciplina
            return True
        else:
            return False
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
        if type(nome) == str:
            self.nome = nome
            return True
        else:
            return False

    def	altera_carga_horaria(self,carga_horaria):
        if type(carga_horaria) == int:
            if carga_horaria <= 0:
                print("-- Inserção Inválida! A carga horária não pode ser menor ou igual a ZERO --")
                return False
            else: 
                self.carga_horaria = carga_horaria
                print("-- Carga Horária Alterada --")
                return True
        else:
            return False
	
    def	altera_teoria(self,teoria):
        if type(teoria) == int:
            if teoria <= 0:
                print("-- Inserção Inválida! A carga horária não pode ser menor ou igual a ZERO --")
                return False
            else: 
                self.teoria = teoria
                print("-- Carga Horária Alterada --")
                return True
        else:
            return False
	
    def	altera_pratica(self,pratica):
        if type(pratica) == int:	
            if pratica <= 0:
                print("-- Inserção Inválida! A carga horária não pode ser menor ou igual a ZERO --")
                return False
            else: 
                self.pratica = pratica
                print("-- Carga Horária Alterada --")
                return True
        else:
            return False
        
    def	altera_ementa(self,ementa):
        if type(ementa) == str:
            self.ementa = ementa
            return True
        else:
            return False

    def	altera_competencias(self,competencias):
        if type(competencias) == str:
            self.competencias = competencias
            return True
        else:
            return False
	
    def	altera_habilidades(self,habilidades):
        if type(habilidades) == str:
            self.habilidades
            return True
        else:
            return False
	
    def	altera_conteudo(self,conteudo):
        if type(conteudo) == str:
            self.conteudo = conteudo
            return True
        else:
            return False

    def	altera_bibliografia_basica(self,bibliografia_basica):
        if type(bibliografia_basica) == str:
            self.bibliografia_basica = bibliografia_basica
            return True
        else:
            return False
	
    def	altera_bibliografia_complementar(self,bibliografia_complementar):
        if type(bibliografia_complementar) == str:
            self.bibliografia_complementar = bibliografia_complementar
            return True
        else:
            return False

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
