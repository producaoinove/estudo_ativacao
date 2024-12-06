import datetime as dtm
from .paths import (
    path_out, path_data, path_log, path_temp, path_tests
)

pastas_necessarias = list()
pastas_necessarias.append(path_data)
pastas_necessarias.append(path_out)
pastas_necessarias.append(path_tests)
pastas_necessarias.append(path_temp)
pastas_necessarias.append(path_log)

pacotes_necessarios : list = [
    'pandas',
    'datetime',
    'os'
]

nome_log = "estudo_ativacao"


