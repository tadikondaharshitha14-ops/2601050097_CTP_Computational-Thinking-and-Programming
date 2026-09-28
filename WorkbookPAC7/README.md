# Producer-Consumer Application

**1. Objective**

To develop a simple Producer-Consumer application using threading, multiprocessing, and synchronization primitives.

**2. Input**

**The program accepts:**

1. Number of items to produce
2. Items produced by the producer
4. Size of the shared buffer

**3. Output**

**The program displays:**

1. Items produced by the Producer
2. Items consumed by the Consumer
3. Producer and Consumer execution
4. Synchronization between Producer and Consumer
5. Completion message

**4. Algorithm**

1. Start.
2. Create a shared buffer.
3. Create Producer and Consumer.
4. Use threading or multiprocessing.
5. Use synchronization primitives to control the buffer.
6. Producer adds items and Consumer removes items.
7. Repeat until all items are processed.
8. Display the results.
9. Stop.

**5. Time and Space Complexity**

**Time Complexity**

O(n)

Where `n` is the number of items produced and consumed.

**Space Complexity**

O(n)

The shared buffer stores the items waiting to be consumed.


