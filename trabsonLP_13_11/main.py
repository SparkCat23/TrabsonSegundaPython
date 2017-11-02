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