import matplotlib

from src.Controller import Controller
from src.Repository import Repository
import matplotlib.pyplot as plt
if __name__ == '__main__':
    # repo = Repository("../data/2c.dat")
    repo = Repository("../data/3c.dat")

    ctrl = Controller(repo)

    total_accuracy = []
    total_runs = 1000
    total_sets = 0.15
    for run in range(total_runs):
        accuracy = ctrl.run(total_sets)
        total_accuracy.append(accuracy)
        print("Accuracy for run {0} = {1}".format(run, accuracy))

    print("Accuracy for {0} runs with {1} sets is: {2}".format(total_runs, total_sets, sum(total_accuracy)/total_runs))

    plt.plot(range(total_runs), total_accuracy)
    plt.show()
