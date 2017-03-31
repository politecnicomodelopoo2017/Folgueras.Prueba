

class Equipo(object):

    Nombre = ""
    Barrio = ""
    Capitan = ""

    def __init__(self):
        self.Lista_Jugadores = []
        self.Turno = [[False, False, False], [False, False, False],
                      [False, False, False], [False, False, False],
                      [False, False, False], [False, False, False]]

    def setNombre(self, Nom):
        self.Nombre = Nom

    def setBarrio(self, B):
        self.Barrio = B

    def Capitan_E(self, Cap):
        self.Capitan = Cap

    def agregarJugador(self, J):
        for item in self.Lista_Jugadores:
            if item.Num_Camiseta == J.Num_Camiseta:
                return False
        self.Lista_Jugadores.append(J)

    def setTurno(self, Dia, Tiempo, Activo):
        self.Turno[Dia][Tiempo] = Activo
