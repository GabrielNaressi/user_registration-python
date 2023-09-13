
import time

class Usuario:
    def __init__(self, nome, idade, cpf, rg, hora):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg 
        self.hora = hora

    def mostrardados (self):
        print("Usuário cadastrado:")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("CPF:", self.cpf)
        print("RG:", self.rg)
        print("Hora do cadastro:", self.hora)

def validar_cpf():
        while True:
            cpf = input("CPF (apenas números): ")
            if len(cpf) == 11 and cpf.isdigit():
                return cpf
            else:
                print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")

def validar_rg():
        while True:
            rg = input("RG (apenas números): ")
            if len(rg) == 8 and rg.isdigit():
                return rg
            else:
                print("rg inválido. O rg deve conter 8 dígitos numéricos.")

def validar_idade():
        while True:
            idade = int(input("idade (apenas números): "))
            if idade >= 18:
                return idade
            else:
                print("idade inválida. O idade deve ser maior que 18.")

def cadastrarusuario():
    usuario = {}  

    usuario["nome"] = input("Digite o nome do usuário: ")
    usuario["idade"] = validar_idade()
    usuario["cpf"] = validar_cpf()
    usuario["rg"] = validar_rg ()
    horacadastro = time.strftime("%Y-%m-%d %H:%M:%S")

    usuario["horacadastro"] = horacadastro

    return usuario

def main():
    usuarios = []
    usuario = cadastrarusuario() 

    novousuario = Usuario (usuario["nome"], usuario["idade"], usuario["cpf"], usuario["rg"], usuario["horacadastro"])

    usuarios.append(novousuario)
    novousuario.mostrardados()

if __name__ == "__main__":
    main()