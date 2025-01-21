from data_collection import collect_data
from data_analysis import analyze_data
from visualization import visualize_results

def main():
    data = collect_data()
    if data:
        results = analyze_data(data)
        visualize_results(results)

if __name__ == "__main__":
    main()
