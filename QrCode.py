# -*- coding: UTF-8 -*-
import qrcode

print ("Qual o nome do produto?")
nome_produto = input () 
nome = (nome_produto)

print ("Qual o material do produto?")
material = input()

if material == "vidro":
    print("Qual o endereço")
    endereco = input()

    imagem = qrcode.make("Material: {}".format(material + " / "+ "Endereco: " + endereco + " / Atencao: Produto Fragil"))
else:
    print("Qual o endereço")
    endereco = input()
    imagem = qrcode.make("Material: {}".format(material + " / Endereco: " + endereco))

imagem.save("Qrcode_{}.jpg".format(nome))