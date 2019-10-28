# Introduction
The following summarizes the analysis for each of the task assigned.

## Problem 1 (Square Root)
### Approach
- Use BST approach to quickly converge on the solution.

### Efficiency
- The time complexity is O(log(n)), since we're using BST approach.
- The space complexity of O(1), since we're only keeping track of 1 variable throughout the loop.

## Problem 2 (Search in Array)
### Approach
I'm still using BST approach in handling this problem. However there's slight adjustment being made to address the rotated array, where some if-else statement was used to determine which half of the array should be drilled down further.

### Efficiency
- O(log(n)) for time complexity since we're adopting binary search approach.
- O(1) for space complexity since we're recursively searching the same space.

## Problem 3 (Rearrange digits)
### Approach
The array is first sorted in ascending order using quicksort. Quicksort is implemented using existing course material. To calculate the sum, the numbers are processed iteratively.

## Efficiency
- O(n log(n)) for Quicksort algorithm, assuming that worst case is ignored. While determining the final value will incur an additional O(n), it's quite negligible when compared to the quicksort complexity. As such, the final complexity is O(n log(n)).
- The space complexity for this is O(n), since we're just rearranging the array space.

## Problem 4 (Dutch National Flag)
### Approach
I maintained a few variables to keep track of the index for value '0' and '2' is at each traversal. By swapping the value of 0 and 2 to the start and end of the array, the value 1 sorts itself out to be in the middle.

## Efficiency
- The space complexity is O(1), as we only maintain the few variables/pointers needed to swap the array order.
- The time complexity is O(n), as we'll need to traverse the entire array.

## Problem 5 (Autocomplete with Tries)
### Approach
The notebook does a trie implementation covering much of what was taught in the previous lessons. A dict is used to keep the node's children and their follow-up character to other nodes. Completed word are flagged with `is_word`.

### Efficiency
- On find(), the time complexity is O(n), as we need to evaluate each char. There is no space complexity (ie O(1)) as nothing is stored.
- On insert(), the time complexity is O(n), as each char is evaluated and stored. Space complexity is thus O(n) as well.
- On suffix(), the time complexity is O(n), as each char is evaluated. There is no space complexity (ie O(1)) as nothing is stored.

## Problem 6 (Min Max)
### Approach
Since we're just tasked with finding the min and max value given an unsorted array, we just need 2 placeholders and traverse through each element in the array.

### Efficiency
- On time complexity, it's O(n) since we evaluate each element.
- On space complexity, it's O(k) since we need 2 placeholders.

## Problem 7 (HTTP Handler)
### Approach
Similar to problem #5, this task is another type of trie implementation. Instead of having flags for word completion, we track the end of the nodes.
Splitting the path by '/' requires some additional work.

### Efficiency
- On find(), the time complexity is O(n), as we need to evaluate each elem. There is no space complexity (ie O(1)) as nothing is stored.
- On insert(), the time complexity is O(n), as each elem is evaluated and stored. Space complexity is thus O(n) as well.
- On lookup(), the complexity is similar to find().
