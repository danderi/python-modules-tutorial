# 🌟 Variables y constantes del módulo

Los módulos también pueden tener variables y constantes. Vamos a aprender cómo crearlas, usarlas y compartirlas entre archivos.

## 📝 Instrucciones

1. Crea un archivo llamado `constants.py` al mismo nivel que el archivo `app.py` y define estas constantes:

```python
PI = 3.14159
GRAVITY = 9.81
AUTHOR = "Your name"
```

2. En tu archivo principal, `app.py` importa las constantes **PI, GRAVITY, AUTHOR** desde `constants.py`. 

3. Crea las siguientes dos funciones en el archivo  `app.py`:

- `calculate_circle_area(radius)`. Esta función debe usar la constante **PI** para calcular y retornar el área de un círculo con el radio proporcionado. La fórmula es: `PI * radius ** 2`. Ejemplo:

```python

def calculate_circle_area(radius):
    return PI * radius ** 2  # Use the constant PI
```

- `calculate_fall_time(height)`. Esta función debe usar la constante **GRAVITY** para calcular y retornar el tiempo que tarda un objeto en caer desde una altura dada usando la fórmula de la física: `(2 * height / GRAVITY) ** 0.5`. Similar como lo hicimos en el paso anterior.

4. Llama a la función `calculate_circle_area` con un radio de **5**. Guarda el resultado e imprime un mensaje como:

```python

area = calculate_circle_area(radius)

print(f"Area of a circle with radius 5: {area}.")
```


5. Tal y como hicimos en el paso anterior. Llama a la función `calculate_fall_time` con una altura de **100** metros. Guarda el resultado  e imprime un mensaje como:

```python
"Time to fall from 100 meters: 4.52 seconds."
```

6. Por último, imprime un mensaje con la constante **AUTHOR** para indicar quién creó estas funciones. Ejemplo:

```python
print(f"These calculations were made by: {AUTHOR}")
```

## ✅ Salida esperada

Tu programa debería imprimir algo como:

```python
Area of a circle with radius 5: 78.54
Time to fall from 100 meters: 4.52 seconds
These calculations were made by: Your Name
```


## 💡 Tips

Las constantes generalmente se escriben en letras MAYÚSCULAS. Ejemplo:
```python
PI = 3.14159
GRAVITY = 9.81
```
