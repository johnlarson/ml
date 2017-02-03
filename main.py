#! /home/john/.virtualenvs/ml/bin/python3.4

from toolkitPython.manager import MLSystemManager

from ml.baseline import BaselineLearner
from ml.perceptron import PerceptronLearner

LEARNERS = {
    'baseline': BaselineLearner(),
    'perceptron': PerceptronLearner(),
}

class MyMLSystemManager(MLSystemManager):

    def get_learner(self, learner):
        if learner in LEARNERS:
            return LEARNERS[learner]
        else:
            raise Exception('Unrecognized learner: {}'.format(learner))

try:
    MyMLSystemManager().main()
except Exception as e:
    raise Exception;