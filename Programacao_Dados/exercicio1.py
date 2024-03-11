class read_csv:
    """
    Essa classe tem como função a leitura de um arquivo csv, retornando os dados do aruivo no formato
    de lista, e retornando uma variável contendo o cabeçalho do arquivo caso for 
    necessário para salvar uma amostra 
    """
    def __init__(self, filename):
        self.filename = filename

    def read(self, encoding='utf-8'):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.readlines()
                header = content[0].strip().split(',')  # Remover quebra de linha e dividir pelo caractere de vírgula
                content = [line.strip().split(',') for line in content[1:]]  # Remover quebra de linha e dividir pelo caractere de vírgula
            return content, header
        except UnicodeDecodeError:
            print('Ocorreu um erro devido ao encoding do arquivo, forneça o encoding correto na chamada do método read. \n Exemplo reader.read(encoding="latin-1")')
            return None, None
        except FileNotFoundError:
            print(f"Arquivo '{self.filename}' não encontrado.")
            return None, None
        except Exception as erro:
            print(f"Erro ao ler o arquivo '{self.filename}'\n com o seguinte erro: {erro}")
            return None, None

import random
import csv

class amostra:
    def __init__(self, data, num_valores, cabecalho):
        self.data = data
        self.num_valores = num_valores
        self.cabecalho = cabecalho

    def gera_amostra(self):
        amostra_aleatoria = random.sample(self.data, self.num_valores)
        amostra_com_cabecalho = [self.cabecalho] + amostra_aleatoria  

        return amostra_com_cabecalho

    def salva_amostra(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(self.cabecalho)  # Escreve o cabeçalho
            writer.writerows(self.data)  # Escreve os dados




# Exemplo de uso:
filename = r"C:\Users\bruno\OneDrive\Documentos\Programação para Dados\steam_games.csv"
reader = read_csv(filename)
corpo, cabecalho = reader.read()

nova_amostra = amostra(corpo, 20, cabecalho)
corpo_amostra = nova_amostra.gera_amostra()


nova_amostra.salva_amostra("amostra2.csv")
