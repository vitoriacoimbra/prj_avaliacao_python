import pandas as pd
import os

class GravarDadosExcel:
    """
    Classe responsável por escrever na planilha os dados capturados no GoogleTravel

    Parâmetros:
    
    Retorna:
    """    

    @staticmethod
    def GravarDados(arg_strPais:str, arg_strDestino:str, arg_strPreco:str):
        """
        metodo para escrever os dados retirados do GoogleTravel em uma planilha
        
        Parâmetros:
            - arg_strDestino(str): Nome do destino capturado
            - arg_strPreco(str): Preço da passagem capturada
        
        Retorna:

        """


        var_strCaminhoBase = r'C:\Robo\prj_T2C_GoogleViagens\prj_T2C_GoogleViagens\resources\planilha_exec'
        var_strNomePlanilha = 'DadosViagem.xlsx'
        var_strCaminhoCompleto = os.path.join(var_strCaminhoBase, var_strNomePlanilha)

        var_dataDadosDestino = {
            'Pais': [arg_strPais],
            'Cidade': [arg_strDestino],
            'Preço': [arg_strPreco]
       }

        var_dfDadosDestino = pd.DataFrame(var_dataDadosDestino)

        

        #Se arquivo existir
        if os.path.exists(var_strCaminhoCompleto):
            #ler arquivo existente
            var_dfExcel = pd.read_excel(var_strCaminhoCompleto) 
            #Juntar dados da planilha com novos
            var_dfDadosDestino = pd.concat([var_dfDadosDestino, var_dfExcel], ignore_index=True)
           
        
        var_dfDadosDestino.to_excel(var_strCaminhoCompleto, sheet_name='Todos', index=False)
    

    @staticmethod
    def OrdenarDados():
        var_strCaminhoBase = r'C:\Robo\prj_T2C_GoogleViagens\prj_T2C_GoogleViagens\resources\planilha_exec'
        var_strNomePlanilha = 'DadosViagem.xlsx'
        var_strCaminhoCompleto = os.path.join(var_strCaminhoBase, var_strNomePlanilha)

        var_dfExcel = pd.read_excel(var_strCaminhoCompleto) 

        var_dfExcel = var_dfExcel.sort_values(by='Preço', ascending= True)

        var_dtDestinosBaratos = var_dfExcel.head(10)

        # Escrever o DataFrame na nova aba
        with pd.ExcelWriter(var_strCaminhoCompleto, engine='openpyxl', mode='a') as writer:
            var_dtDestinosBaratos.to_excel(writer, sheet_name='Baratos', index=False)






