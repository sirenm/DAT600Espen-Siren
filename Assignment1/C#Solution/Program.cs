using System;
using System.Diagnostics;
using Sortingalgorithms;

List<int> sizes_of_lists = new List<int>{5, 10, 15, 20, 25, 30, 35, 40, 45, 50};
Console.WriteLine("Execution Time for Insertion Sort: ");
foreach (var size in sizes_of_lists)
{
    var stopwatch = new Stopwatch();
    List<int> list_to_be_sorted = Enumerable.Range(0, size).Select(_ => new Random().Next(0, 1000)).ToList();
    var algorithms = new SortingAlgorithms(list_to_be_sorted);
    stopwatch.Start();
    algorithms.InsertionSort();
    stopwatch.Stop();
    var elapsedtime = stopwatch.Elapsed.TotalSeconds;
    Console.WriteLine($"Execution Time for list of size {size}: " + elapsedtime);
}

Console.WriteLine();

Console.WriteLine("Execution Time for Heap Sort: ");
foreach (var size in sizes_of_lists)
{
    var stopwatch = new Stopwatch();
    List<int> list_to_be_sorted = Enumerable.Range(0, size).Select(_ => new Random().Next(0, 1000)).ToList();
    var algorithms = new SortingAlgorithms(list_to_be_sorted);
    stopwatch.Start();
    algorithms.HeapSort();
    stopwatch.Stop();
    var elapsedtime = stopwatch.Elapsed.TotalSeconds;
    Console.WriteLine($"Execution Time for list of size {size}: " + elapsedtime);
}