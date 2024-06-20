#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Uso:

Variael LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Italo Rafael"
__license__ = "Unlicense"

import os

current_languade = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_languade == "pt_BR":
    msg = "Olá Mundo!"
elif current_languade == "it_IT":
    msg = "Ciao, Mondo!"
elif current_languade == "es_SP":
    msg = "Hola, Mondo!"

print(msg)
