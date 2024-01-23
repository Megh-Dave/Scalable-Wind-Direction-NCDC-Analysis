import sys
from pyspark import SparkContext

def main():
    sc = SparkContext(appName='RangeofSkyCeilingHeight')

    input_rdd = sc.textFile('/home/6student6/Project/ProjectData/')

    filtered_rdd = input_rdd.filter(lambda line: line[70:75] != "99999" and int(line[75:76]) in [0, 1, 4, 5, 9])

    station_height_rdd = filtered_rdd.map(lambda line: (line[4:10], int(line[70:75])))

    range_rdd = station_height_rdd.reduceByKey(lambda height1, height2: max(height1, height2) - min(height1, height2))

    range_rdd.saveAsTextFile('/home/6student6/Project/outputpyspark_SkyCeilingRange/')

    sc.stop()

if __name__ == '__main__':
    main()