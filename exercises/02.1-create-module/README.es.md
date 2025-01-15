# 🎨 Crea tu primer módulo

¡Creemos un módulo de saludo simple! Haremos un módulo que tenga funciones para saludar de diferentes maneras.

## 📝 Instrucciones

1. Crea un archivo llamado `greetings.py`

2. En el archivo llamado `greetings.py` escribe una función llamada `say_hello(name)` que devuelva:

```python
"Hello, [name]!"
```
3. En el mismo archivo `greetings.py` define otra función llamada `say_goodbye(name)` que devuelva: 

```python
"Goodbye, [name]!"
```
4. Importa y usa estas funciones en el archivo `app.py`,  haciendo un print() de lo que retorna cada una.


## ✅ Salida esperada

Tu programa debería imprimir algo como:
```python
Hello, Alice!
Goodbye, Alice!
```

## 💡 Pista

La importación en tu archivo `app.py` debería verse algo así:

```python
# app.py

from greetings import say_hello 
```