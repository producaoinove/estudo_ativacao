try:
    from settings import ( 
        pastas_necessarias, pacotes_necessarios, verificar_pacotes, verificar_pastas
    )

    verificar_pastas(pastas_necessarias)
    verificar_pacotes(pacotes_necessarios)
    print("Pastas e pacotes verificados e criados, se necessario!")

except Exception as e:
    print(f"Impossivel verificar pacotes e pastas... {str(e)}")
import logging
from settings import (
    setup_log, nome_log, path_log, path_data, path_out
)
from modules import (
    gerar_dataframes, gerar_resultado
)
logging.getLogger(setup_log(nome_log, path_log))

if __name__ == "__main__":
    logging.info("Aplicacao >> inicio")

    df_atual, df_inativado, df_ativado = gerar_dataframes(path_data)

    gerar_resultado(path_out, df_atual, df_ativado, df_inativado)

    logging.info("Aplicacao >> final")
