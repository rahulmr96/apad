import time

def csv_reader_with_generator(fileval):
    read_csv=[]
    for i in fileval:
        read_csv.append(i)
    yield read_csv

def csv_normal(file):
    read_new=[]
    for i in file:
        read_new.append(i)
    return read_new        

file=open("LargeCSVFile.csv","r")
csv_gen = csv_reader_with_generator(file)
row_count = 0
start_time=time.perf_counter_ns()
for row in csv_gen:
    row_count += 1
total_time=time.perf_counter_ns()-start_time
print(f"Row count is {row_count}")
print(total_time/1e9)

file=open("LargeCSVFile.csv","r")
csv_gen = csv_normal(file)
row_count = 0
start_time=time.perf_counter_ns()
for row in csv_gen:
    row_count += 1
total_time=time.perf_counter_ns()-start_time
print(f"Row count is {row_count}")
print(total_time/1e9)


file.close()