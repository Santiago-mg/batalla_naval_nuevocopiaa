
class filas_equivocadas ( Exception ):
    pass

class columnas_equivocadas ( Exception ):
    pass

class Except_salto_disparo (Exception):
    """Aun no puedes pasar el turno,  no has elegido la posicion en la que dispararas"""

class Except_Disparo_out_of_Range (Exception):
    def __init__(self, mensaje="Disparo fuera de rango."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class Except_disparo_Repetido (Exception):
    pass

#Verificar el rango para cualquier cosa y si no es el correcto saltar una excepcion
def rango_correcto (filas, columnas ):
    if filas !=10:
        raise filas_equivocadas ("ERROR: El numero de filas no es correcto, numero de filas dieferente de 10")
    
    if columnas !=10:
        raise columnas_equivocadas ("ERROR: El numero de columnas no es correcto, numero de columnas dieferente de 10")
    
    