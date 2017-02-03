from toolkitPython.supervised_learner import SupervisedLearner
from toolkitPython.matrix import Matrix


class PerceptronLearner(SupervisedLearner):

    def __init__(self):
        # things I change
        self.weights = Matrix()
        self.threshold = 0

    def train(self, features, labels):
        """
        :type features: Matrix
        :type labels: Matrix
        """
        self.labels = []
        self._init_weights(features, labels)
        for i in range(labels.rows):
            f = features.row(i)
            t = labels.row(i)
            y = []
            self.predict(f, y)
            self._update_weights(y, t)

    def _init_weights(self, features, labels):
        height = features.cols + 1
        width = labels.cols
        self.weights.set_size(height, width)
        for row in range(height - 1):
            for col in range(width):
                self.weights.set(row, col, 0)
        for col in range(width):
            self.weights.set(height - 1, col, -1)

    def _update_weights(self, y, t):
        ...

    def predict(self, features, labels):
        """
        :type features: [float]
        :type labels: [float]
        """
        features.append(1)
        del labels[:]
        for col in range(self.weights.cols):
            amount = 0;
            for row in range(self.weights.rows):
                amount += features[row] * self.weights.get(row, col)
            labels.append(self.do_threshold(amount))

    def do_threshold(self, amount):
        return 1 if amount > self.threshold else 0



