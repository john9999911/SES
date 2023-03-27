import numpy as np


class Entropy:
    def __init__(self, data):
        self.data = data
        means = np.mean(data, axis=0)
        stds = np.std(data, axis=0)
        normalized_data = (data - means) / stds
        covariance_matrix = np.cov(normalized_data, rowvar=False)
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
        self.weight = weights = eigenvectors[:, 0] / np.sum(eigenvectors[:, 0])
        weighted_data = normalized_data * weights
        self.scores = np.sum(weighted_data, axis=1)


# if __name__ == '__main__':
#     data = person.get_dataframe()
#     entropy = Entropy(data)
