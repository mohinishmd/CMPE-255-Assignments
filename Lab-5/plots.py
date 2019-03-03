import data
import linear_algebra
import knn
from knn import *
from collections import Counter
from statistics import mean
import math, random
import matplotlib.pyplot as plt
from data import cities
from linear_algebra import distance

def plot_state_borders(plt, color='0.8'):
    pass

def plot_cities(cities):

    plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }
    markers = { "Java" : "o", "Python" : "s", "R" : "^" }
    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }

    for (longitude, latitude), language in cities:
        plots[language][0].append(longitude)
        plots[language][1].append(latitude)

    for language, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[language], marker=markers[language],
                          label=language, zorder=10)

    plot_state_borders(plt)    

    plt.legend(loc=0)          
    plt.axis([-130,-60,20,55]) 
    plt.title("Popular Programming Languages")
    plt.show()


def classify_and_plot_grid(cities, k=1):
    plots = { "Java" : ([], []), "Python" : ([], []), "R" : ([], []) }
    markers = { "Java" : "o", "Python" : "s", "R" : "^" }
    colors  = { "Java" : "r", "Python" : "b", "R" : "g" }


    for longitude in range(-130,-60):
        for latitude in range(20, 55):
            city = knn_classify(k, cities, (longitude,latitude))
            plots[city][0].append(longitude)
            plots[city][1].append(latitude)
            
    for language, (x, y) in plots.items():
        plt.scatter(x, y, color=colors[language], marker=markers[language],
                          label=language, zorder=10)

    plot_state_borders(plt)    
    
    print("Popular Programming Languages k = ",k)
    plt.legend(loc=0)          
    plt.axis([-130,-60,20,55]) 
    plt.show()
    print()


if __name__ == "__main__":
#    print(cities)
    plot_cities(cities)
    classify_and_plot_grid(cities)
    classify_and_plot_grid(cities, 3)
    classify_and_plot_grid(cities, 5)
