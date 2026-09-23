import time
import tracemalloc

N = 1_000_000


# List processing
def list_processing():
    return [x * 2 for x in range(N)]


# Generator processing
def generator_processing():
    return (x * 2 for x in range(N))


# Test List
tracemalloc.start()

start = time.time()
data = list_processing()
list_time = time.time() - start

current, list_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()


# Test Generator
tracemalloc.start()

start = time.time()
data = generator_processing()

# Process generator
for x in data:
    pass

generator_time = time.time() - start

current, generator_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()


print("List Time:", list_time)
print("List Memory:", list_memory / 1024 / 1024, "MB")

print("Generator Time:", generator_time)
print("Generator Memory:", generator_memory / 1024 / 1024, "MB")