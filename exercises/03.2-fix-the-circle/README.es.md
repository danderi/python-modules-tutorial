## 🛠️ Soluciona la importación circular

Ahora que hemos visto el error de importación circular, ¡vamos a solucionarlo! Aprenderemos cómo reorganizar nuestro código para evitar la dependencia circular.

## 📝 Instrucciones

1. **Entender el problema de importación circular.** Revisa los archivos `app.py` y `validator.py`. Ambos archivos intentan importar funciones de uno al otro, lo que causa un error de importación circular, necesitamos reorganizar el código para que esto no ocurra.

2. **Identifiquemos qué hace cada archivo.** 
- `app.py`: Contiene las funciones de cálculo, como `add_numbers` y `multiply_numbers`, estas se encargan de recibir los números, validarlos y luego realizar las operaciones.

- `validator.py`: Contiene la función `validate_numbers`, que valida si los números proporcionados son válidos antes de realizar una operación. Sin embargo, este archivo está intentando usar las funciones de cálculo (como `multiply_numbers`), lo que crea un ciclo.

3. **Separar las lógicas en diferentes archivos.** Para evitar la importación circular, vamos a reorganizar el código. 

- Refactoriza las funciones `add_numbers` y `multiply_numbers` para que sean funciones matemáticas puras, sin ninguna validación. Luego muevelas a `utils.py`.

`utils.py` se deberia ver asi:

```python
# utils.py

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b
```

- Ahora, en `validator.py`, vamos a mantener solo la lógica de validación. No necesitamos las funciones de cálculo aquí. Copia este código en `validator.py`:

```python

# validator.py
def validate_numbers(a, b):
    """Check if the numbers are valid"""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return False
    return True
```

4. **Refactoriza el archivo app.py.** Importa las funciones de cálculo (`add_numbers, multiply_numbers`) desde `utils.py` y la función de validación `validate_numbers` desde `validator.py`.

5. Define una función llamada `main` para hacer el código más organizado. Esta función debería ser el punto de entrada del programa y debe realizar lo siguiente:

- Validar los números usando `validate_numbers`.
- Si son válidos, realizar la suma y multiplicación con las funciones `add_numbers`, `multiply_numbers`.
- Si no son válidos, mostrar un mensaje indicando que los números son inválidos. Ejemplo:

```python

a, b = 4, 3
if validate_numbers(a, b):
    print(add_numbers(a, b))  
    print(multiply_numbers(a, b)) 
else:
    print("Invalid numbers")

```


## ✅ Salida esperada

Al ejecutar `app.py`:

```python
7  # Resultado de 4 + 3
12 # Resultado de 4 * 3
```

Si realizaste estas instrucciones con exito, significa que separaste las responsabilidades de las funciones de cálculo y de validación en diferentes módulos. Esto no solo elimina el problema de importación circular, sino que también hace que tu código sea más organizado y fácil de mantener.

