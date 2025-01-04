1. Barrier.py
Purpose: Demonstrates the use of a Barrier to synchronize threads in a multi-threaded program.
How It Works:
Three runners are simulated using threads.
Each runner thread sleeps for a random time (to simulate running) and then waits at a barrier.
The barrier ensures that all threads reach a certain point (the "finish line") before continuing.
Once all threads reach the barrier, the race is declared over.
Key Feature: Synchronization of threads using threading.Barrier to simulate a race where all participants must finish together​
.
2. Condition.py
Purpose: Implements a producer-consumer problem using threading.Condition to synchronize access to a shared resource.
How It Works:
A Producer thread generates items and adds them to a shared list (items).
A Consumer thread removes items from the list.
The Condition object is used to coordinate the producer and consumer, ensuring the producer waits if the list is full and the consumer waits if the list is empty.
Key Feature: Demonstrates thread synchronization using conditions to avoid race conditions and resource contention​
.
3. ink.py
Purpose: Highlights a race condition when multiple threads modify a shared variable concurrently without proper synchronization.
How It Works:
Two threads increment a shared counter variable 1,000,000 times each.
Due to the lack of synchronization, the final value of the counter is often incorrect because threads interfere with each other’s updates.
Key Feature: Demonstrates the concept of race conditions and the need for synchronization mechanisms like locks in multi-threaded programs​
.
4. Threading with Lock for Synchronization
Purpose: Demonstrates the use of threading with a lock to ensure synchronized access to shared resources.
Key Features:
A threadLock is used to ensure that only one thread at a time can execute the critical section (printing process ID).
Each thread sleeps for a random duration (1–10 seconds) and then releases the lock.
The lock prevents threads from interfering with each other while accessing shared resources or printing.
Outcome: Threads run sequentially within the critical section, avoiding conflicts.

5. Threading with Lock (Alternate Order)
Purpose: Similar to Code 1 but with slight changes in the order of lock acquisition and release.
Key Features:
Threads acquire the lock, execute their critical section, and release the lock after completing the task.
This ensures that threads do not overlap in the critical section.
The structure is slightly modified to release the lock after the sleep duration.
Outcome: Threads maintain synchronization, but the critical section remains locked longer due to the sleep duration.

6. Threading Without Lock
Purpose: Demonstrates threading without synchronization, allowing threads to execute independently.
Key Features:
Threads execute concurrently without acquiring a lock.
Each thread prints its details and sleeps for a random duration (1–10 seconds).
There is no restriction on the sequence of thread execution.
Outcome: Threads run in parallel without any synchronization, which may lead to overlapping outputs in the console