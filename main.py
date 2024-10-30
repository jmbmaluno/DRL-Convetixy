from cig import *
from pcig import *

for g in os.listdir("entradas"):
   grafo = np.genfromtxt("entradas/" + g)
   jogo = PCIG(nx.from_numpy_array(grafo))
   jogo.start()