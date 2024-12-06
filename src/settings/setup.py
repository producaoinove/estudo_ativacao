import logging
import os
import subprocess
import sys

def instalar_pacotes_externos(pacote: str) -> None:
    """
Instala o pacote especificado usando pip.

Entrada:
    pacote (str): o nome do pacote a ser instalado

Saída:
    nenhuma (none)
    """
    try:
        os.system("python.exe -m pip install --upgrade pip")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o pacote {pacote}: {e}")
        raise

def verificar_pacotes(pacotes: list) -> None:
    """
Verifica se os pacotes estão instalados, caso contrário, instala-os.

Entrada:
    pacotes (list): uma lista de strings com os nomes dos pacotes a serem verificados

Saída:
    nenhuma (none)
    """
    for pacote in pacotes:
        try:
            __import__(pacote)
        except ImportError:
            print(f"Pacote {pacote} não encontrado. Instalando...")
            instalar_pacotes_externos(pacote)

def setup_log(nome_base: str, path_log: str) -> None:
    """
Realiza a configuração do log da aplicação

Entrada:
    nome_base (str): o nome do arquivo de log
    path_log (str): a pasta que vai salvar 

Saída:
    nenhuma (none)
    """

    logging.basicConfig(
        filename=os.path.join(path_log, f'{nome_base}.log'),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def verificar_pastas(pastas: list) -> str:
    """
Verifica as pastas necessárias ao projeto e cria se necessário.

Entrada:
    pastas (list): uma lista com caminhos (absolutos) das pastas necessárias ao projeto

Saída:
    uma string avisando que verificou e criou se necessário
    """
    for pasta in pastas:
        if not os.path.exists(pasta):
            os.makedirs(pasta)
    
    return "Pastas verificadas e criadas, se necessário."
