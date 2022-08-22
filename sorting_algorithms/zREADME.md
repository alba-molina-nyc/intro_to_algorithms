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
[3, 44, 38, 5, 47, 15, 36, 26]

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

### Practice Quiz

[practice quiz](/sorting_algorithms/assignment/assignment.py)

Introduction to Algorithms
Practice Quiz (Introduction)
Total Points: 100

1. Write a pseudocode for the following sorting algorithm that sorts n numbers in descending order.
Consider that the input numbers are given in the form of an array A. You make multiple passes
through the array in the following way. In the first pass you find the largest element in the array
and place at position 1. In the second pass, you find the second largest element in the array and
place it at position 2. In this way in the ith pass you find the ith largest element in the array and
place it at position i. After n passes through the array, it should be sorted. (25 points)

```python
A = [] #Consider that the input numbers are given in the form of an array A

```

2. A and B are two sorted arrays (ascending order) of size n. You are provided another array C of
size n. Write the pseudocode for finding the n smallest numbers in A and B and inserting it into a
single sorted array C. (25 points)

```python
```

3. Sort the following numbers in ascending order using selection sort 5, 7, 3, 8, 2, 9, 10, 12. (25
points)

```python
```

4. Sort the following numbers in ascending order using bubble sort 5, 7, 3, 8, 2, 9, 10, 12. (25
points)

```python
```
