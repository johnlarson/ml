from toolkitPython.supervised_learner import SupervisedLearner
from toolkitPython.matrix import Matrix


class BaselineLearner(SupervisedLearner):
    """
    For nominal labels, this model simply returns the majority class. For
    continuous labels, it returns the mean value.
    If the learning model you're using doesn't do as well as this one,
    it's time to find a new learning model.
    """

    labels = []

    def __init__(self):
        pass

    def train(self, features, labels):
        """
        :type features: Matrix
        :type labels: Matrix
        Here you make some changes to the learner internally so that it
        will give the best answers for predicting. You will also use the
        `predict` function in here for each column
        """
        self.labels = []
        for i in range(labels.cols):
            if labels.value_count(i) == 0:
                self.labels += [labels.column_mean(i)]          # continuous
            else:
                self.labels += [labels.most_common_value(i)]    # nominal

    def predict(self, features, labels):
        """
        :type features: [float]
        :type labels: [float]
        Fill `class.labels` with the answers for the given input
        `features`
        """
        del labels[:]
        labels += self.labels



