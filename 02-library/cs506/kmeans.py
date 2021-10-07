from collections import defaultdict
from math import inf
import random
import csv

def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    n = len(points) # length of points
    if n == 0:
        return []
    d = len(points[0]) # number of dimensions in points
    center = [0.0] * d
    
    for point in points:
        for i in range(d):
            center[i] += point[i]
    
    center = [i / n for i in center]

    return center


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    # Find number of clusters, k
    k = max(assignments) + 1
    print("----------------------------")
    print(k)
    print("----------------------------")
    centers = []
    for cluster_i in range(k):
        # Find all samples in cluster i
        cluster_i_samples = []
        for sample_i in range(len(dataset)):
            if assignments[sample_i] == cluster_i:
                cluster_i_samples.append(dataset[sample_i])
        
        # Find centroid of all samples
        # print("----------------------------")
        # print(cluster_i, " has ", cluster_i_samples, "center:")
        # print(point_avg(cluster_i_samples))
        # print("----------------------------")
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
    if isinstance(a, int):
        tmp = a
        a = [0 for i in range(len(b))]
        a[0] = tmp
    if isinstance(b, int):
        tmp = b
        b = [0 for i in range(len(a))]
        b[0] = tmp
    if len(a) == 0 or len(b) == 0:
        return 0

    dist_hyp = 0
    for i in range(len(a)):
        dist_hyp += (a[i] - b[i]) ** 2
    dist_hyp = dist_hyp ** (1/2)

    return dist_hyp

def distance_squared(a, b):
    return distance(a, b) ** 2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    n = len(dataset) - 1
    centroids = []
    chosen_index = []

    for _ in range(k):
        idx = random.randint(0,n)
        while idx in chosen_index:
            idx = random.randint(0,n)
        centroids.append(dataset[idx])
        chosen_index.append(idx)

    return centroids


def cost_function(clustering):
    # sum of distances squared
    res = 0
    origin = [0 for i in range(len(clustering))]
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
    weights = [distance(a,0) for a in dataset]
    print("----------------------------")
    print("Starting new clustering")
    print(k)
    print("----------------------------")
    n = len(dataset)
    dataset_i = range(n)
    centroids = []
    chosen_index = []
    
    for _ in range(k):
        idx = random.choices(dataset_i,weights=weights, k=1)[0]
        while idx in chosen_index:
            idx = random.choices(dataset_i,weights=weights, k=1)[0]
        centroids.append(dataset[idx])
        chosen_index.append(idx)

    return centroids
    # return random.choices(dataset,weights=weights, k=1)


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
