from cmath import nan
import pandas as pd

class DadosCredito():

    dados = nan

    def __init__(self):
        pass

    def carregaArquivo(caminho):
        if (type(caminho) != str):
            raise NameError('A variável caminho não foi informada corretamente')
        else:
            dados = pd.read_csv(caminho) 
            return dados
