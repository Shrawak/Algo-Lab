import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations


def average_degree(G, v):
    totalDegree = 0
    for node in nx.nodes(G):
        count = 0
        for neighbor in nx.neighbors(G, node):
            count += 1
        totalDegree += count

    avgDegree = totalDegree/v
    print("Average Degree : ", int(avgDegree))
    return(int(avgDegree))


def density(G, v, e):
    if v > 1:
        print("Density : ", round((2*e)/(v*(v - 1)), 5))
        return(round((2*e)/(v*(v - 1)), 5))
    else:
        print("Density : 0")
        return(0)

def diameter(G,v):
    try:
        print('Degree :', nx.diameter(G))
        return nx.diameter(G)
    except:
        return "The graph is not connected so diameter is infinite"


def clustering_coefficient(G, v):
    clusterCoeff = 0
    for node in nx.nodes(G):
        Ki, Ei = 0, 0
        for i in G.neighbors(node):
            Ki += 1

        for v1, v2 in combinations(G.neighbors(node), 2):
            if G.has_edge(v1, v2):
                Ei += 1
        
        if Ki > 1:
            clusterCoeff += (2*Ei)/(Ki*(Ki - 1))
    
    print("Clustering Coefficient : ", round(clusterCoeff/v, 5))
    return(round(clusterCoeff/v, 5))


def degree_distribution(G, v):
    frequencyList = nx.degree_histogram(G)
    probDegreeList = [x/v for x in frequencyList]
    degreeList = [*range(0, len(frequencyList))]
    plt.plot(degreeList, probDegreeList, "g")
    plt.show()


if __name__ == "__main__":
    header_list = ["a", "b"]
    E = pd.read_csv('data/ia-reality.mtx', sep = " ", header = None, names = header_list)
    G = nx.from_pandas_edgelist(E, "a", "b")

    num_nodes = nx.number_of_nodes(G)
    num_edges = nx.number_of_edges(G)
    print("Number of nodes: ", num_nodes)
    print("Number of edges: ", num_edges)

    # nx.draw(G)
    plt.show()
    
    average_degree(G, num_nodes)
    density(G, num_nodes, num_edges)
    diameter(G, num_nodes)
    clustering_coefficient(G, num_nodes)

    degree_distribution(G, num_nodes)