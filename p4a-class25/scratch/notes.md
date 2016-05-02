machine learning
-----
* __supervised__ = your algorithm is trained with data that has "labels"
* __unsupervised__ = your algorithm just figures out the "labels"

We're going to be looking at classification.

* taking some data and dumping into a category or bucket
* there are kinds of machine learning (regression, etc.)

Our data... will sometimes be called __data point__, __instance__

                                each component of a point is some sort of feature
* each component of a data point   \/
* single data point for a student [m1, m2, final]
* features can be multidimensional (obvs just like ^), or you can have a single feature too [m1]
* you'll have a lot of data points for a class

classification algo that we're using is k-means clustering

* unsupervised learning (the algo isn't trained with data with labels)
* k-means

1. choose k clusters <-- (this is pretty significant to outcome of algo)
2. pick k random points from our data set (k random points are our initial set of centroids)
3. go through all points in data set....
4. drop them in the closest centroid (which forms a cluster)
5. calculate a new centroid.... by taking the average of all of the features in that cluster
6. go back to number 3!




















