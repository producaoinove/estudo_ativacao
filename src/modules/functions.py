import os
import pandas as pd
from datetime import datetime
import logging

def descobrir_separador(caminho_arquivo, linhasparaanalisar=5):
    try:
        with open(caminho_arquivo, 'r') as file:
            for _ in range(linhasparaanalisar):
                line = file.readline().strip()
                separators = [',', ';', '\t']
                separator = next((sep for sep in separators if sep in line), None)
                if separator is None:
                    raise ValueError("Não foi possível determinar o separador do arquivo.")
                return separator
    except:
        return ','

def gerar_dataframes(path_pasta):

    if not os.path.exists(path_pasta) or len(os.listdir(path_pasta)) == 0:
        raise ValueError("Pasta não existe ou está vazia")
    
    # arquivos = [arq for arq in os.listdir(path_pasta) if arq.startswith('rfb_listaCredito_') and arq.endswith('.csv')]
    # arquivos.sort()
    arquivo_velho, arquivo_novo = 'rfb_listaCredito_18.10.2024.csv', 'rfb_listaCredito_14.11.2024.csv'
    # arquivo_velho = arquivo_velho[0]
    # arquivo_novo = arquivo_novo[0]

    path_velho = os.path.join(path_pasta, arquivo_velho)
    separador_velho = descobrir_separador(path_velho)
    path_novo = os.path.join(path_pasta, arquivo_novo)
    separador_novo = descobrir_separador(path_novo)

    df_velho = pd.read_csv(path_velho, sep=separador_velho, dtype=str, low_memory=False)
    cnpjs_velhos = set(df_velho['CNPJ'].to_list())
    df_novo = pd.read_csv(path_novo, sep=separador_novo, dtype=str, low_memory=False)
    cnpjs_novos = set(df_novo['CNPJ'].to_list())

    inativados = cnpjs_velhos - cnpjs_novos
    ativados = cnpjs_novos - cnpjs_velhos

    df_inativados = df_velho[df_velho['CNPJ'].isin(inativados)]
    df_ativados = df_novo[df_novo['CNPJ'].isin(ativados)]
    return df_novo, df_inativados, df_ativados

def gerar_resultado(path_saida, df_original, df_ativados, df_inativados):
    if not os.path.exists(path_saida):
        raise ValueError("Pasta de saída não existe")
    mes_atual = datetime.now().strftime("%B").lower()
    total_cnpjs = len(df_original)
    total_ativados = len(df_ativados)
    total_inativados = len(df_inativados)
    print(f"Total CNPJs em {mes_atual.capitalize()}: {total_cnpjs}")
    print(f"Total CNPJs ativados em {mes_atual.capitalize()}: {total_ativados}")
    print(f"Total CNPJs inativados em {mes_atual.capitalize()}: {total_inativados}")
    df_ativados.to_csv(os.path.join(path_saida, f"novos_cnpjs_{mes_atual}.csv"), index=False)
    df_inativados.to_csv(os.path.join(path_saida, f"desativados_cnpjs_{mes_atual}.csv"), index=False)
