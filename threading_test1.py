import threading
import time
from queue import Queue

def thread_job():
	print "This is an added Thread, number is %s" % threading.current_thread()
	for i in range(10):
		time.sleep(0.1)
	print "T1 finish\n"


def T2_job():
	print "T2 start\n"
	print "T2 finish\n"

def square_job(l, q):
	for i in range(len(l)):
		l[i] = l[i]**2
	q.put(l)

def multi_threading():
	q = Queue()
	threads = []
	data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]

	for i in range(4):
		t = threading.Thread(target = square_job, args=(data[i], q))
		t.start()
		threads.append(t)

	for thread in threads:
		thread.join()

	results = [] 

	for _ in range(4):
		results.append(q.get()) # get one value in order

	print results


def main():
	multi_threading()
	'''
	added_thread = threading.Thread(target = thread_job, name = "T1")
	added_thread.start()
	
	thread2 = threading.Thread(target = T2_job, name= "T2")
	thread2.start()
	added_thread.join()
	thread2.join()
	'''
	print "all done\n"
	print threading.active_count()
	# print threading.enumerate()
	# print threading.current_thread()

if __name__ == '__main__':
	main()