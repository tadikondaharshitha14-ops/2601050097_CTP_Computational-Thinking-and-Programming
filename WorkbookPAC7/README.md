**Producer-Consumer Application**

**1. Objective**

To develop a simple Producer-Consumer application using threading, multiprocessing, and synchronization primitives.

**2. Input**

**The program accepts:**

Number of items to produce

Items produced by the producer

Size of the shared buffer

**3. Output**

**The program displays:**

Items produced by the Producer

Items consumed by the Consumer

Producer and Consumer execution

Synchronization between Producer and Consumer

Completion message

**4. Algorithm**

Start.

Create a shared buffer.

Create Producer and Consumer.

Use threading or multiprocessing.

Use synchronization primitives to control the buffer.

Producer adds items and Consumer removes items.

Repeat until all items are processed.

Display the results.

Stop.

**5. Time and Space Complexity**

**Time Complexity**

O(n)

Where n is the number of items produced and consumed.

**Space Complexity**

O(n)

The shared buffer stores the items waiting to be consumed.
