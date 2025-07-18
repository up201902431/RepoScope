from collections import defaultdict

import numpy as np
from sklearn.cluster import KMeans


class KMeansCluster:
    @staticmethod
    def cluster(embeddings: list[np.ndarray], num_clusters: int):
        label_index_map = defaultdict(list[int])
        if num_clusters == 0:
            label_index_map['default'] = [idx for idx in range(len(embeddings))]
        else:
            kmeans = KMeans(n_clusters=num_clusters, random_state=0)
            labels = kmeans.fit_predict(embeddings)
            for i, label in enumerate(labels):
                label_index_map[label].append(i)
        return label_index_map
