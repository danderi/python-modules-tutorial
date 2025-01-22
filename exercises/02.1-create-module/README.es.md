# 🎨 Crea tu primer módulo

¡Creemos un módulo de saludo simple! Haremos un módulo que tenga funciones para saludar de diferentes maneras.

## 📝 Instrucciones

1. Crea un archivo llamado `greetings.py`. Este archivo debe estar en la misma carpeta que el archivo `app.py` de este ejercicio.

2. En el archivo llamado `greetings.py` declara una función llamada `say_hello(name)`. Esta función tomará un nombre como entrada y devolverá un saludo personalizado con ese nombre. Ejemplo:

```python
def say_hello(name):
    return f"Hello, {name}!"

```
3. En el mismo archivo `greetings.py` define otra función llamada `say_goodbye(name)` que devuelva el siguiente mensaje: 

```python
return f"Goodbye, {name}!"
```

Similar a como lo hicimos en el paso anterior.

4. Ahora, en el archivo `app.py`, vamos a importar las funciones que acabamos de crear en `greetings.py` y las vamos a usar.,  haciendo un `print()` de lo que retorna cada una. Ejemplo:

```python
print(say_hello("Alice"))
```


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