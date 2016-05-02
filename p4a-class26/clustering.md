K-Means Clustering
=====


Background Information
-----

Clustering is a technique that attempts to group together related data. 

* the clusters that result from this grouping have exhibit some kind of similarity to each other while showing a dissimilar relationship to data values outside of the cluster
* these relationships are usually not well known beforehand, and consequently clustering is used to reveal hidden properties of the data being analyzed

Clustering belongs to a larger group of machine learning techniques called unsupervised learning. As a result, learning some machine learning terminology is useful when discussing clustering.

* __supervised learning__ - a category of machine learning where the algorithm is provided with inputs and _correct_ outputs so that it can "learn" what to do with future unknown inputs
    * detecting faces (algorithm needs to know what a face is!)
    * given a list of movies and a personal ratings of those movies, recommend movies
* __unsupervised learning__ - a category of machine learning where the algorithm does not know what the _right_ answer is, but is instead is meant to discover hiddenattributes about data, or group/cluster data together
    * given a mixture of two sound sources (for example, a person talking over some music), separate the two 
    * market segmentation... given demographic information / survey results on potential buyers of 5 different models of a computer, determine which model to pitch to someone
* __observation, instance, data point__ - a single piece of data in a data set
* __feature__ - an attribute of a data point
    * data points can have one or more features... and features can be numeric, categorical, etc.
    * you can think of a data point as having a list/array/vector of features

Again, clustering is unsupervised learning.

K-means is a clustering algorithm
-----

### Overview

* it takes k number of specified clusters
* and groups data points from a data set into those clusters
* ... based on euclidean distance of each data point's features

### Terminology

* __euclidean distance__ - a method for determining "closeness" of two data points by taking their features and taking the square root of (the sum of all ((differences of each feature in both data points) squared))
* __centroid__ -  the mean of a collection of data points (that is, take the average of each feature in every data point, and create a point out of that)

### Algorithm

Before you start, it may make sense to make sure your data points have features that are numeric:

* rating: 1 - 5 stars
* test scores: 0 - 99 points
* latitude: 40.7128 degrees
* weight: 50kg

Any features that aren't numeric? Make them numeric.

1. choose k clusters to begin with
2. create k centroids by choosing k random data points from your data set
3. create a cluster for each centroid... 
4. group together data points in each cluster by determining which centroid they are closest to
5. for every cluster, calculate new centroids by taking the average of each feature in all data points in a cluster 
"""


"""
Clustering test scores!
-----

### Problem Statement and Background

Imagine you're grading exam scores for this class. 

1. The test scores are from 0 to 100
2. You have to assign letter grades to each test score: A, B, C, D, and F
3. You'd like to assign letter grades by how students' scores cluster together

For example, the scores may be:

23, 56, 12, 44, 87, 45, 76, 98, 25, 34, 76, 12, 78, 98, 78, 90, 89, 45, 77, 22, 11

How many features are in each data point in this data set?

* data set is all scores
* each data point has only one feature, a test score

### What Do We Keep Track of, and What Data Structures Do We Use

1. what will a data point look like, be represented by?
2. ...and what about a data set?
3. what will a centroid be?... and what should all of them be put in?
4. how about clusters?
5. distances of data points to in cluster to centroid


the __data set__, that is all the test scores, will look like this 

* each element, or data point is a list/array/vector of features
* `[[23], [56] ... ] # <--- size going to be length of data set`

each __centroid__ will look like this:

* each centroid must have all features of a data point
* so a single centroid is, again, a list/array/vector of features
* `[23] #<--- a single data point with one feature, exam score` 

all of our __centroids together__ will look like this:

* we'll just have a list...
* `[[23], [56]...] #<--- size is going to be k`

__clusters__ will look like:

* a list of lists... each sub list is a cluster
* each element in cluster... is the original index of the actual data point (not the data point itself!)
* `[[1, 2, 8], [9, 10, 3] ...] #<--- size is going to be k`
* (that's a list of clusters, which each cluster being a list of indexes to the original data point)
* (looking back at the book implementation, it probably would have made more sense to have a list of clusters as a list of dictionaries or a list of cluster objects!)

1. (function) generate initial centroids
2. (function) generate clusters 
    1. (function or list comprehension) create k empty clusters
    2. for every data point...
        1. (function) calculate distances (of all data points in cluster to centroid) 
            1. create an empty list of distances and populate with...
            1. (function) distance from data point to each centroid
        2. get min distance
        3. determine which cluster to put data point in based on min distance
        4. add data point to cluster
    3. give back clusters
3. (function) generate new centroids
