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