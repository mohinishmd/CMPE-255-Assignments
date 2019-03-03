from collections import Counter
from statistics import mean
import math, random
import matplotlib.pyplot as plt
import data
from data import cities
import math

def vector_subtract(v, w):
    """subtracts two vectors componentwise"""
    return [v_i - w_i for v_i, w_i in zip(v,w)]
    
def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return math.sqrt(squared_distance(v, w))

def majority_vote(labels):
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority_vote(labels[:-1]) # try again without the farthest


def knn_classify(k, labeled_points, new_point):
    """each labeled point should be a pair (point, label)"""

    # order the labeled points from nearest to farthest
    by_distance = sorted(labeled_points,
                         key=lambda point_label: distance(point_label[0], new_point))

    # find the labels for the k closest
    k_nearest_labels = [label for _, label in by_distance[:k]]

    # and let them vote
    return majority_vote(k_nearest_labels)


def predict_preferred_language_by_city(k_values, cities):
    """
    TODO
    predicts a preferred programming language for each city using above knn_classify() and 
    counts if predicted language matches the actual language.
    Finally, print number of correct for each k value using this:
    print(k, "neighbor[s]:", num_correct, "correct out of", len(cities))
    """
    for i in range(0,len(k_values)):
        num_correct = 0
        for j in range(0,len(cities)):
            if cities[j][1] == knn_classify(k_values[i] , cities, (cities[j][0][0],cities[j][0][1])):
                num_correct += 1
        print(k_values[i], "neighbor[s]:", num_correct, "correct out of", len(cities))
        
if __name__ == "__main__":
    k_values = [1, 3, 5, 7]
    # TODO
    # Import cities from data.py and pass it into predict_preferred_language_by_city(x, y).
    predict_preferred_language_by_city(k_values, cities)
