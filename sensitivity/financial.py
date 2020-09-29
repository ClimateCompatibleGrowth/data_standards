import numpy as np
from SALib.test_functions import Ishigami

class Model():

    def __init__(self):

        pass

    def evaluate(self, parameter_values: np.ndarray) -> np.ndarray:
        """
        """

        results = Ishigami.evaluate(parameter_values)

        return results