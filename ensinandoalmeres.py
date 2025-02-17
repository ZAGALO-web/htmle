# Como escrver alguma coisa em baixo:

print("OLá, Mundo!")

# Como perguntar algo:

# input("Quantos anos vc tem?")

# Como fazer uma condição:

# palmeiras = mundial = True

#  if palmeiras == mundial == False:
#     print("Palmeiras não tem mundial!")
# elif palmeiras == mundial == True or False:
#     print("Alguns acham que sim outros não.")
# elif palmeiras == mundial == True:
#     print("Palmeiras tem mundial!")
# else:
#     pass

# Sabe o elif! ele aidciona mais uma condição
# Sabe o else! ele faz uma condição negativa
# Sabe o True e o False! São binários: True = Sim False = Não
# Sabe o pass! ele deixa o algoritimo quieto

# Como importar uma biblioteca:

# import pygame

# Como baixar:

# pip install pygame

# Como mostrar o valor dessa coisa:

# print(type(1))

# Como fazer uma classe:

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#     def descrever_carro(self):
#         return f"{self.ano} {self.marca} {self.modelo}"

#     def acelerar(self):
#         return f"O {self.modelo} está acelerando."

#     def frear(self):
#         return f"O {self.modelo} está freando."

# meu_carro = Carro("Toyota", "Corolla", 2020)
# print(meu_carro.descrever_carro())
# print(meu_carro.acelerar())
# print(meu_carro.frear())

# Como fazer uma continuação:

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.velocidade = 0

#     def descrever_carro(self):
#         return f"{self.ano} {self.marca} {self.modelo}"

#     def acelerar(self, incremento):
#         self.velocidade += incremento
#         return f"O {self.modelo} está acelerando. Velocidade atual: {self.velocidade} km/h"

#     def frear(self, decremento):
#         self.velocidade = max(0, self.velocidade - decremento)
#         return f"O {self.modelo} está freando. Velocidade atual: {self.velocidade} km/h"

#     def velocidade_atual(self):
#         return f"Velocidade atual do {self.modelo}: {self.velocidade} km/h"

# # Exemplo de uso da classe
# meu_carro = Carro("Toyota", "Corolla", 2020)
# print(meu_carro.descrever_carro())
# print(meu_carro.acelerar(30))
# print(meu_carro.velocidade_atual())
# print(meu_carro.frear(10))
# print(meu_carro.velocidade_atual())

# Como fazer um loop e fazer uma coisa para não ser falsa:

# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.velocidade = 0

#     def descrever_carro(self):
#         return f"{self.ano} {self.marca} {self.modelo}"

#     def acelerar(self, incremento):
#         self.velocidade += incremento
#         return f"O {self.modelo} está acelerando. Velocidade atual: {self.velocidade} km/h"

#     def frear(self, decremento):
#         self.velocidade = max(0, self.velocidade - decremento)
#         return f"O {self.modelo} está freando. Velocidade atual: {self.velocidade} km/h"

#     def velocidade_atual(self):
#         return f"Velocidade atual do {self.modelo}: {self.velocidade} km/h"

#     def simular_movimento(self):
#         while self.velocidade > 0:
#             print(self.frear(5))
#             print(self.velocidade_atual())

# # Exemplo de uso da classe
# meu_carro = Carro("Toyota", "Corolla", 2020)
# print(meu_carro.descrever_carro())
# print(meu_carro.acelerar(30))
# print(meu_carro.velocidade_atual())
# meu_carro.simular_movimento()

# E você percebeu que usamos classes, condições, perguntas, importamos bibliotecas e muito mais! 





