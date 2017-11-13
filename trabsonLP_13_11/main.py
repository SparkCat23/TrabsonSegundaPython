import trabson

'''
-- Métodos da  Classe Pessoa --
a1.altera_celular(string)
a1.altera_email(string)
a1.altera_nome(string)
a1.retorna_celular()
a1.retorna_email()
a1.retorna_nome()
-- Métodos da  Classe Usuario --
a1.altera_ra(string)
a1.altera_senha(string)
a1.retorna_ra()
a1.retorna_senha()
^Estes são herdados pelas Classes Aluno e Professor^
Objetos Aluno : Exemplo
a1 = trabson.Aluno("Fulano", "abc@123.com", "99999-9999", "123456", "aluno1", "ADS")
-- funções --
a1.matricular(Object)
a1.confirmar_matricula(Object)
a1.cancelar_matricula(Object)
Objetos Professor : Exemplo
p1 = trabson.Professor("Utonium","prof1@123.com","11111-1111","111111","prof1","Professor")
-- funções --
p1.adiciona_disciplina(Object)
p1.remove_disciplina(Object)
p1.carga_horaria_total()
p1.disciplinas_professor()
Objetos Disciplina : Exemplo
d1 = trabson.Disciplina("Linguagem de Programação 1",80,30,50,"Ementa de LP","Competencia de LP",
                        "Programação","Python","Livro Básico","Livro Complementar")
-- funções --
d1.altera_<atributo>(string/int) -- altera o atributo
d1.retorna_<atributo>(string/int) -- retorna o atributo
^Métodos válidos para todos os atributos de Disciplinas^
Objetos Matricula : Exemplo
m1 = trabson.Matricula(a1,d1,"2017-11-01")
-- funções --
m1.altera_aluno(Object)
m1.altera_disciplina(Object)
m1.retorna_aluno()
m1.retorna_disciplina()
'''

#Criação das Disciplinas
d1 = trabson.Disciplina('Linguagem de Programação', 80, 80, 0, 'Programação em python', 
                        'programação', 'programação', 'python', 'Uns livro ae', 'Otros livro ae')
d2 = trabson.Disciplina('Linguagem de Programação II', 60, 30, 30, 'Programação em python', 
                        'programação', 'programação', 'python', 'Uns livro ae', 'Otros livro ae')
d3 = trabson.Disciplina('Linguagem de Programação III', 90, 20, 70, 'Programação em python', 
                        'programação', 'programação', 'python', 'Uns livro ae', 'Otros livro ae')
d4 = trabson.Disciplina('Linguagem de Programação IV', 120, 0, 120, 'Programação em python', 
                        'programação', 'programação', 'python', 'Uns livro ae', 'Otros livro ae')
d5 = trabson.Disciplina('Linguagem de Programação V', 50, 10, 40, 'Programação em python', 
                        'programação', 'programação', 'python', 'Uns livro ae', 'Otros livro ae')


#Criação dos Alunos
a1 = trabson.Aluno('Reginaldo', 'renaldo@123.com', '99999-9999', '000001', 'aluno01', 'ADS')
a2 = trabson.Aluno('Fulano', 'fulano@123.com', '98888-9999', '000002', 'aluno02', 'ADS')
a3 = trabson.Aluno('Ciclano', 'ciclano@123.com', '97777-9999', '000003', 'aluno03', 'ADS')
a4 = trabson.Aluno('Larissa', 'Larissa@123.com', '96666-9999', '000004', 'aluno04', 'ADS')
a5 = trabson.Aluno('Bianca', 'Bianca@123.com', '95555-9999', '000005', 'aluno05', 'ADS')


#Criação dos Professores
p1 = trabson.Professor('Fernando', 'prof.f@123.com', '94444-9999', '999999', 'prof01', 'Prof_F')
p2 = trabson.Professor('Diana', 'prof.d@123.com', '93333-9999', '999998', 'prof02', 'Prof_d')


#Matricula Alunos Disciplinas
m1 = trabson.Matricula(a1, d1, '2017-11-01')
m2 = trabson.Matricula(a1, d2, '2017-11-01')
m3 = trabson.Matricula(a1, d3, '2017-11-01')
m4 = trabson.Matricula(a1, d4, '2017-11-01')
m5 = trabson.Matricula(a1, d5, '2017-11-01')

a1.matricular(m1)
a1.matricular(m2)
a1.matricular(m3)
a1.matricular(m4)
a1.matricular(m5)

m6 = trabson.Matricula(a2, d1, '2017-11-01')
m7 = trabson.Matricula(a2, d2, '2017-11-01')
m8 = trabson.Matricula(a2, d3, '2017-11-01')
m9 = trabson.Matricula(a2, d4, '2017-11-01')
m10 = trabson.Matricula(a2, d5, '2017-11-01')

a1.matricular(m6)
a1.matricular(m7)
a1.matricular(m8)
a1.matricular(m9)
a1.matricular(m10)

m11 = trabson.Matricula(a3, d1, '2017-11-01')
m12 = trabson.Matricula(a3, d2, '2017-11-01')
m13 = trabson.Matricula(a3, d3, '2017-11-01')
m14 = trabson.Matricula(a3, d4, '2017-11-01')
m15 = trabson.Matricula(a3, d5, '2017-11-01')

a1.matricular(m11)
a1.matricular(m12)
a1.matricular(m13)
a1.matricular(m14)
a1.matricular(m15)

m16 = trabson.Matricula(a4, d1, '2017-11-01')
m17 = trabson.Matricula(a4, d2, '2017-11-01')
m18 = trabson.Matricula(a4, d3, '2017-11-01')
m19 = trabson.Matricula(a4, d4, '2017-11-01')
m20 = trabson.Matricula(a4, d5, '2017-11-01')

a1.matricular(m16)
a1.matricular(m17)
a1.matricular(m18)
a1.matricular(m19)
a1.matricular(m20)

m21 = trabson.Matricula(a5, d1, '2017-11-01')
m22 = trabson.Matricula(a5, d2, '2017-11-01')
m23 = trabson.Matricula(a5, d3, '2017-11-01')
m24 = trabson.Matricula(a5, d4, '2017-11-01')
m25 = trabson.Matricula(a5, d5, '2017-11-01')

a1.matricular(m21)
a1.matricular(m22)
a1.matricular(m23)
a1.matricular(m24)
a1.matricular(m25)


#Adicionar disciplina ao professor
p1.adiciona_disciplina(d1)
p1.adiciona_disciplina(d2)

p2.adiciona_disciplina(d3)
p2.adiciona_disciplina(d4)
p2.adiciona_disciplina(d5)


#Mostrar Disciplinas Aluno
md1 = a1.disciplinas_aluno()
print(md1)
md2 = a2.disciplinas_aluno()
print(md2)
md3 = a3.disciplinas_aluno()
print(md3)
md4 = a4.disciplinas_aluno()
print(md4)
md5 = a5.disciplinas_aluno()
print(md5)


#Mostrar Disciplinas Prof
mdl1 = p1.disciplinas_professor()
print(mdl1)
mdl2 = p2.disciplinas_professor()
print(mdl2)


#Mostra carga Prof
mch1 = p1.carga_horaria_total()
print(mch1)
mch2 = p2.carga_horaria_total()
print(mch1)


#Confirma disc pro
a1.confirmar_matricula(d1)
a1.confirmar_matricula(d2)
a1.confirmar_matricula(d3)
a1.confirmar_matricula(d4)
a1.confirmar_matricula(d5)

a2.confirmar_matricula(d1)
a2.confirmar_matricula(d2)
a2.confirmar_matricula(d3)
a2.confirmar_matricula(d4)
a2.confirmar_matricula(d5)

a4.confirmar_matricula(d1)
a4.confirmar_matricula(d2)
a4.confirmar_matricula(d3)
a4.confirmar_matricula(d4)
a4.confirmar_matricula(d5)

a5.confirmar_matricula(d1)
a5.confirmar_matricula(d2)
a5.confirmar_matricula(d3)
a5.confirmar_matricula(d4)
a5.confirmar_matricula(d5)

a3.confirmar_matricula(d1)
a3.confirmar_matricula(d2)
a3.confirmar_matricula(d3)
a3.confirmar_matricula(d4)
a3.confirmar_matricula(d5)
