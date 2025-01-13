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

```python
# helper.py (Another module)
def greet(name):
    print(f"Hello, {name}!")
```

## 🌟 Por qué esto importa


- 🎯 Mantiene su código organizado
- 🔄 Deja claro dónde comienza su programa
- 📦 Ayuda a evitar importaciones circulares (¡las aprenderemos más adelante!)
En los próximos ejercicios, practicaremos la importación y el uso de módulos, ¡siempre comenzando desde nuestro punto de entrada app.py! 🚀