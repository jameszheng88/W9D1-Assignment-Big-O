# W9D1-Assignment-Big-O

## Algorithm 1: Linear Search

The time complexity of the linear search algorithm is O(n). As the size of the array increases, the time to complete the search proportionally increases.

One possible way to improve the linear search is to use transposition. If the key is found in the array, the element is moved 1 index prior during each search until it is moved to the front. This is assuming that key is more frequently searched than others, and the drawback would be it would still take longer time to find other elements. The improvement in this case would be very slight.

Another possible improvement is to use hash tables to map the element to its position to the list. This way, the position of an element can be looked up by its value in the hash table and would result in O(1). Drawback of this approach is that it would make the code less concise. It would still take O(n) time to build the hash table, but subsequent searches and any multiple searches would result in faster time. This makes sense for databases that would be searched over and over again.

In our example, because the test cases is based on the same array, using a hash table makes sense as once the hash table is generated, it is used again.

## Algorithm 2: Bubble Sort

The time complexity of the Bubble Sort algorithm is O(n^2). As the array is traversed, it sorts the largest value to the last index, and this process is repeated until all the elements are in order. In the best case scenario, it will require at least 1 iteration through the array (O(n)), if all the elements in the array are sorted. For average cases, it requires more than 1 iteration through the array.

One possible way to improve Bubble Sort is to implement a flag variable. It will be set to False and changed to True if a swap occurs. This way, if no swapping occurs, then the array is sorted and there is no need to continue iterating through the array.

In our test cases, both arrays already has the largest integer as the last element. With the flag variable, it saves at least 1 iteration through the array.
