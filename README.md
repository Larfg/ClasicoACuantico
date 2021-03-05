# Librería de Clásico a Cuántico

Trabajo desarrollado en Python que proporciona una librería de distintos experimentos como los siguientes:

1. Los experimentos de la canicas con coeficiente booleanos
2. Experimentos de las múltiples rendijas clásico probabilístico, con más de dos rendijas.
3. Experimento de las múltiples rendijas cuántico.
4. Cree una función para graficar con un diagrama de barras que muestre las probabilidades de un vector de estados. La imagen se debe poder guardar en el computador con un formato de imagen.

## Comenzando 

### Pre-requisitos

Python 3.7.7, las librerías panda y matplotlib.pyplot

### Instalación

Descargue Python 3.7.7 de un sitio oficial y luego copie el archivo llamado *ClasicToCuantic.py* en donde quiera utilizarlo. Las librerías las puede descargar a través de su compilador de preferencia o manualmente (se recomienda buscar un tutorial de YouTube)

 ## Ejemplos

Estos son ejemplos de como utilizar todas las funciones implementadas.

1. Para poder experimentar con canicas únicamente ajuste la matriz de estados de las canicas (matriz binaria) a la que usted desee implementar, igualmente debe cambiar el vector de estados inicial, después de modificar el contenido de m y de v otro valor que puede modificar es el tercer parámetro de manyClicks para poder simular uno o más de un click.

   ```python
   #TestCase1: Canicas
       m = np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 1],
                     [0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0],
                     [1, 0, 0, 0, 1, 0]])#Esta es la matriz que puede modificar
       v = np.array([6, 2, 1, 5, 3, 10])#Este es el vector inicial que puede modificar
       a = manyClicks(m, v, 1)#De esta funcion puede cambiar el 1 por el numero de clicks que quiera
       print("Matriz estado:\n", a[0])
       print("vector estado:\n", a[1])
   ```

2. Para poder experimentar con las rendijas probabilísticas únicamente cambie el numero de rendijas y el numero de receptores a su gusto.

   ```python
   #TestCase2: Varias Rendijas Probabilisticas
       rendijas = 2#Este valor lo puede cambiar por otro numero entero
       receptores = 5#Este valor lo puede cambiar por otro numero entero
       vector1 = dobleRendijaProb(rendijas,receptores)
   ```

3. Para poder experimentar con las rendijas cuánticas igualmente que en el punto anterior puede modificar rendijas y receptores al gusto.

   ```python
   #TestCase3: Varias Rendijas Cuanticas
       rendijas = 2#Este valor lo puede cambiar por otro numero entero
       receptores = 5#Este valor lo puede cambiar por otro numero entero
       vector2 = dobleRendijaCuantum(rendijas,receptores)
   ```

4.  Para graficar un vector de estados solamente cambie el parámetro de la función graphVector por el vector que desee graficar, por defecto en la librería se grafican los vectores de estados de los 3 anteriores puntos.

   ```python
   #TestCase4: Graficar Vector de estado
       graphVector(a[1])
       graphVector(vector1)
       graphVector(vector2)
   ```

   Estas funciones se ejecutaran una por una (para avanzar a la siguiente cierre la que este abierta) y en el cuadro de la grafica encontrara la opción de guardarla en su computador como imagen.





## Ejecutando las pruebas 

Para ejecutar las pruebas ejecute el *ClasicToCuantic.py* en un compilador.

## Construido con 

- [PyCharm]([PyCharm: el IDE de Python para desarrolladores profesionales, por JetBrains](https://www.jetbrains.com/es-es/pycharm/)) - IDE utilizado para el desarrollo de la librería y el test.
- [Python 3.7.7]([Welcome to Python.org](https://www.python.org/)) - Lenguaje de la librería.

## Autores 

- **Luis Felipe Giraldo** -  [Larfg]([Larfg (github.com)](https://github.com/Larfg))

