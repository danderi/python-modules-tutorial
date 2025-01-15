## 🛠️ Soluciona la importación circular

Ahora que hemos visto el error de importación circular, ¡vamos a solucionarlo! Aprenderemos cómo reorganizar nuestro código para evitar la dependencia circular.

## 📝 Instrucciones

1. Revisa el archivo llamado `utils.py` lo usaremos para el código compartido
2. Mueve la lógica de validación a `utils.py`
3. Actualiza `app.py` y `validator.py` para usar el código compartido
4. ¡Prueba que todo funciona ahora!

## 💡 Pista

A veces, la mejor manera de solucionar una importación circular es crear un nuevo módulo del que ambos archivos puedan importar. ¡Piensa en qué código se podría compartir!

## ✅ Salida esperada

Al ejecutar `app.py`:

```python
7  # Resultado de 4 + 3
12 # Resultado de 4 * 3
```
