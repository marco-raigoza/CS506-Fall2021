from collections import defaultdict
from math import inf
import random
import csv
# import numpy as np


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    if len(points) == 0:
        return []

    center = [0 for i in range(len(points[0]))]
    for point in points:
        for i in range(len(point)):
            center[i] += point[i]
        tmp = [i / 2 for i in center]
        center = tmp
    # raise NotImplementedError()
    return center


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    # raise NotImplementedError()
    # Find k
    k = 0
    while (k in assignments):
        k = k + 1

    centers = []
    for cluster_i in range(k):
        # Find all samples in cluster i
        cluster_i_samples = []
        for sample_i in range(len(dataset)):
            if dataset[sample_i] == cluster_i:
                cluster_i_samples.append(dataset[sample_i])
        
        # Find centroid of all samples
        centers.append(point_avg(cluster_i_samples))

    return centers

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    # raise NotImplementedError()
    if len(a) == 0 or len(b) == 0:
        return 0
    # center = []
    # for i in range(len(a)):
    dist_x = (a[0] - b[0]) ** 2
    dist_y = (a[1] - b[1]) ** 2
    dist_hyp = (dist_x + dist_y) ** (1/2)
    return dist_hyp

def distance_squared(a, b):
    # raise NotImplementedError()
    return distance(a, b) ** 2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    # raise NotImplementedError()
    return random.choices(dataset, k=k)

def cost_function(clustering):
    # raise NotImplementedError()
    # sum of distances squared
    res = 0
    origin = [0 for i in range(len(clustering[0]))]
    for point in clustering:
        res += distance_squared(point, origin)

    return res


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    # dist(a,b) / costfunction
    # raise NotImplementedError()
    


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
