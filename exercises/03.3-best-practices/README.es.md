## 🌟 Mejores prácticas para la organización de módulos

¡Aprendamos a organizar nuestro código para prevenir importaciones circulares antes de que sucedan!

## 📝 Instrucciones

1. Observa la estructura actual de archivos del ejercicio:
   ```
   03.3-best-practices/
   ├── app.py      # Archivo de entrada
   ├── models.py      # Estructuras de datos
   ├── utils.py       # Utilidades compartidas
   ├── students.py    # Operaciones de estudiantes
   └── courses.py     # Operaciones de cursos
   ```

2. Completa el código en cada archivo siguiendo estas reglas:
   - Mantén el código compartido en `utils.py`.
   - Define las estructuras de datos en `models.py`.
   - Usa esas estructuras en otros módulos.

## 💡 Pista

Al organizar módulos, piensa en las dependencias:
- ¿Qué código necesita ser compartido?
- ¿Qué módulos deberían importar de cuáles?
- ¿Dónde debería residir cada pieza de funcionalidad?

## ✅ Salida esperada

Al ejecutar `students.py`:

```python
Estudiante: Alice (ID: 1) inscrito en Curso: Python 101 (Código: PY101)
