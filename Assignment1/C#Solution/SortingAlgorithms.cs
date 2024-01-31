namespace Sortingalgorithms {
    public class SortingAlgorithms
    {
        public List<int> _A {get; set;}
        public SortingAlgorithms(List<int> A)
        {
            _A = A;
        }

        public List<int> InsertionSort(){
            for (int i = 1; i < _A.Count; i++)
            {
                var key = _A[i];
                var j = i-1;
                while (j>-1 && _A[j] > key){
                    _A[j+1] = _A[j];
                    j -= 1;
                }
                _A[j+1] = key;
            }
            return _A;
        }

        public List<int> HeapSort(){
            BuildMaxHeap();
            int heapsize = _A.Count;
            for (int i = heapsize; i >= 1; i-- ){
                int temporary = _A[i-1];
                _A[i-1] = _A[0];
                _A[0] = temporary;
                heapsize -= 1;
                MaxHeapify(1, heapsize);
            }
            return _A;
        }

        public void BuildMaxHeap(){
            int heapsize = _A.Count;
            for (int i = heapsize / 2; i > 0; i--){
                MaxHeapify(i, heapsize);
            }
        }

        public void MaxHeapify(int i, int heapsize){
            int l = Left(i);
            int r = Right(i);
            int largest;
            if (l <= heapsize && _A[l-1] > _A[i-1]){
                largest = l;
            }
            else {
                largest = i;
            }
            if (r <= heapsize && _A[r-1] > _A[largest-1]){
                largest = r;
            }
            if (largest != i){
                int temporary = _A[i-1];
                 _A[i-1] = _A[largest-1];
                 _A[largest-1] = temporary;
                 MaxHeapify(largest, heapsize);
            }
        }

        public int Left(int i){
            return i*2;
        }

        public int Right(int i){
            return (2*i)+1;
        }
    }
}