from plot_generator import generate_sort_algorithm_plot
from InsertionSort import InsertionSort
from HeapSort import HeapSort
from merge_sort import merge_sort
from QuickSort import QuickSort

def main():
    #generate_sort_algorithm_plot(HeapSort, "O(N log N)")
    #generate_sort_algorithm_plot(InsertionSort, "O(N^2)")
    #generate_sort_algorithm_plot(merge_sort, "O(N log N)")
    generate_sort_algorithm_plot(QuickSort, "O(N log N)")
if __name__ == "__main__":
    main()