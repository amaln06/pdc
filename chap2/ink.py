import threading

# Shared variable
counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1

# Two threads that increment the same variable
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)  # Expected output is 2000000, but due to race condition, the output will likely be less
