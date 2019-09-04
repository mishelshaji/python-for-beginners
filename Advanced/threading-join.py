import threading
import time

def square(num):
	time.sleep(10)
	print("Square: {}".format(num ** 2))

def cube(num):
	time.sleep(5)
	print("Cube: {}".format(num ** 3))

#if __name__ == "__main__":
	# creating thread
t1 = threading.Thread(target=square, args=(2,))
t2 = threading.Thread(target=cube, args=(2,))

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

# both threads completely executed
print("Done!")
