frase = Curso em video Python
O ultimo valor sempre é ignorado pelo python
len(frase) = qual o comprimento da frase? = 21 caratecteres
frase.count('o') = quantas vezes aparece a letra 'o' minuscula = 3
frase.count('0', 0, 13) = contagem com fatiamento, do zero até o 12 = 1 letra 'o'
frase.find('deo') = irá mostrar em que posição se encontra os ou o caractere(letras)
'Curso' in frase = > in < existe 'curso' em frase? = sim existe
frase.replace('Python','Android') = irá substituir 'Python' pelo 'Android'
frase.upper() = substitui as letras minusculas em maiusculas
frase.lower() = substitui as letras maiusculas em minusculas
frase.capitalize() = transforma toda a string(frase) em minuscula e a 1º letra deixa em maiuscula
frase.title() = vai analisar quantas palavras tem a string e transforma todas as 1º letra de cada palavra em maiuscula
frase.strip() = removerá todos os espaços antes e depois da frase
frase.rstrip() = removerá somente os ultimos espaços depois da frase
frase.lstrip() = removerá os espaços antes da frase
frase.split() = irá eliminar os espaços entre cada palavra da frase
[Curso][em][Video][Python]
[01234][01][01234][012345]
[  0  ][1 ][  2  ][  3   ]
' '.join(frase)
frase.len()