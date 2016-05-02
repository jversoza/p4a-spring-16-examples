import random
import math
test_scores = [23, 56, 12, 44, 87, 45, 76, 98, 25, 34, 76, 12, 78, 98, 78, 90, 89, 45, 77, 22, 11]

# data will be in array
# each data "point" will also be an array, with each component a "feature"
# test scores [[23], [67] ...]
# earthquaks [[20.282, -156.611] [59.808, -152.538] ... ]
d = [[score] for score in test_scores]


# centroid will be a list of data points
# (that is a subset of above)
# test scores [[23], [67] ...] (but only k elements)
def create_centroids(k, data):
    used_indexes = []
    centroids = []

    while len(centroids) < k:
        random_index = random.randint(0, len(data) - 1)
        if random_index not in used_indexes:
            centroids.append(data[random_index])
            used_indexes.append(random_index)
    return centroids
print(create_centroids(5, d))

def create_centroids(k, data):
    return random.sample(data, k)

print(create_centroids(5, d))

def distance(p1, p2):
    """ euclidean distance

    p1 is an array of features
    p2 is an array of features
    p1 and p2 should be the same size!
    """
    sum_all = 0
    for i, value in enumerate(p1):
        diff_squared = (value - p2[i]) ** 2
        sum_all += diff_squared
    return math.sqrt(sum_all)

print(distance((5, 0), (2, 12)))


def distance(p1, p2):
    sum_all = 0
    for value1, value2 in zip(p1, p2):
        diff_squared = (value1 - value2) ** 2
        sum_all += diff_squared

    return math.sqrt(sum_all)

print(distance((5, 0), (2, 12)))

def distance(p1, p2):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))

print(distance((5, 0), (2, 12)))

def initialize_empty_clusters(k):
    """ initialize clusters

    create a list of empty lists, with len k
    """
    clusters = []
    for i in range(k):
        clusters.append([])
    return clusters

print(initialize_empty_clusters(5))

def initialize_empty_clusters(k):
    return [[] for i in range(k)]

print(initialize_empty_clusters(5))

def calculate_distances(data_point, centroids):
    """ generate a list of distances 
    
    retursn a list of distances from this data ponit to each centroid
    ... should be same length as centroids!
    """

    distances = []
    for centroid in centroids:
        distances.append(distance(data_point, centroid))
    return distances

print(calculate_distances([12], [[5],[10],[15]]))

def calculate_distances(data_point, centroids):
    return list(map(lambda centroid: distance(data_point, centroid), centroids)) 

print(calculate_distances([12], [[5],[10],[15]]))

def create_clusters(k, centroids, data):
    """ clusters data based on nearest centroids

    will create a list of lists of indexes to data

    indexes...
     \/
    [[7, 13, 15, 16], [0, 2, 3, 5, 8, 9, 11, 17, 19, 20], [1, 6, 10, 18], [4], [12, 14]]
    """
    # initialize clusters
    # list of empty lists, size k
    # clusters will be a list of indexes! 
    # not the actual data itself!
    clusters = initialize_empty_clusters(k)


    # for every data point / instance
    # create a list of distances
    #    data      [[], [], ...]
    #                0   1     N
    # so distances [[], [], ...]
    for data_index, data_point in enumerate(data):
        distances = calculate_distances(data_point, centroids)

        # get the min distance (closest)
        # the index of that distance will be the index of your closest centroid!
        min_distance = min(distances)
        cluster_index = distances.index(min_distance)
        #print('cluster_index', cluster_index)

        # add the index of the data to this cluster
        clusters[cluster_index].append(data_index)
    return clusters

print(create_clusters(5, [[90], [34], [76], [87], [78]], d))

def generate_new_centroids(clusters, data):

    new_centroids = []
    # for every cluster
    #   for every point in cluster
    #      for every component
    #         add to sum
    # for every cluster
    #   for every summed component
    #     divide by num of features
    num_features = len(data[0])
    for cluster in clusters:
        # add all features for all points in this cluster
        feature_sums = [0] * num_features
        new_centroid = []
        for point_index in cluster:
            point = data[point_index]
            for feature_index, feature_value in enumerate(point):
                feature_sums[feature_index] += feature_value

        # now... try to divide by the number of points in this cluster
        # (ignore if 0)
        for feature_sum in feature_sums:
            try:
                new_centroid.append(feature_sum / len(cluster))
            except:
                pass
        new_centroids.append(new_centroid)
    return new_centroids

print('generating new centroids', generate_new_centroids([[7, 13, 15, 16], [0, 2, 3, 5, 8, 9, 11, 17, 19, 20], [1, 6, 10, 18], [4], [12, 14]], d))


def k_means(k, data, repeats):
    centroids = create_centroids(k, data)
    #centroids = [[90], [34], [76], [87], [78]]
    #centroids = [[90], [34], [76], [87], [78]]
    for rep in range(repeats):
        print("\nPASS", rep)
        clusters = create_clusters(k, centroids, data)
        for c in clusters:
            print("CLUSTER")
            for key in c:
                print(data[key], end=' ')
            print()
        centroids = generate_new_centroids(clusters, data)
    return clusters

k_means(5, d, 2)



from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

with open('earthquakes.txt', 'r') as f:
    data = []
    for line in f:
        line_parts = line.split()
        lat, lon = float(line_parts[3]), float(line_parts[4])
        data.append([lat, lon])
    print(data)
    clusters = k_means(5, data, 1000)
    print(clusters)

 
    eq_map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
    eq_map.drawcoastlines()
    eq_map.drawcountries()
    eq_map.fillcontinents(color = 'gray')
    eq_map.drawmapboundary()
 
    colors = ['red', 'green', 'blue', 'yellow', 'orange']
    for cluster_num, cluster in enumerate(clusters):
        print('cluster', cluster)
        for i, data_index in enumerate(cluster):
            lat, lon = data[data_index]
            x,y = eq_map(lon, lat)
            eq_map.plot(x, y, marker='o', color=colors[cluster_num])
 
    plt.show()



