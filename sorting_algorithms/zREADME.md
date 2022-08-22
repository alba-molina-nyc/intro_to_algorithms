# Sorting Algorithms

1. bubble
2. insertion
3. selection

pseudo code

## Bubble

```python
[3, 44, 38, 5, 47, 15, 36, 26]

set the swapped flag to false
then iterate from index 1 to 5 inclusive

do 
    swapped = false
    for i = 1 to indexOfLastUnsortedElement - 1
        if leftElement > rightElement
            swap(leftElement, rightElement)
            swapped = True
            """

```

## Insertion

```python
Extract the first unsorted element(47)
mark first element as sorted
for each unsorted element X
    'extract'the element X
    for j = lastSortedIndex down to 0
        if current element j < X
            move sorted element to the right by 1
        break loop and isert X here
```


## Selection

```python
[3, 44, 38, 5, 47, 15, 36, 26]

repeat(numOfElements - 1) times
    set the first unsorted element as the minimum
    for each of the unsorted elements
        if element < currentMinimum
            set element as new minimum
    swap minimum with first unsorted position
```