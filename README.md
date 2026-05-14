# ML-Codes-py

A comprehensive collection of machine learning algorithms implemented in Python.

## Overview

This repository contains a variety of machine learning implementations including linear regression, logistic regression, decision trees, Gaussian mixture models, k-means clustering, k-medoids clustering, principal component analysis (PCA), random forests, support vector machines (SVM), and artificial neural networks (ANN). All programs are tested, viable, and error-free.

## Project Structure

```
ML-Codes-py/
├── datasets/          # Datasets folder containing all CSV files
├── *.py              # Individual ML algorithm implementations
├── *.csv             # Sample datasets
└── README.md         # This file
```

## Datasets

All datasets are provided in the `datasets/` folder within the project. These include:
- california_housing.csv
- iris.csv
- social.csv
- And other supporting datasets

## Getting Started

### Prerequisites

- Python 3.x
- pandas
- numpy
- matplotlib
- scikit-learn
- scipy

### Installation & Execution

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ML-Codes-py.git
   cd ML-Codes-py
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Before running any script**: Copy the required dataset from the `datasets/` folder to the main project directory:
   ```bash
   cp datasets/california_housing.csv .
   # or whichever dataset your script requires
   ```

4. Run any Python script:
   ```bash
   python linear.py
   python svm.py
   # etc.
   ```

## Available Algorithms

- **Linear Regression** (`linear.py`) - Basic linear regression implementation
- **Logistic Regression** (`logreg.py`) - Binary classification using logistic regression
- **K-Means Clustering** (`kmeans.py`) - Unsupervised clustering algorithm
- **K-Medoids Clustering** (`kmedoid.py`) - Clustering with medoids
- **Gaussian Mixture Model** (`gaussian.py`) - Probabilistic clustering
- **Principal Component Analysis** (`pca.py`) - Dimensionality reduction
- **Random Forest** (`randomforest.py`) - Ensemble learning method
- **Support Vector Machine** (`svm.py`) - Classification with SVM
- **Artificial Neural Network** (`Ann.py`) - Deep learning implementation
- And more...

## Notes

- All datasets must be copied from the `datasets/` folder to the current working directory before executing the respective scripts
- Each script is self-contained and can be run independently
- Output visualizations are saved as PNG files in the project directory

## Author

Your Name / Your Organization

## License

MIT License
