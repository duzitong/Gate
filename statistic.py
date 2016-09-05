from pyspark import SparkContext
sc = SparkContext("spark://172.16.7.12:7077", "Statistic")
text = sc.textFile("hdfs://172.16.7.12:9000/duzitong/6/")
text.filter(lambda line: ('7827' in line) or ('13029' in line) or ('22950' in line) or ('25743' in line)).saveAsTextFile("hdfs://172.16.7.12:9000/duzitong/6sp")
print('Finished')
