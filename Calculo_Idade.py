nascimento= 2006
nome= 'Breno'
anoAtual= 2023
nascimentoJovem= 2010

def calculoIdade (nascimento, anoAtual):
 idade= anoAtual-nascimento
 return idade
idade=calculoIdade (nascimento, anoAtual)
idadeJovem=calculoIdade(nascimentoJovem, anoAtual)
print ('idade é'+ str(idade))
print ('idadeJovem'+ str(idadeJovem))
