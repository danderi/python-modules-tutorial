# 🎬 Entendiendo los puntos de entrada en Python

¡Hola! 👋 Antes de sumergirnos en la importación de módulos, comprendamos algo súper importante: ¡los puntos de entrada!

## 🤔 ¿Qué es un punto de entrada?

Piense en su programa Python como un libro 📚. Así como cada libro necesita una primera página, cada programa de Python necesita un archivo principal donde todo comienza. A esto lo llamamos el "punto de entrada" de su programa.

En nuestros ejercicios, usaremos `app.py` como nuestro punto de entrada. Este es el archivo que:

1. 🎯 Inicia su programa
2. 📥 Importa otros módulos
3. 🎮 Controla el flujo principal de su programa

## 💡 Ejemplo
Aquí hay un ejemplo sencillo:
```python
# app.py (Tu punto de entrada)
from helper import greet  # Importar desde otro módulo

def main():
    name = "Alice"
    greet(name)

if __name__ == "__main__":
    main()
```

helper.py (Otro modulo)

```python
def greet(name):
    print(f"Hello, {name}!")
```

## Instrucciones

En este ejercicio vamos a trabajar con dos archivos ya creados. ¡Empecemos! 🚀

1. Fijate en el archivo llamado `helper.py` el cual contiene una función auxiliar llamada `greet(name)` que simplemente se encarga de saludar al usuario. Es una "herramienta" que utilizaremos en el programa principal.

2. Fijate en el archivo llamado `app.py:` que será el archivo principal que sirve como punto de entrada al programa e importa la función `greet` de helper.py y organiza la lógica principal en la función `main()`.

**Nota:** El bloque `if __name__ == "__main__"` asegura que el programa comience desde aquí.

3. En el archivo principal `app.py` completa la función `main()` en app.py para que pida el nombre del usuario y guardalo en una variable `name`. 

4. Para saludar al usuario: Llama a la función `greet(name)` pasando la variable `name` que obtuviste en el paso anterior.

5. Comprueba en la función `main()` lo siguiente:

- Si el nombre es "Teacher", mostrar un mensaje especial. Ejemplo: 

```python
"Welcome, teacher ready to guide your students?"
```

- Si el nombre tiene menos de 3 caracteres, dar una advertencia. Ejemplo: 

```python
"Your name is quite short! Are you sure that's correct?"
```

- Si es distinto a "teacher" y tiene más de 3 caracteres darle la Bienvenidad. Ejemplo:

```python
 "Nice to meet you! Let's start learning Python!"
```

6. Una vez que hayas completado la lógica en la función `main()`, ejecuta el programa.

Finalmente, ¿por qué ha sido importante la organización que hemos elegido para nuestro código?


- 🎯 Porque mantiene el código organizado
- 🔄 Deja claro dónde comienza su programa
- 📦 Ayuda a evitar importaciones circulares (¡las aprenderemos más adelante!)

En los próximos ejercicios, practicaremos la importación y el uso de módulos, ¡siempre comenzando desde nuestro punto de entrada app.py! 