# InstagramML2017

## Features Extraction 

Code: ReadJSONAndExtractStatistics.py

The features are face features, label features and image features from "annotations" field in json data.

## Prediction model

Code: KNearestNeighborRegressor.py

We use a simple K-Nearest Neighbor model. The weights of all neighbors are calculated as the inversion of Euclidean distances.

## Prediction Submission
Code: APIGetNewImages.py

New data is requested every 6 seconds.
