import trabson

# Objectos Aluno
a1 = trabson.Aluno("Fulano", "abc@123.com", "99999-9999", "123456", "aluno1", "ADS")
a2 = trabson.Aluno("Siclano","def@123.com","88888-8888","654321","aluno2","BD")

# Objetos Disciplina
d1 = trabson.Disciplina("Linguagem de Programação 1",80,30,50,"Ementa de LP","Competencia de LP",
                        "Programação","Python","Livro Básico","Livro Complementar")
d2 = trabson.Disciplina("Matemática Aplicada",80,40,40,"Ementa de MatAp","Competencia de MatAp",
                        "Lógica","Matemática","Livro Básico","Livro Complementar")

# Objetos Matricula
m1 = trabson.Matricula(a1,d1,"2017-11-01")
m2 = trabson.Matricula(a1,d2,"2017-11-01")
m3 = trabson.Matricula(a2,d1,"2017-11-01")
m4 = trabson.Matricula(a2,d2,"2017-11-01")
m5 = trabson.Matricula(a1,d1,"2017-11-01")

a1.matricular(m1)
a1.matricular(m2)
#print(a1.disciplinas_aluno())

#a1.matricular(m5)
#print(a1.disciplinas_aluno())

a1.confirmar_matricula(m1)
for m in a1.matriculas:
    print(m.data_confirmacao)