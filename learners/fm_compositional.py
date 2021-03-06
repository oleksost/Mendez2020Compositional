import torch
import torch.nn as nn
import os
from itertools import zip_longest
from learners.base_learning_classes import CompositionalLearner

class CompositionalFM(CompositionalLearner):
    def __init__(self, net, results_dir='./tmp/results/'):
        super().__init__(net, results_dir)

    def update_modules(self, trainloader, task_id):
        # Just update structure instead
        for X, Y in trainloader:
            X = X.to(self.net.device, non_blocking=True)
            Y = Y.to(self.net.device, non_blocking=True)
            self.update_structure(X, Y, task_id)

    def update_multitask_cost(self, trainloader, task_id):
        pass