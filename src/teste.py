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
    setup_log, nome_log, path_log
)
logging.getLogger(setup_log(nome_log, path_log))

if __name__ == "__main__":
    logging.info("Teste >> inicio")

    logging.info("Teste >> final")
