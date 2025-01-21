# 🔄 Usando tu módulo personalizado

Ahora que hemos creado nuestro módulo de saludos, ¡usemoslo en nuestro app.py!

## 📝 Instrucciones

1. Asegúrate de tener el archivo `greetings.py` creado. Este archivo debe contener las dos funciones:

- `say_hello(name)` que devuelve "Hello, {name}!".
- `say_goodbye(name)` que devuelve "Goodbye, {name}!".

2. Importa las funciones `say_hello` y `say_goodbye` desde tu archivo `greetings.py`. Ejemplo

```python
#app.py
from greetings import say_hello, say_goodbye
```
3. Crea una lista de nombres: 

```python
names = ["Alice", "Bob", "Charlie"]
```
4. Usa un bucle para recorrer la lista de nombres para saludar y despedirte de cada persona.
5. Imprime los resultados de cada saludo y despedida.


## ✅ Salida esperada

Tu programa debería imprimir algo como:
```python
Hello, Alice!
Goodbye, Alice!
Hello, Bob!
Goodbye, Bob!
Hello, Charlie!
Goodbye, Charlie!
```