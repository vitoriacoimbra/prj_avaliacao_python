from botcity.web import WebBot, Browser,By
from botcity.core import DesktopBot
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CMaestro import T2CMaestro, LogLevel, ErrorType
from prj_T2C_GoogleViagens.classes_t2c.utils.T2CExceptions import BusinessRuleException
from prj_T2C_GoogleViagens.classes_t2c.sqlite.T2CSqliteQueue import T2CSqliteQueue
from prj_T2C_GoogleViagens.classes_t2c.Navegador.GoogleTravel.T2CGoogleTravel import GoogleTravel
import os

class T2CInitAllApplications:
    """
    Classe feita para ser invocada principalmente no começo de um processo, para iniciar os processos necessários para a automação.
    """

    #Iniciando a classe, pedindo um dicionário config e o bot que vai ser usado e enviando uma exceção caso nenhum for informado
    def __init__(self, arg_dictConfig:dict, arg_clssMaestro:T2CMaestro, arg_botWebbot:WebBot=None, arg_botDesktopbot:DesktopBot=None, arg_clssSqliteQueue:T2CSqliteQueue=None):
        """
        Inicializa a classe T2CInitAllApplications.

        Parâmetros:
        - arg_dictConfig (dict): dicionário de configuração.
        - arg_clssMaestro (T2CMaestro): instância de T2CMaestro.
        - arg_botWebbot (WebBot): instância de WebBot (opcional, default=None).
        - arg_botDesktopbot (DesktopBot): instância de DesktopBot (opcional, default=None).
        - arg_clssSqliteQueue (T2CSqliteQueue): instância de T2CSqliteQueue (opcional, default=None).

        Retorna:
        """
        
        if(arg_botWebbot is None and arg_botDesktopbot is None): raise Exception("Não foi possível inicializar a classe, forneça pelo menos um bot")
        else:
            self.var_botWebbot = arg_botWebbot
            self.var_botDesktopbot = arg_botDesktopbot
            self.var_dictConfig = arg_dictConfig
            self.var_clssMaestro = arg_clssMaestro
            self.var_clssSqliteQueue = arg_clssSqliteQueue

    def add_to_queue(self):
        """
        Adiciona itens à fila no início do processo, se necessário.

        Observação:
        - Código placeholder.
        - Se o seu projeto precisa de mais do que um método simples para subir a sua fila, considere fazer um projeto dispatcher.

        Parâmetros:
        """
        # Abrir a homePage dados mundiais
        self.var_botWebbot.browse('https://www.dadosmundiais.com/turismo.php')
        self.var_botWebbot.maximize_window()

        print("Inicio da extração dos países da tabela da página dos Dados Mundiais")
        #For de 30 percorrendo a tabela dos dados mundiais e capturando os paises e lançando na fila 
        for i in range(1,6):
            var_strPais = self.var_botWebbot.find_element(f'//*[@id="main"]/div[3]/div[2]/table/tbody/tr[{str(i+1)}]/td[2]', by=By.XPATH).text 
            
            self.var_clssSqliteQueue.insert_new_queue_item(arg_strReferencia= var_strPais)

        print("Fim da extração dos países da tabela da página dos Dados Mundiais")

        # Fechar navegador
        #self.var_botWebbot.close_page()

    def execute(self, arg_boolFirstRun=False, arg_clssSqliteQueue=None):
        """
        Executa a inicialização dos aplicativos necessários.

        Parâmetros:
        - arg_boolFirstRun (bool): indica se é a primeira execução (default=False).
        - arg_clssSqliteQueue (T2CSqliteQueue): instância da classe T2CSqliteQueue (opcional, default=None).
        
        Observação:
        - Edite o valor da variável `var_intMaxTentativas` no arquivo Config.xlsx.
        
        Retorna:

        Raises:
        - BusinessRuleException: em caso de erro de regra de negócio.
        - Exception: em caso de erro geral.
        """


        #Exclui arquivo de processamento, caso houver

        var_strCaminhoCompleto = r'C:\Robo\prj_T2C_GoogleViagens\prj_T2C_GoogleViagens\resources\planilha_exec\DadosViagem.xlsx'
        #Se arquivo existir
        if os.path.exists(var_strCaminhoCompleto):
           #excluir arquivo
            os.remove(var_strCaminhoCompleto)
        else:
            print("arquivo não existe na pasta")

        #Mata os itens velhos da fila
        self.var_clssSqliteQueue.abandon_queue()
        #Chama o método para subir a fila, apenas se for a primeira vez
        if(arg_boolFirstRun):
            self.add_to_queue()

        #Edite o valor dessa variável a no arquivo Config.xlsx
        var_intMaxTentativas = self.var_dictConfig["MaxRetryNumber"]
        
        for var_intTentativa in range(var_intMaxTentativas):
            try:
                self.var_clssMaestro.write_log("Iniciando aplicativos, tentativa " + (var_intTentativa+1).__str__())
                #Insira aqui seu código para iniciar os aplicativos
                GoogleTravel.open_GoogleTravel(arg_clssMaestro=self.var_clssMaestro, arg_botWebbot=self.var_botWebbot)

            except BusinessRuleException as exception:
                self.var_clssMaestro.write_log(arg_strMensagemLog="Erro de negócio: " + str(exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.BUSINESS_ERROR)

                raise
            except Exception as exception:
                self.var_clssMaestro.write_log(arg_strMensagemLog="Erro, tentativa " + (var_intTentativa+1).__str__() + ": " + str(exception), arg_enumLogLevel=LogLevel.ERROR, arg_enumErrorType=ErrorType.APP_ERROR)

                if(var_intTentativa+1 == var_intMaxTentativas): raise
                else: 
                    #inclua aqui seu código para tentar novamente
                    
                    continue
            else:
                self.var_clssMaestro.write_log("Aplicativos iniciados, continuando processamento...")
                break
            
