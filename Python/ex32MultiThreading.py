import threading
import time

def downloading_file(filename, duration):
    print(f"Starting download for {filename}...")
    for i in range(1, duration+1):
        print('Downloading File....')
        time.sleep(1)
    print(f"Finished downloading {filename}")

def process_data(data, duration):
    print(f"Starting to process {data}")
    for i in range(1, duration+1):
        print('Downloading File....')
        time.sleep(1)
    print(f"Finished processing {data}")

# #create threads:
thread1 = threading.Thread(target=downloading_file, args=('file1.zip', 5))
thread2 = threading.Thread(target=process_data, args=('data1', 10))
#
# print("Main program is running now............")
# #start the threads where they shall execute parellelly
# # thread1.start()
# # thread2.start()
#
# print("Main Program is continuing to do the job")
# # Allow the main program to wait till all the threads are completed.
# thread1.join()
# thread2.join()
#
# print("All the threads are done with the job")




#########################Using locks##########################################
# Shared resource:
counter  = 0
# Lock for the resource
lock = threading.Lock()

def increment_counter(arg):
    lock.acquire()
    global counter
    for _ in range(10):
        time.sleep(1)
        counter += 1
        print(f"counter: {counter} from thread {arg}")
    lock.release()

t1 = threading.Thread(target=increment_counter, args=("1"))
t2 = threading.Thread(target=increment_counter, args=("2"))

t1.start()
t2.start()

t1.join()
t2.join()
print(f"Final counter value: {counter}" )