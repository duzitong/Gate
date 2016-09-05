import time
from operator import add
from pyspark import SparkContext

def operate(a, b, gate_type):
    if gate_type == 0:
        return a & b
    elif gate_type == 1:
        return ~a & b
    elif gate_type == 2:
        return a & ~b
    elif gate_type == 3:
        return a | b
    elif gate_type == 4:
        return a ^ b

def gate_output_generator(line):
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            for gate_type in range(5):
                yield operate(line[i], line[j], gate_type) 

def check(i, line):
    if i in line:
        return False
    if i == 0:
        return False
    return True

def str_gen(line):
    ret = ''
    for i in range(len(line)-1):
        ret += str(line[i]) + ','
    ret += str(line[-1])
    return ret

def operate_line(linestr):
    ret = []
    line = [int(num) for num in linestr.split(',')]
    output = set(gate_output_generator(line))
    for i in output:
        if check(i, line):
            ret.append(str_gen(sorted(line + [i])))
    return ret

sc = SparkContext("spark://172.16.7.12:7077", "Gate")
a = ["255,3855,13107,21845"]
start = time.time()
rdd = sc.parallelize(a)
for i in range(6):
    rdd = rdd.flatMap(operate_line).distinct()
print('saving file')
rdd.saveAsTextFile("hdfs://172.16.7.12:9000/duzitong/6")
end = time.time()
print('Done: ' + str(end-start) + 'seconds used.')
