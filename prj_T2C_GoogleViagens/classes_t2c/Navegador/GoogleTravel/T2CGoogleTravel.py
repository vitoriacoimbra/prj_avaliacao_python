from botcity.web import WebBot, Browser,By
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from classes_t2c.Excel.GravarDadosExcel import GravarDadosExcel
from time import sleep
from selenium.webdriver.common.keys import Keys



class GoogleTravel:
    """
    Classe responsável por centralizar todos os passos feitos no site do GoogleTravel.

    Parâmetros:
    
    Retorna:
    """

    @staticmethod
    def open_GoogleTravel(arg_clssMaestro:T2CMaestro, arg_botWebbot:WebBot=None):
        """
        metodo para abrir o site do GoogleTravel na página de explore
        
        Parâmetros:
            - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.
            - arg_botWebbot (WebBot): instância de WebBot (opcional, default=None)
        
        Retorna:
        """
        var_strURL:str = 'https://www.google.com/travel/explore/'
        
        
        arg_clssMaestro.write_log('Abrindo GoogleTravel..')

        arg_botWebbot.browse(var_strURL)
        #arg_botWebbot.maximize_window()

        arg_clssMaestro.write_log('GoogleTravel aberto com sucesso')

    
    @staticmethod
    def close_GoogleTravel(arg_clssMaestro:T2CMaestro, arg_botWebbot:WebBot=None):

        """
        metodo para fechar o site do GoogleTravel
        
        Parâmetros:
            - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.
            - arg_botWebbot (WebBot): instância de WebBot (opcional, default=None)
        
        Retorna:

        """
        
        
        
        arg_clssMaestro.write_log('Fechando GoogleTravel..')

        arg_botWebbot.close_page()

        arg_clssMaestro.write_log('GoogleTravel fechado com sucesso')

    
    @staticmethod
    def search_destination(arg_strCountry:str, arg_clssMaestro:T2CMaestro, arg_botWebbot:WebBot=None):
        """
        metodo para pesquisar destino no site do Google Travel
        
        Parâmetros:
            - arg_strCountry(str): Pais que precisa ser pesquisado
            - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.
            - arg_botWebbot (WebBot): instância de WebBot (opcional, default=None)
        
        Retorna:

        """
        var_strCountry = ''
        if arg_strCountry == 'USA':
            var_strCountry = 'Estados Unidos'
        else:
            var_strCountry = arg_strCountry

        #Filtrando o campo 'De onde:'
        var_eleOnde = arg_botWebbot.find_element('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div[1]/div/div/input', by=By.XPATH)
        var_eleOnde.clear()
        var_eleOnde.send_keys("São Paulo")
        arg_botWebbot.find_element(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/ul/li[1]', by=By.XPATH).click()
        
        sleep(2)
        #Filtrando o campo 'Para onde:'
        var_eleDestino = arg_botWebbot.find_element('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div/input', by=By.XPATH)
        var_eleDestino.clear()
        var_eleDestino.send_keys(var_strCountry)

        for i in range(0, 10):
            var_strResultado = arg_botWebbot.find_element(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/ul/li[{str(i+1)}]/div[2]/div[1]/div', by=By.XPATH).text

            if var_strResultado == var_strCountry:
                arg_botWebbot.find_element(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[3]/ul/li[{str(i+1)}]', by=By.XPATH).click()
                break
        

        sleep(2)
     

        if arg_strCountry == "França":
            #Filtrando o campo de datas
            arg_botWebbot.find_element('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[1]', by=By.XPATH).click()
            arg_botWebbot.find_element(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/div/span/button[1]', by=By.XPATH).click()

            #Inserindo valores no campo de dataInicio
            var_eleDataInicio = arg_botWebbot.find_element(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/span/div/div[1]/div/div[1]/div/input', by=By.XPATH)
            sleep(1)
            var_eleDataInicio.send_keys("20/08/2024")

            #Inserindo valores no campo de dataFim
            var_eleDataFim = arg_botWebbot.find_element(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/span/div/div[1]/div/div[2]/div/input', by=By.XPATH)
            var_eleDataFim.send_keys("23/08/2024")
            var_eleDataFim.send_keys(Keys.ENTER)
            sleep(2)

            #clicando no botão confirmar
            arg_botWebbot.find_element(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/div[1]/section/div/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[3]/div[1]/button/span', by=By.XPATH).click()
            

    @staticmethod
    def get_destinations(arg_strCountry:str, arg_botWebbot:WebBot=None):
        """
        metodo para extrair destinos dentro do pais pesquisado e retornando uma tabela com esses destinos 
        
        Parâmetros:
            - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.
            - arg_botWebbot (WebBot): instância de WebBot (opcional, default=None)
        
        Retorna:

        """

        sleep(5)
        for i in range(0, 40):
            var_strDestino = arg_botWebbot.find_element(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{str(i+1)}]/div/div[2]/div[1]/h3', by=By.XPATH).text
            var_strPreco = arg_botWebbot.find_element(f'/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div/div/div[1]/main/div/div[2]/div/ol/li[{str(i+1)}]/div/div[2]/div[2]/div[1]/div[1]/span', by=By.XPATH).text

            GravarDadosExcel.GravarDados(arg_strPais=arg_strCountry, arg_strDestino=var_strDestino, arg_strPreco=var_strPreco)







        
        
