# Ball-Bearing-Fault-Analysis-and-Lifetime-Prediction

The goal is to analysis bi-axial accelerometer signal data collected from multiple different machines in their healthy and faulty (simulated) states and identify signals that typically detect faults in the bearings. This is a time-series analysis problem where detection of signals that denote faults in ball bearings is like anomaly detection. Once the fault signals are detected, the lifetime of the particular ball bearing is then predicted. 

This repo contains code for the fault detection part. Here the data is curated, denoised, features are extracted and observations are clustered to detect outliers (fault signals).

Stages:

1. Denoising: Moving average, Savitzky Golay and Gauissain (1D) filters were tried. Gaussian filter performed the best. It got rid of random erroneous noise readings while preserving the spikes and anomalies that denote faults.


2. Feature creation: 
	We performed two types of feature selection.
	
	1. Horizontal feature selection: In this, we calculated different measures like rms, kurtosis, mean, etc using x1 and x2 values. We formed 9 total columns using these values.
	
	2 . Vertical feature selection: In this, we calculated different measures like rms, kurtosis, mean, etc using
	sets of 100 rows of x1 and x2 each. We formed 18 columns here out of which 9 colums came from x1 and 9 from x2.	


3. Feature selection and dimensionality reduction:
To extract dominant and informative features from analyzed dataset features, we performed PCA on both our horizontally and vertically selected features. When performed on horizontally selected features, we found out that 99% variance is being captured at 4 features. When performed on vertically selected features, we found out that 99% variance is being captured at 7 features.
	
4. Clustering: To find outlier/fault signals
We used K-means clustering with 2 clusters. We also tried hierarchical (aglomerative) clustering which gave better inferences for use in the prediction model.
