linhas = int(input())
colunas = int(input())
if (linhas % 2 == 0 and colunas % 2 == 0) or (linhas % 2 != 1 and colunas % 2 != 0):
    print(1)
elif not (linhas % 2 == 0 and colunas % 2 == 0) or not (linhas % 2 != 1 and colunas % 2 != 0):
    print(0)