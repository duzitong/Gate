from pyspark import SparkContext
sc = SparkContext("spark://172.16.7.12:7077", "Statistic")
text = sc.textFile("hdfs://172.16.7.12:9000/duzitong/6/")
text.flatMap(lambda line: [int(i) for i in line.split(',')]).distinct().saveAsTextFile("hdfs://172.16.7.12:9000/duzitong/6s")
print('Finished')
