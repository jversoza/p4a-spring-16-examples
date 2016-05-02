import random
import math
scores = [23, 56, 12, 44, 87, 45, 76, 98, 25, 34, 76, 12, 78, 98, 78, 90, 89, 45, 77, 22, 11]
d = {k: [v] for k, v in enumerate(scores)}

def create_centroids(k, data):
    centroids = []
    centroid_count = 0
    centroid_keys = []

    while centroid_count < k:
        rkey = random.randint(1, len(data))
        centroids.append(data[rkey])
        centroid_keys.append(rkey)
        centroid_count += 1
    return centroids

def create_centroids(k, data):
    return random.sample(list(data.values()), k)

#print(d)
#print(create_centroids(5, d))

def distance(p1, p2):
    # get the sum of the squares of all differences
    sum = 0
    for index in range(len(p1)):
        diff = (p1[index] - p2[index]) ** 2
        sum += diff
    # take the square root of the result
    return math.sqrt(sum)

#print(distance((5, 0), (2, 12)))

def distance(p1, p2):
    # use zip to create tuples of each component of each point
    # p1 = (1, 2, 3) and p2 = (4, 5, 6)... so zip (1, 4), (2, 5) ...
    # unpack
    # list comprenesion
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(p1, p2)]))

#print(distance((5, 0), (2, 12)))

def create_clusters(k, centroids, data, repeats):
    centroids = [[90], [34], [76], [87], [78]]
    # do this x number of times
    for apass in range(repeats):
        print("****PASS", apass, "****") 

        # reset clusters...
        # initialize an empty list of lists 
        # (each centroid will have its own set of elements)
        # or clusters
        clusters = []
        for i in range(k):
            clusters.append([])

        # go through every data element and construct
        # a list of distances to each centroid
        for key in data:
            distances = []
            for cluster_index in range(k):
                # print('data', data[key], 'centroids', centroids[cluster_index])
                dist = distance(data[key], centroids[cluster_index])
                distances.append(dist)
            # find the smallest distance
            min_distance = min(distances)
    
            # add this data element's key to the cluster
            i = distances.index(min_distance)
            clusters[i].append(key)
        print('clusters mid', clusters)
    
        # how many dims are in a single "point"
        dimensions = len(data[0])
    
        
        # this is finding the average part!
        # for every cluster
        for cluster_index in range(k):
    
            # take the sums of all components of each point in that cluster
            sums = [0] * dimensions
    
            # just adding
            for key in clusters[cluster_index]:
                datapoints = data[key]
                #print('datapoints', datapoints)
                for ind in range(len(datapoints)):
                    sums[ind] += datapoints[ind]
    
            # now dividing to get average
            for ind in range(len(sums)):
                cluster_len = len(clusters[cluster_index])
                if cluster_len != 0:
                    sums[ind] = sums[ind] / cluster_len
    
            # new centroid ftw!
            centroids[cluster_index] = sums
    
        for c in clusters:
            print("CLUSTER")
            for key in c:
                print(data[key], end=" ")
            print()
    return clusters
        
centroids = create_centroids(5, d)
create_clusters(5, centroids, d, 2)
   
"""
def create_clusters(k, centroids, data, repeats):
    clusters = [[] for i in range(5)]
"""

    



