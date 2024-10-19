class BipartiteGraph:
    def __init__(self, p1, p2, edges):
        """
        :param p1: Количество вершин в первой доле (V1)
        :param p2: Количество вершин во второй доле (V2)
        :param edges: Список рёбер
        """
        self.p1 = p1 
        self.p2 = p2
        self.edges = edges
        self.M = [0] * (p2 + 1)  
        self.x = [False] * (p1 + 1)  

    def Aug(self, v):
        """
        :param v: Вершина первой доли (V1)
        :return: True, если удалось найти увеличивающую цепь
        """
        if self.x[v]:
            return False  
        self.x[v] = True  

        for u in self.edges[v]:

            if self.M[u] == 0 or self.Aug(self.M[u]):
                self.M[u] = v  
                return True  

        return False  

    def maximum_matching(self):

        self.M = [0] * (self.p2 + 1)

        for v in range(1, self.p1 + 1):

            self.x = [False] * (self.p1 + 1)
            self.Aug(v)

        return self.M

if __name__ == "__main__":

    edges1 = {
        1: [1, 2, 3],
        2: [1, 2],
        3: [1],
    }
    graph1 = BipartiteGraph(p1=3, p2=3, edges=edges1)
    matching1 = graph1.maximum_matching()
    print("Пример 1: Паросочетание (M):")
    for u in range(1, len(matching1)):
        if matching1[u] != 0:
            print(f"Вершина {matching1[u]} первой доли связана с вершиной {u} второй доли.")

    print("\n")

    edges2 = {
        1: [2],
        2: [1, 3],
        3: [4],
        4: [2],
    }
    graph2 = BipartiteGraph(p1=4, p2=4, edges=edges2)
    matching2 = graph2.maximum_matching()
    print("Пример 2: Паросочетание (M):")
    for u in range(1, len(matching2)):
        if matching2[u] != 0:
            print(f"Вершина {matching2[u]} первой доли связана с вершиной {u} второй доли.")

    print("\n")

    edges3 = {
        1: [1, 2],
        2: [2, 3],
        3: [4],
        4: [5],
        5: [1],
    }
    graph3 = BipartiteGraph(p1=5, p2=5, edges=edges3)
    matching3 = graph3.maximum_matching()
    print("Пример 3: Паросочетание (M):")
    for u in range(1, len(matching3)):
        if matching3[u] != 0:
            print(f"Вершина {matching3[u]} первой доли связана с вершиной {u} второй доли.")