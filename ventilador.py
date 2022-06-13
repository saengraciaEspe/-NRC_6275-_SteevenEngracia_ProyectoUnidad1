from tokenize import Double


class ventilador:
    """
    Clase que representa un ventilador inteligente.
    ...
    
    Atributos
    ---------
    aencendido: boolean
                Indica si el ventilador se encuentra conectado.
    
    
    """
    def __init__(self,encendido=False):
        """Constructor usado para inicializar el ventilador

        Parámetros
        ----------
            encendido : boolean.
                        Indica si el ventilador se encuentra conectado.
        """
        self.aencendido=encendido

    def detallaren(self):
        """Detalla los parámetros de encendido al encender el ventilador

            Parámetros
            ----------
            No contiene parámetros
        
        """
        if not self.aencendido:
            print("Encendiendo ventilador...")
            print("Preparando motores...")
            print("Revisando sensores...")
            print("Se ha encendido sin ningún problema el ventilador")
        else:
            print("El ventilador ya está encendido")

    def detectartemp(self):
        """
        Revisa en el entorno si la temperatura ambiente excede la medidad
        tolerante 
        >27 C
        """
        entrada=Double(input("Extrayendo temperatura del ambiente..."))
        print("Procesando datos...")

        if entrada>=27:
        

