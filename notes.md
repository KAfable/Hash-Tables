# Hashtables and Blockchain Week

## Arrays

### Memory structure of an array

- array is a sequence of elements of the same type stored in a continguous block of memory
- it is important it is a continguous block of memory because it helps with pointers
- How do you declare an array? eg, [2,3,4,5]

  1. Determine how big the array needs to be:
     - an integer is 4bytes, so 16 bytes total
     - there are 8 bits in a byte
  2. Request a block of memory from the operating system
  3. Receive the memory address of the reserved block
  4. Write your values into the array

- access an element in the array it is : `index * sizeof(type) + start_address`

  - this happens quickly because it is just multiplying/adding: O(1)

### Adding an element to end of array

    1. Take size of current array and increase by one element
    2. Request a NEW block of memory with updated size
    3. Copy each element from old space into new space one at a time
    4. Stick the new element into the end
    5. Free memory from the old array

- according to Brady on this [video](https://www.youtube.com/watch?v=e8tSdmh_u_0) adding to end of an array is O(n) operation

- according to python wiki on time complexity - insertion into end of a **list** is `O(1)` / constant
- what does the python list structure due to decrease the time?
  - python is a little bit smarter, it will allocate a few empty spaces each time the array grows
  - everytime the arrow grows, it will allocate a bit more space than it previously did (adding variable amount each time)
  - reallocating space happens more and more infrequently the more frequently you add to an array
  - as a result it is usually O(1) but sometimes O(n), on average though it is considered to be O(1)

### Adding an element to start of array

- insertion into middle of an array is `O(k)` but wtf is k?

## Blockchain
