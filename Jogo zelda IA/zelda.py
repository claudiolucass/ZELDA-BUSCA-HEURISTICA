import pygame
import numpy as np
import math
import time
from queue import PriorityQueue
mapa = [
    "fffffffffffffffmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "f     f f f        aadaa      aaaa mmmmmmmmm mm",
    "f     f   f       aaaaaaaa  aaaaaaaa mmmm    mm",
    "f    ff f f    aaaaaaaaaaaaaaaaaaaaaaa       mm",
    "f       f f    a  aaaaaaaa  aaaaaaaa         mm",
    "f     f f f    a   aaaaaa  r  aaaa  r        mm",
    "f     f f      a  mmmmmm   r        r        mm",
    "f     f f      aaaaaaaaaa  r        r        mm",
    "f       f   r    a    a    r        r        mm",
    "ffffffff   rrr             r        r        mm",
    "fffffff   rrrrr  fff fffff r        r        mm",
    "f f f      rrr            rrrrrrrrrrr        mm",
    "    f       r   rrrrrrrrrrr     f    f       mm",
    "    f           r         r          f       mm",
    "                r f    f  r  f   f   f       mm",
    " fffffff  fffff           r                  mm",
    "                r f    f                      m",
    "                r         r      aaaaadaa     m",
    "          ffff  rrrr  rrrrr      a aa aaa     m",
    "        fffffffff         r      aaaaaaaa     m",
    "        fffff fffff fff   r      a    a       m",
    " ffffff ffff   fffffff    r      aaaaaaaa     m",
    "     fffff      ffffff    r      a            m",
    "      fffff    ffffffff   r        aa         m",
    "       ffffff ffffff      r                   m",
    "                          r                   m",
    "                          r                   m",
    "                          r                   m",
    "                          r                   m",
    "                          r                   m",
    "                          rr rrrr             m",
    "                                r             m",
    "                                r             m",
    "                                r             m",
    "  aaaadaa           f     rrrrrrrrrrrrrr   m  m",
    "  aaaaaaa   f  rr   f     rrrrrrrrrrrrrr      m",
    "  aaaaaaa      rr   f     rrrrrrrrrrrrrr      m",
    "  aaaaaaa   f             rrrrrrrrrrrrrr      m",   
    "  aaaaaam   f     fff     rrrrrrrrrrrrrr      m",
    "  aaaaaaaa  f rrr  f      rrrrrrrrrrrrrr      m",
    "  aaaaaaaa         f      rrrrrrrrrrrrrr      m",
    "  aaaaaaaaa               rrrrrrrrrrrrrr      m",    
    "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
]

mapa_obj = [
    "               mmmmmmmmmmmmmmmmmmmmmmmmmmm",
    "                  mmmmmmmmmmmmmmmmmmmmmmmm",
    "                  mmmmmmmm               m",
    "                  mmm   mmm              m",
    "                   m                     m",
    "                   m                     m",
    "                                         m",
    "                                         m",
    "                                         m",
    "                                         m",
    "                                         m",
    "                                         m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                                        m",
    "m                               mmmmmmmm m",
    "m                                 m      m",
    "m                                 m      m",
    "m                                 m mmmm m",
    "m                                        m",
    "m          mmmmmmm  mmmm                 m",
    "mmmmmmmmmm m           m                 m",
    "m        m m           m                 m",
    "m        m m           m                 m",
    "m        m m           m                 m",
    "m        m             m                 m",
    "m        m             m                 m",
    "m        mmm           m                 m",
    "m         mm           m                 m",
    "m                      mmm               m",
    "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
]


AMARELO = (0xFF, 0xFF,0X00)
PRETO = (0X00, 0X00, 0X00)
AZUL = (0,0,285)

TELA_WIDTH = 800
TELA_HEIGHT = 600

BLOCK_WIDTH = TELA_WIDTH // 42
BLOCK_HEIGHT = TELA_HEIGHT // 42

custo_agua = 180
custo_areia = 20
custo_grama = 10
custo_montanha = 150
custp_floresta = 100

peso_dic = {' ':10,'f':100, 'm' :150, 'r': 180, 'a': 20, 'd': 10}


pygame.init()
tela = pygame.display.set_mode((TELA_WIDTH, TELA_HEIGHT))

def ImgTerreno(img_set, x, y):
    img_init = img_set.subsurface((x,y), (16, 16))
    img_scaled = pygame.transform.scale(img_init,(BLOCK_WIDTH, BLOCK_HEIGHT))
    return img_scaled


tiles = pygame.image.load("basictiles.png").convert_alpha()


img_rio = ImgTerreno(tiles, 80, 32)
img_areia = ImgTerreno(tiles,32, 16)
img_floresta = ImgTerreno(tiles, 80, 144)
img_montanha = ImgTerreno(tiles, 96, 112)
img_grama = ImgTerreno(tiles, 16, 128)
img_dungeon = ImgTerreno(tiles, 16, 64)
img_trajeto = ImgTerreno(tiles, 16,16)

#======= pinta o ponto vermelho do trajeto============
class trajeto(pygame.sprite.Sprite):
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)  
          self.image = img_trajeto
          self.rect = pygame.Rect((40, 40), (BLOCK_WIDTH, BLOCK_HEIGHT))

ponto = trajeto()            
conj_pontos = pygame.sprite.Group(ponto)
#=========================================================================

for id_linha, linha in enumerate(mapa):
    for id_coluna, caracter in enumerate(linha):          
            x = id_coluna * BLOCK_WIDTH
            y = id_linha * BLOCK_HEIGHT
            
            tela.blit(img_grama, (x, y)) #invés disso printar o objeto de trajeto
            if caracter == 'r':
                cor = AZUL

                pygame.display.update()
#==============pintando montanha========================           
for id_linha, linha in enumerate(mapa_obj):   
    for id_coluna, caracter in enumerate(linha):          
            x = id_coluna * BLOCK_WIDTH
            y = id_linha * BLOCK_HEIGHT
            if caracter == 'm':
                tela.blit(img_montanha, (x, y))
pygame.display.update()   
  
#==============pintando rio========================
for id_linha, linha in enumerate(mapa):   
    for id_coluna, caracter in enumerate(linha):          
            x = id_coluna * BLOCK_WIDTH
            y = id_linha * BLOCK_HEIGHT
            if caracter == 'r':
               tela.blit(img_rio, (x, y))
pygame.display.update()    

#==============pintando floresta========================
for id_linha, linha in enumerate(mapa):   
    for id_coluna, caracter in enumerate(linha):          
            x = id_coluna * BLOCK_WIDTH
            y = id_linha * BLOCK_HEIGHT
            if caracter == 'f':
               tela.blit(img_floresta, (x, y))
pygame.display.update()  
#=====================dungeon==================================
for id_linha, linha in enumerate(mapa):   
    for id_coluna, caracter in enumerate(linha):          
            x = id_coluna * BLOCK_WIDTH
            y = id_linha * BLOCK_HEIGHT
            if caracter == 'd':
               tela.blit(img_dungeon, (x, y))
pygame.display.update()

#==============pintando areia========================
for id_linha, linha in enumerate(mapa):   
    for id_coluna, caracter in enumerate(linha):          
            x = id_coluna * BLOCK_WIDTH
            y = id_linha * BLOCK_HEIGHT
            if caracter == 'a':
               tela.blit(img_areia, (x, y))
conj_pontos.draw(tela)
pygame.display.update()  
            
#=======================distanicia manhattan===============================================
def distancia_manhattan(self, ponto_partida, ponto_destino): 
     return abs(ponto_partida[0] - ponto_destino[0]) + abs(ponto_partida[1] - ponto_destino[1])
#===================adicionando coordenadas===============================================
ponto_partida = (25, 14)
ponto_destino = (3, 13)
celula_atual = ()
def medindo_distancia(ponto_partida, ponto_destino):
        x1, y1 = ponto_partida
        x2, y2 = ponto_destino
        return medindo_distancia(celula_atual.posicao, ponto_destino)*10

# a estrela=================================================================
class Nodes():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue


            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
#================================================================================
def verifica_visitado( x, y, visitados):
        for no in visitados:
            if no.x == x and no.y == y:
                return True
        return False    
                  
def verifica_heap( x, y, heap):
        for no in heap:
            if no.x == x and no.y == y:
                return True
        return False

class Nodex():
    def __init__(self, x, y, custo_g, custo_h, pai=None):
        self.x = x
        self.y = y
        self.custo_g = custo_g
        self. custo_h = custo_h
        self.custo_f = custo_g + custo_h
        self.pai = pai

    def _lt_(self, outro):
        return self.custo_f < outro.custo_f

def distancia_manhattan( ponto1, ponto2):
        return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])
    
def a_star(mapa, inicio, final):
        linhas, colunas = mapa.shape
        heap = []
        visitados = set()
        no_inicial =  Nodex(inicio[0], inicio[1], 0, distancia_manhattan(inicio, final))
        #heapq.heappush(heap, no_inicial)
        heap.append(no_inicial)

        while heap:
            #no_atual = heapq.heappop(heap)
            heap = sorted(heap, key=lambda no: no.custo_f)
            no_atual = heap.pop(0)
            visitados.add(no_atual)

            if(no_atual.x, no_atual.y) == final:
                path = []
                while no_atual:
                    path.append((no_atual.x, no_atual.y))
                    no_atual = no_atual.pai
                return path[::-1]

            for vizinho in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = no_atual.x + vizinho[0]
                y = no_atual.y + vizinho[1]

                if (x >= 0 and x < linhas and y >= 0 and y < colunas and not verifica_visitado(x, y, visitados) and not verifica_heap(x, y, heap)):
                    custo_g = no_atual.custo_g + mapa[x, y]
                    custo_h = distancia_manhattan((x, y), final)
                    novo_no = Nodex(x, y, custo_g, custo_h, no_atual)
                    #heapq.heappush(heap, novo_no)
                    heap.append(novo_no)

        return None

def main():
    def mapaCusto(mapa):
        mapaCusto = list()
        for id_linha, linha in enumerate(mapa):   
            linhaLista = list()
            for id_coluna, caracter in enumerate(linha):  
                linhaLista.append(peso_dic[caracter])        
            mapaCusto.append(linhaLista)
        return mapaCusto            
    maze = mapaCusto(mapa)
    maze = np.asarray(maze)

    start = (25, 28)
    end = (38, 16)
    path = a_star(maze, start, end)
    
    for x , y in (path):          
            x = x * BLOCK_WIDTH
            y = y * BLOCK_HEIGHT
            tela.blit(img_trajeto, (x, y)) 
            custo_grama
    time.sleep(0.3)                
    pygame.display.update()
    print(path)


if __name__ == '__main__':
    main()
# ====================================================================

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
