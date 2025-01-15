# 🌟 Variables y constantes del módulo

Los módulos también pueden tener variables y constantes. Vamos a aprender cómo crearlas, usarlas y compartirlas entre archivos.

## 📝 Instrucciones

1. Crea un archivo llamado `constants.py` y define estas constantes:

```python
PI = 3.14159
GRAVITY = 9.81
AUTHOR = "Your name"
```

2. En tu archivo principal, `app.py` crea las siguientes dos funciones:
- `calculate_circle_area(radius)`. Esta función debe usar la constante **PI** para calcular y devolver el área de un círculo con el radio proporcionado.
- `calculate_fall_time(height)`. Esta función debe usar la constante **GRAVITY** para calcular y devolver el tiempo que tarda un objeto en caer desde una altura dada usando la fórmula de la física: (2 * height / GRAVITY) ** 0.5
- Importa las constantes **PI, GRAVITY, AUTHOR** desde `constants.py`.

3. Usa la función `calculate_circle_area` para calcular el área de un círculo con un radio de 5 y muestra el resultado.
4. Usa la función `calculate_fall_time` para calcular el tiempo de caída de un objeto desde una altura de 100 metros y muestra el resultado.
5. Por último, imprime un mensaje con la constante **AUTHOR** para indicar quién creó estas funciones.

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
