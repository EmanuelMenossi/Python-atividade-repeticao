cont = 0
N = 0
S = 0
M = 0
F = 0

while cont <= 3:
    sexo = (input('Você é homem? digite {M} ou Você é mulher? digite {F} : '))
    idade = int(input("Qual é sua idade?: "))
    resp = (
        input("Você gostou do nosso produto? Sim = {S} | Nao = {N} | Indiferente = I: "))

    if resp == 'S':
        S = S + 1
    if resp == 'N':
        N = N + 1

    if sexo == 'M' and resp == 'N':
        M = M + 1

    if sexo == 'F' and resp == 'S':
        F = F + 1

    cont = cont + 1
(print('Foram entrevistadas', (cont)))
(print(N, 'Disseram que NÃO'))
(print(S, 'Disseram que SIM'))
(print(F, 'Mulheres que disseram que sim'))
(print(M, 'Homens que disseram que não'))
