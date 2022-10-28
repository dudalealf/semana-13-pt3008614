class Turma:
  def __init__(self):
    self.turma = [];
    self.menorNota = None;
    self.maiorNota = None;

  def cadastrarAlunos(self, alunos):    
    for i in alunos:
      if(i.nota < 0 or i.nota > 10):
        return print("Nota inválida para o aluno {}, atualize o cadastro e tente novamente".format(i.nome))
      self.turma.append(i);
      if((self.menorNota == None) or (self.menorNota.nota > i.nota)):
        self.menorNota = i;
      if((self.maiorNota == None) or (self.maiorNota.nota < i.nota)):
        self.maiorNota = i;                 

  def mostrarAlunos(self):  
    print('Quantidade de alunos:', len(self.turma));
    for x in self.turma:      
      print(x.mostrarAluno());