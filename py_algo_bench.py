import random as rd
import time
import itertools

def algorithm(config):
    """
    This function should yield values as follows:
    (iteration number, best element, best score, best updated?)
    """
    pass


def iterate(val):
    if hasattr(val, "__iter__"):
        return val
    else:
        return [val]

class RunConfig:
    def __init__(self,
                 conf_name,
                 algorithm_config,
                 algorithm_function,
                 stop_predicate,
                 number_of_runs,
                 max_iter,
                 authors=["None"]):
                     
        if not hasattr(algorithm_function, "__call__"):
            raise ValueError("algorithm_function has to be callable")
        
        if not hasattr(stop_predicate, "__call__"):
            raise ValueError("stop_predicate has to be callable")
        
        if number_of_runs is None:
            raise ValueError("number_of_runs cannot be None (set it to 1)")
        
        if max_iter is None:
            raise ValueError("max_iter cannot be None")
        
        self.conf_name = "no name" if conf_name is None else conf_name
        self.algorithm_config = algorithm_config
        self.algorithm_function = algorithm_function
        self.stop_predicate = stop_predicate
        self.number_of_runs = number_of_runs
        self.max_iter = max_iter
        self.authors = authors




def test_single_config(runConfig):
    """
    This algorithm returns all the best scores in order with iteration
    number
    """
    finalConfig = {}
    finalConfig.update(runConfig.algorithm_config)
    finalConfig.update({"predicate": runConfig.algorithm_function})
    finalConfig.update({"stop_predicate": runConfig.stop_predicate})
    finalConfig.update({"runNumber": range(1,runConfig.number_of_runs+1)})
    finalConfig.update({"max_iter": runConfig.max_iter})
    finalConfig.update({"config_start_timestamp": time.time()})
    finalConfig.update({"authors": [runConfig.authors]})
    
    print(finalConfig)
    
    for element in itertools.product(
            *map(lambda t: [(t[0], x) for x in iterate(t[1])], finalConfig.items())):
        print(element)
    

def pseudo_func(x):
    return x

testConf = RunConfig("test config",
    {"firstParam": range(2),
     "secondParam": ["ok", "not ok"]},
    pseudo_func,
    pseudo_func,
    1,
    1)

test_single_config(testConf)












