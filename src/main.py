class No:

    def __init__(self, nome):
        self.nome = nome
        self.adjacentes = []
        self.antecessor = None
        self.distancia = -1

    def add_adjacente(self, adjacente, peso):
        self.adjacentes.append((adjacente, peso))
    
    def __str__(self):
        return self.nome

class Grafo:

    def __init__(self):
        self.nos = []
    
    def add_no(self, no):
        self.nos.append(no)
    
    def add_aresta(self, origem, destino, peso):
        for no in self.nos:
            if no.nome == origem:
                no.add_adjacente(destino, peso)
    
    def __str__(self):
        grafo = ''
        for no in self.nos:
            grafo += no.nome + ' -> ' + str(no.adjacentes) + '\n'
        return grafo
    

class Dijkstra:

    def __init__(self, grafo, start):
        self.grafo = grafo
        self.start = start
        self.vizitados = []
    
    def sequencia(self):
        self.zera()
        self.calcula()

    def zera(self):
        self.start.antecessor = self.start
        self.start.distancia = 0
    
    def calcula(self):
        # Não é necessário atribuir valor infinito, pois considerar infinito = -1
        # Enquanto houver nós não vizitados
        while len(self.vizitados) < len(self.grafo.nos):
            # Pega o nó com menor distância
            no = self.menor_distancia()
            # Vizita o nó
            self.vizita(no)
            # Calcula a distância dos nós adjacentes
            self.calcula_adjacentes(no)

    def menor_distancia(self):
        # Nesta função vou buscar o nó com menor distância
        # que ainda não foi vizitado
        menor = None
        # Percorre todos os nós
        for no in self.grafo.nos:
            # Se o nó não foi vizitado
            if no not in self.vizitados:
                # Se o nó for o primeiro a ser analisado
                if menor == None:
                    # O menor nó é o primeiro nó analisado
                    menor = no
                # Se o nó não for o primeiro a ser analisado
                else:
                    # Se a distância do nó analisado for menor que a do menor nó
                    if no.distancia < menor.distancia:
                        # O menor nó é o nó analisado
                        menor = no
        # Retorna o menor nó
        return menor
    
    def vizita(self, no):
        # Adiciona o nó na lista de nós vizitados
        self.vizitados.append(no)

    def calcula_adjacentes(self, no):
        # Percorre todos os nós adjacentes
        for adjacente in no.adjacentes:
            # Se o nó adjacente não foi vizitado
            if adjacente[0] not in self.vizitados:
                # Calcula a distância do nó adjacente
                self.calcula_adjacente(no, adjacente)

    def calcula_adjacente(self, no, adjacente):
        # Calcula a distância do nó adjacente
        distancia = no.distancia + adjacente[1]
        # Se a distância do nó adjacente for menor que a distância
        # que já está armazenada no nó adjacente
        if distancia < adjacente[0].distancia:
            # Atualiza a distância do nó adjacente
            adjacente[0].distancia = distancia
            # Atualiza o antecessor do nó adjacente
            adjacente[0].antecessor = no

grafo = Grafo()

grafo.add_no(No('A'))
grafo.add_no(No('B'))
grafo.add_no(No('C'))
grafo.add_no(No('D'))
grafo.add_no(No('E'))
grafo.add_no(No('F'))
grafo.add_no(No('G'))
grafo.add_no(No('H'))

grafo.add_aresta('A', 'B', 5)
grafo.add_aresta('A', 'C', 3)
grafo.add_aresta('A', 'D', 2)
grafo.add_aresta('B', 'E', 1)
grafo.add_aresta('B', 'F', 2)
grafo.add_aresta('C', 'G', 4)
grafo.add_aresta('D', 'H', 2)

print(grafo)