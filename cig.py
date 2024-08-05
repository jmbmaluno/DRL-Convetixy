import networkx as nx
import matplotlib.pyplot as plt

class CIG:
    def __init__(self, G):
        self.G = G
        self.L = set()
        
        #colorindo os vértices
        nx.set_node_attributes(self.G, 'gray', 'color')
    
    def plotar(self, final=None, time=0.5):
        plt.clf()
        nx.draw(self.G, 
                pos=nx.kamada_kawai_layout(self.G), 
                with_labels = True, 
                node_color = [self.G.nodes[v]['color'] for v in self.G])


        if final:
            plt.show()

        else:
            plt.ion()
            plt.pause(time)
            plt.ioff()
    

    def infect(self, v):
        self.L.add(v)
        self.update_L()
        #marcando os vértices que estão infectados
        self.G.nodes[v]['color'] = 'red'


    def update_L(self):
        #f2(L) = Ic(L)

        at = set()

        for v in self.L:
            for u in self.L:
                if u != v:
                    for P in nx.all_shortest_paths(self.G, source = v, target=u):
                        for k in P:
                            self.G.nodes[k]['color'] = 'red'
                            at.add(k)
        
        self.L = self.L.union(at)
    
    
    def start(self, version=1):
        #assumindo que a versão sempre será a normal
        turn = 1
        self.plotar()
        done = False
        player = ""

        while self.L != set(self.G.nodes):
        
            if turn%2 != 0:
                player = "PRIMEIRO JOGAGOR"
            else:
                player = "SEGUNDO JOGAGOR"
            
            res = input(player + ", escolha algum vértice: ")

            while res in self.L:
                print("NÂO PODE ESCOLHER VÉRTICES JÁ ROTULADOS")
                res = input(player + ", escolha algum vértice: ")
            
            self.infect(res)

            if self.L == set(self.G.nodes):
                if version==1:
                    print(player + " VENCEU O JOGO")
                else:
                    print(player + " PERDEU O JOGO")

                self.plotar(time = 2)
            else:
                self.plotar()

            turn = turn + 1
        
        

g = {'a': {'b'},
     'b': {'a', 'c'},
     'c': {'b', 'd', 'e'},
     'd': {'c'},
     'e': {'c', 'i', 'f'},
     'f': {'e', 'g', 'h'},
     'g': {'f'},
     'h': {'f'},
     'i': {'e', 'j'},
     'j': {'i'} 
    }

g2 = {'a': {'b', 'c', 'e'},
      'b': {'a', 'f'},
      'c': {'a', 'd'},
      'd': {'c', 'e'},
      'e': {'a', 'f', 'd'},
      'f': {'e', 'b'}
    } 

jogo = CIG(nx.Graph(g))
jogo.start()
