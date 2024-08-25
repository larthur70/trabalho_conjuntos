arquivo_1 = "arquivo_teste.txt"
arquivo_2 = "arquivo_teste2.txt"
arquivo_3 = "arquivo_teste3.txt"
#COLOQUE NESTA STRING O NOME DO ARQUIVO DE TESTE DO PROFESSOR
arquivo_professor = ''

opcao = int(input("Digite o número do arquivo de testes (1 a 3), 4 se for o do professor: "))
if opcao == 1:
    nome_arquivo = arquivo_1
elif opcao == 2:
    nome_arquivo = arquivo_2
elif opcao == 3:
    nome_arquivo = arquivo_3
else:
    nome_arquivo = arquivo_professor
    
def uniao(conj1,conj2):
    print(conj1 | conj2)

def intersecao(conj1,conj2):
    print(conj1 & conj2)

def diferenca(conj1,conj2):
    dif = set()
    for e in conj1:
        if e not in conj2:
            dif.add(e)
    print(dif)

def produto_cartesiano(conj1,conj2):
    produto = []
    for e in conj1:
        for e2 in conj2:
            par_ordenado = (e,e2)
            produto.append(par_ordenado)
    produto = set(produto)
    print(produto)

def tratar_string(string):
    conj = [e.strip(' ') for e in string.split(',')]
    conj = set(conj)
    return conj

with open(nome_arquivo,'r',encoding='utf8') as arquivo:
    linhas = [l.strip("\n") for l in arquivo]
    numOp = int(linhas[0])
    i1 = 2
    i2 = 3
    op = 1
    for n in range(numOp):
        conj1 = tratar_string(linhas[i1])
        conj2 = tratar_string(linhas[i2])
        if linhas[op] == 'U':
            print("União:")
            uniao(conj1,conj2)
        elif linhas[op] == 'I':
            print("Intersecção:")
            intersecao(conj1,conj2)
        elif linhas[op] == 'D':
            print("Diferença:")
            diferenca(conj1,conj2)
        else:
            print("Produto Cartesiano:")
            produto_cartesiano(conj1,conj2)
        i1 += 3
        i2 += 3
        op += 3
        
        

        
        
