# 🔄 Entendiendo las importaciones circulares

Hablemos de algo complicado que puede suceder cuando se trabaja con módulos de Python: ¡las importaciones circulares!

## 🤔 ¿Qué es una importación circular?

Imagina a dos amigos que intentan llamarse por teléfono al mismo tiempo exacto. ¡Ambos están ocupados llamando, por lo que ninguno puede contestar! Eso es algo así como lo que sucede con las importaciones circulares: dos (o más) módulos que intentan importarse entre sí al mismo tiempo.

Ejemplo:
```python
# archivo1.py
from archivo2 import funcion2  # Importa de archivo2

# archivo2.py
from archivo1 import funcion1  # Importa de archivo1
```

## 🚫 ¿Por qué es un problema? 

1. Tu código se queda atascado en un bucle 
2. Python se confunde acerca de qué módulo cargar primero 
3. Tu programa podría bloquearse o no funcionar correctamente 

## ✨ ¿Cómo solucionarlo? 

Hay varias formas de solucionar las importaciones circulares: 
1. Reorganiza tu código 
2. Mueve el código compartido a un nuevo módulo 
3. Usa instrucciones import dentro de las funciones 
4. Importa módulos donde se necesiten 

¡Practiquemos cómo encontrar y corregir importaciones circulares en los próximos ejercicios! 🚀 