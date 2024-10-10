"""
Created on Wednesday 09/10/24

@author: Victor Mendoza
"""
# Se crea la clase Pila
class Pila:
    def __init__(self): # Se crean los atributos de la clase
        self.pila = []
        self.tope = 0

    def insertar_dato(self, dato): # Método para insertar datos a la pila
        if self.tope < 8: # Límite de la pila de 8 datos
            self.pila.append(dato)
            self.tope += 1
            print(f"Insertar ({dato},{self.tope})")
        else:
            print("Límite de pila alcanzado, no se pueden insertar más datos") # Mensaje para avisar que se alcanzó el límite

    def eliminar_dato(self): # Método para eliminar datos de la pila
        if self.tope > 0: # Si la pila tiene datos se pueden eliminar
            dato = self.pila.pop()
            print(f"Eliminar ({dato},{self.tope})")
            self.tope -= 1
        else:
            print("Pila vacía, no se pueden eliminar datos") # Mensaje para avisar que no hay datos para eliminar de la pila
# Se crea el objeto de la clase
Pl = Pila()
# Se usan los métodos de la clase
Pl.insertar_dato(1)
Pl.insertar_dato(2)
Pl.eliminar_dato()
Pl.eliminar_dato()
Pl.eliminar_dato()
Pl.insertar_dato(3)
Pl.insertar_dato(4)
Pl.eliminar_dato()
Pl.insertar_dato(5)