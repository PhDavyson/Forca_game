#random de palavras
from random import choice
import string

with open('bco_palavras.txt') as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split('\n')

#variáveis
palavra = choice(lista_de_palavras).upper()
qtd_caracteres = len(palavra)
mensagem = ''
acertos = 0
erros = 0
letras_acertadas = ''
letras_erradas = ''
chances = 6
# alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'y', 'x', 'z']


def listAlphabet():
  return list(string.ascii_lowercase)
# print(listAlphabet())
