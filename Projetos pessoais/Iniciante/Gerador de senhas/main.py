# Importa o módulo 'string', que contém constantes úteis como letras, dígitos e pontuações
import string
# Importa o módulo 'random', usado para gerar elementos aleatórios
import random

# Define uma função chamada 'gerar_senha' que recebe o tamanho desejado como argumento
def gerar_senha(tamanho):
    # Verifica se o tamanho informado é menor que 5
    if tamanho < 5:
        # Exibe uma mensagem avisando que a senha deve ter pelo menos 5 caracteres
        print("A senha deverá conter no mínimo 5 caracteres!")
    else:
        # Garante que a senha tenha pelo menos 1 letra, 1 número e 1 caractere especial
        senha = [
            random.choice(string.ascii_letters),   # Escolhe uma letra aleatória (maiúscula ou minúscula)
            random.choice(string.digits),          # Escolhe um número aleatório
            random.choice(string.punctuation)      # Escolhe um símbolo especial aleatório (ex: @, #, !)
        ]

        # Junta todas as possibilidades de caracteres: letras, números e símbolos
        possibilidades = ''.join([
            string.ascii_letters,   # abc...XYZ
            string.digits,          # 0123456789
            string.punctuation      # !@#$%...
        ])

        # Adiciona à senha os caracteres restantes para atingir o tamanho desejado
        senha.extend(random.choices(possibilidades, k=tamanho-3))

        # Embaralha todos os caracteres da senha para garantir aleatoriedade
        random.shuffle(senha)

        # Junta todos os caracteres da lista em uma única string e retorna a senha final
        return ''.join(senha)

# Pede ao usuário que digite o tamanho da senha desejada e converte para inteiro
tamanho = int(input("Digite o tamanho da senha: "))

# Chama a função gerar_senha com o tamanho informado e imprime o resultado
print(gerar_senha(tamanho))
