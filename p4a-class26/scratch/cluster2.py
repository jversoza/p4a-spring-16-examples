import random
import math

test_scores = [23, 56, 12, 44, 87, 45, 76, 98, 25, 34, 76, 12, 78, 98, 78, 90, 89, 45, 77, 22, 11]
d = [[score] for score in test_scores]
def create_centroids(k, data):
    """returns a list of values, each value a list
    ... that's a random sampling of data
    """
    used_indexes = []
    centroids = []
    centroid_count = 0
    while centroid_count < k:
        score_index = random.randint(0, len(data) - 1)
        if score_index not in used_indexes:
            centroids.append(data[score_index])
            used_indexes.append(score_index)
            centroid_count += 1
    return centroids

print(create_centroids(5, d))

def create_centroids(k, data):
    return random.sample(data, k)

print(create_centroids(5, d))


def distance(p1, p2):
    # get the sum of the squares of all differences
    sum = 0
    for index in range(len(p1)):
        diff = (p1[index] - p2[index]) ** 2
        sum += diff
    # take the square root of the result
    return math.sqrt(sum)
        
def distance(p1, p2):
    # use zip to create tuples of each component of each point
    # p1 = (1, 2, 3) and p2 = (4, 5, 6)... so zip (1, 4), (2, 5) ...
    # unpack
    # list comprenesion
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))
    
# clusters = list of lists
# each cluster is a list of indexes

# centroids are _actual_ insances
def create_clusters(k, centroids, data, repetitions):
    print(centroids)
    centroids = [[90], [34], [76], [87], [78]]
    for repetition in range(repetitions):
        print("PASS ", repetition)

        # reset clusters
        clusters = []
        for i in range(k):
            clusters.append([])

        # how far is each instance, piece of data from the centroid
        # sooo... list of lists, with centroid index matching index
        # of distances
        # entire list is every instance, each element is (num centroids) 
        # length list
        for i, score in enumerate(data):
            distances = []
            for j, centroid_value in enumerate(centroids):
                distances.append(distance(score, centroid_value))
            min_distance = min(distances)
            #print('distances', distances)
            # find an index... so we can match with clusters
            related_cluster = distances.index(min_distance)
            #print(related_cluster)
            clusters[related_cluster].append(i)
                
        # get the average of each "feature"... so sum, then divide per
        # component

        #print('clusters mid', clusters)
        num_features = len(data[0])

        # do this for every cluster to get a new centroid for that cluster
        for cluster_index, cluster in enumerate(clusters):
            #print('cluster', cluster)

            # we'll need to add up all of the features for this cluster
            sums = [0] * num_features

            # for every instance / data we have
            for instance_index, data_index in enumerate(cluster):
                instance = data[data_index]
                #print('instance', instance)

                for feature_index, feature in enumerate(instance):
                    sums[feature_index] += feature

            # we have all of the sums for each feature
            # go over every sum, then every feature
            for j, feature_sum in enumerate(sums):
                if len(clusters[cluster_index]) != 0:
                    sums[j] /= len(clusters[cluster_index])

            centroids[cluster_index] = sums

        for c in clusters:
            print("CLUSTER")
            for key in c:
                print(data[key], end=' ')
            print()
    return clusters

centroids = create_centroids(5, d)
create_clusters(5, centroids, d, 100)

with open('earthquakes.txt', 'r') as f:
    data = []
    for line in f:
        line_parts = line.split()
        lat, lon = float(line_parts[3]), float(line_parts[4])
        data.append([lat, lon])
    print(data)
    centroids = create_centroids(5, data)
    clusters = create_clusters(5, centroids, data, 100)
    print(clusters)




    # --- Build Map ---
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt
 
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
