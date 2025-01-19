from io import StringIO
import sys
from unittest.mock import patch
import pytest
import importlib


@pytest.mark.it("Should import the PI, GRAVITY, and AUTHOR constants")
def test_import_constants():
    from app import PI, GRAVITY, AUTHOR
        
    # Verificar que las constantes estén definidas
    assert isinstance(PI, (int, float)), "PI is not a valid number"
    assert isinstance(GRAVITY, (int, float)), "GRAVITY is not a valid number"
    assert isinstance(AUTHOR, str), "AUTHOR is not a valid string"
    

@pytest.mark.it("Should verify that the functions calculate_circle_area and calculate_fall_time are declared")
def test_functions_declared():
    from app import calculate_circle_area, calculate_fall_time
        
    # Verificar que ambas funciones sean callables (es decir, que estén definidas como funciones)
    assert callable(calculate_circle_area), "The function calculate_circle_area is not declared in app.py"
    assert callable(calculate_fall_time), "The function calculate_fall_time is not declared in app.py"
   
   

@pytest.mark.it("Should use calculate_circle_area and calculate_fall_time in app.py")
def test_app_uses_functions():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        # Importar el módulo app
        import app

        # Llamar manualmente las funciones para asegurarse de que se usen
        app.calculate_circle_area(5)
        app.calculate_fall_time(100)

        # Recargar el módulo para ejecutar el código en el bloque principal
        importlib.reload(app)  # Esto hace que se ejecute el código principal nuevamente

        # Capturar la salida de la consola
        output = mock_stdout.getvalue()

        # Verificar que las funciones hayan sido utilizadas
        assert "Area of a circle with radius 5:" in output, "The function calculate_circle_area was not used in app.py"
        assert "Time to fall from 100 meters:" in output, "The function calculate_fall_time was not used in app.py"
    #     # Importar y recargar el módulo app
    #     import app
    #     import app
    #     app.calculate_circle_area(5)
    #     app.calculate_fall_time(100)
    #     importlib.reload(app)  # Asegura que el bloque principal del código se ejecute

       