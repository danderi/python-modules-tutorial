## 🔍 Detecta la importación circular

¡Oh no! Tenemos dos archivos Python que intentan usar las funciones del otro. ¡Veamos qué sucede cuando intentamos ejecutarlos!

## 📝 Instrucciones

1. Observa estos dos archivos:
    - `app.py`: Tiene funciones matemáticas e importa `validar_numeros` de `validator.py`
    - `validator.py`: Tiene funciones de validación e importa `multiplicar_numeros` de `app.py`

2. Intenta comprender por qué causan una importación circular:

   ```python
   # app.py importa de validator.py
   from validator import validar_numeros

   # validator.py importa de app.py
   from app import multiplicar_numeros
   ```

3. Ejecuta el código y observa el error que obtienes
4. Toma notas sobre lo que te indica el mensaje de error

## 💡 Pista

Cuando veas este error:
```
ImportError: cannot import name '...' from partially initialized module '...' (most likely due to a circular import)
```
Significa que tus módulos están tratando de importarse entre sí. ¡Piensa en ello como dos amigos que intentan llamarse por teléfono al mismo tiempo exacto! 📞

## ✅ Salida esperada

Al ejecutar `app.py`, deberías ver un mensaje de error sobre importaciones circulares. ¡No te preocupes, esto es exactamente lo que queremos! En el siguiente ejercicio, aprenderemos cómo solucionar esto. 🛠️

## 🤔 ¿Por qué sucede esto?

1. Cuando Python comienza con `app.py`, ve que necesita `validar_numeros` de `validator.py`.
2. Entonces va a `validator.py`, pero luego ve que necesita `multiplicar_numeros` de `app.py`.
3. ¡Pero `app.py` aún no ha terminado de cargarse!
4. Python se confunde y genera un error.

En el próximo ejercicio, aprenderemos cómo solucionar esto reorganizando nuestro código. 🚀