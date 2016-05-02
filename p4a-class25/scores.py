"""
data set will look like this
[[23], [56] ... ] <--- size going to be length of data set

when we first calculate the centroids
[[23], [56]...] <--- size is going to be k

clusters will look like
each sub list is a cluster
each element in cluster... is the original index of the actual data point
[[1, 2, 8], [9, 10, 3] ...] <--- size is going to be k

1. choose k centroids/clusters <-- (this is pretty significant to outcome of algo)
2. pick k random points from our data set (k random points are our initial set of centroids)
3. go through all points in data set....
4. drop them in the closest centroid (which forms a cluster)
5. calculate a new centroid.... by taking the average of all of the features in that cluster
6. go back to number 3!
"""
import random
import math

test_scores = [23, 56, 12, 44, 87, 45, 76, 98, 25, 34, 76, 12, 78, 98, 78, 90, 89, 45, 77, 22, 11]

d = [[score] for score in test_scores]

def generate_initial_centroids(k, data):
    """ we're going to choose k data points from data

    no duplicate centroids
    """
    centroids = []
    used_indexes = []
    while len(centroids) < k:
        random_index = random.randint(0, len(data) - 1)
        if random_index not in used_indexes:
            centroids.append(data[random_index])
            used_indexes.append(random_index)
    return centroids

print(generate_initial_centroids(5, d))

def generate_initial_centroids(k, data):
    return random.sample(data, k)

print(generate_initial_centroids(5, d))



def distance(p1, p2):
    """returns euclidean distance
    p1 is a list of features
    p2 is alsoa a list of features
    p1 and p2 should be the same size

    distance is the squareroot
    of sum of all squares of differences for each feature
    """

    """
    (p1[0] - p2[0]) ** 2 + 
    (p1[1] - p2[1]) ** 2 + 
    """
    sum_all = 0
    for i, v in enumerate(p1):
        diff_squared = (v - p2[i]) ** 2
        sum_all += diff_squared
    return(math.sqrt(sum_all))

print(distance((5, 0), (2, 12)))


def distance(p1, p2):
    sum_all = 0
    for v1, v2 in zip(p1, p2):
        diff_squared = (v1 - v2) ** 2
        sum_all += diff_squared
    return(math.sqrt(sum_all))

print(distance((5, 0), (2, 12)))

def distance(p1, p2):
    return math.sqrt(sum([(v1 - v2) ** 2 for v1, v2 in zip(p1, p2)]))

print(distance((5, 0), (2, 12)))

"""
we can generate centroids
we also have eulidean distance
generate clusters
    get the distances of ever data point compared to every centroid
"""



def calculate_distances(data_point, centroids):
    """ what are all of the distances between this data point
    and the centroids
    (eventually... we'll find the min distance, which will identity nearest centroid)
    """
    distances = []
    for centroid_index, centroid_value in enumerate(centroids):
        distances.append(distance(data_point, centroid_value))
    return distances

print(calculate_distances([12], [[5],[10],[15]]))


def calculate_distances(data_point, centroids):
    return list(map(lambda centroid_value: distance(data_point, centroid_value), centroids))

print(calculate_distances([12], [[5],[10],[15]]))
"""
          actual feature values
              \/
centroids = [[16], [12]] <--- size is k

         list of indexes in the original incoming data
           \/
cluster = [[1, 6, 3]... ] <--- size is als k
"""
def generate_clusters(k, centroids, data):
    
    # where to store clusters?
    # initialize clusters to list of empty lists
    clusters = [[] for i in range(k)]


    # go through every data point
    for data_index, data_point in enumerate(data):
        # get all of the distances for that data point
        """what is the size of distances going to be?"""
        distances = calculate_distances(data_point, centroids)
        min_distance = min(distances)
        min_index = distances.index(min_distance)
        clusters[min_index].append(data_index)
        """
        centroids [[] ... k]
                    0
        distances [[] ... k]
                    0                   
        clusters [[3, 1 ,4] ... k]
        """
    return clusters

print(generate_clusters(5, [[90], [34], [76], [87], [78]], d))

"""
x created inital centroids
x we've clusters
x generate new centroids 

generate_new_centroids
for cluster in clusters
    for data_point in cluster
        for feature in data point
            add feature values together
    go through all sums of features
        divide by number of data points in cluster
"""
def generate_new_centroids(clusters, data):
    for cluster_index, cluster in enumerate(clusters):
        # initialize a bunch of 0's
        # based on how many features we have per data point
        sum_features = [0] * len(data[0])
        for data_point_i, data_index in enumerate(cluster):
            data_point = data[data_index]



















































