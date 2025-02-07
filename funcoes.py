# a estrutura def serve para criar uma funcao
def saudacao():
    print("Ola, vamos iniciaro curso de Python")

saudacao()

# Ó código acima serve para executar uma funcao

def bemvindo(nome):
    print(f"Ola, seja bem vindo ao curso de Python, {nome}")

bemvindo("Charles")

# Ó código acima serve para executar uma funcao

# Agora vamos ter uma pequena aula de boas práticas de código

# 1. Funções devem ter nomes significativos
# 2. Funções devem ser pequenas e concebidas para fazer uma coisa
# 3. Funções devem ser reutilizaveis
# precisamos organizar a execução de cada função na sua ordem de aplicação

def main():
    saudacao()
    bemvindo("Charles")
    

if __name__ == "__main__":
    main()


# DICA: Para executar uma funcao, basta chama-la, quando tivermos mais de uma função, devemos colocar em ordens para serem executadas.
""" e depois com essa estrutura para saber se as funções estão sendo executadas em outros scripts 
if __name__ == "__main__":
    main() """