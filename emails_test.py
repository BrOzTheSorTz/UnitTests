import unittest
#A continuación comprobaremos el código escrito
#para ver si falla algo mediante unit test

#Primero importamos la función que queremos testear
from emails import find_email

class TestEmail(unittest.TestCase):
  def test_basico(self):
    inicio = [None,"Blossom","Gill"]  #Lo ponemos de esta forma porque estamos usando
						  #la línea de comando para pasar todo
    final = "blossom@abc.edu"
    self.assertEqual(find_email(inicio),final)
  
  #A continuación comprobaremos que pasa si solo metemos o un nombre o un apellido
  def test_un_nombre(self):
    inicio = [None,"Roberto"]
    final = "Nombre incompleto"
    self.assertEqual(find_email(inicio),final)#Comprueba si ambas cosas son iguales y si no
 							    #lanza an AssertionError

    #Sin embargo cuando lo ejecutamos vemos que no ha habido un assertionerror si no un
    # index error, luego corregiremos eso en nuestro script


  #Otro posible fallo que debemos testear es que pasa si el nombre no está en el diccionario
  def test_nombre_incorrecto(self):
    inicio =[None, "Jose", "Soriano"]
    final = "No esta ese nombre en la lista"
    self.assertEqual(find_email(inicio),final)
#Para que corra lo anterior ponemos lo siguiente
if __name__ == "__main__":
  unittest.main()