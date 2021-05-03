## Importamos el package sys que nos permite acceder de modo global
import sys
sys.path.append("pytests/utils/functions")

# Una vez conociendo todos los packages locales tomamos el que necesitamos
from helloworld import say_hello


say_hello() # podemos llamar así xq del modulo solo se importó una funcion y no todas
