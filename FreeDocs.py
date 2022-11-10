#By MrBluess, just use and enjoy! 😎
#De MrBluess, solo usalo y disfrutalo! 😎

# Librerías
import pyautogui, sys
import random
import os

# Generar Nombres aleatorios 🖋
minus = "abcdfghijklmnñopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"

base = minus+mayus+numeros

longitud = 8

muestra=random.sample(base, longitud)
NombreAleatorio = "".join(muestra)

# Codigo 1 <--- First step --->
pyautogui.PAUSE = 1.2 # Tiempo que de mora entre cada tarea.
pyautogui.click(787, 313) # Seleccionar idioma español.
pyautogui.click(83, 486) # Seleccionar pagina aleatoria.
pyautogui.hotkey('ctrl', 'a') # Seleccionar todo el texto.
pyautogui.hotkey('ctrl', 'c') # Copiar todo el texto.
with pyautogui.hold('alt'): # Cambiar de ventana. (test)
    pyautogui.press('tab')
    pyautogui.press('tab') # Se puede cambiar, pero por ahora no 💔
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v') # Pegar el texto seleccionado.
pyautogui.hotkey('ctrl', 'shift','s') # Guardar el archivo. 📁
pyautogui.write(NombreAleatorio)# Generar un nombre aleatorio
pyautogui.press('enter') # Guardar el archivo x2. 📁
pyautogui.hotkey('ctrl', 'e') # Seleccionar todo el texto ***TXT***
pyautogui.press('backspace') # Borrar el texto pegado.

for x in [0,1,2,3,4,5,6,7,8,9]: # Cantidad de veces que se va a ejecutar el script 😎

    # Generar Nombres aleatorios 🖋
    minus = "abcdfghijklmnñopqrstuvwxyz"
    mayus = minus.upper()
    numeros = "0123456789"

    # Formula a utilizar
    base = minus+mayus+numeros

    # Tamaño del codigo (Aquí seleccionamos cuantos caracteres vamos a utilizar)
    longitud = 8

    # Se genera el nombre random
    muestra=random.sample(base, longitud)
    NombreAleatorio = "".join(muestra)

    pyautogui.click(83, 486) # Seleccionar pagina aleatoria.
    pyautogui.hotkey('ctrl', 'a') # Seleccionar todo el texto.
    pyautogui.hotkey('ctrl', 'c') # Copiar todo el texto.
    with pyautogui.hold('alt'): # Cambiar de ventana. (test)
        pyautogui.press('tab') # Se puede cambiar, pero por ahora no 💔
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'v') # Pegar el texto seleccionado.
    pyautogui.hotkey('ctrl', 'shift','s') # Guardar el archivo. 📁
    pyautogui.write(NombreAleatorio)# Generar un nombre aleatorio
    pyautogui.press('enter') # Guardar el archivo x2. 📁
    pyautogui.hotkey('ctrl', 'e') # Seleccionar todo el texto ***TXT***
    pyautogui.press('backspace') # Borrar el texto pegado.

# Despedida
pyautogui.alert('Terminamos, gracias por usar FreeDocs \n - MrBluess')
```
