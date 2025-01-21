import matplotlib.pyplot as plt

def visualize_results(results):
    plt.bar(['Performance Score'], [results['performance_score']])
    plt.title('Athlete Performance')
    plt.ylabel('Score')
    plt.show()
