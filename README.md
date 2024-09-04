# Weather Data Analysis with Big Data Technologies

## Overview
This project involves processing and analyzing large-scale weather data from the National Climatic Data Center (NCDC). It utilizes various big data technologies to extract insights on wind direction, sky ceiling height, and visibility across multiple weather stations. The project showcases the use of Hadoop ecosystem tools and other big data technologies to efficiently process and analyze vast amounts of weather data.

## Features
- Large-scale data processing of NCDC weather records using Hadoop and Spark
- Custom MapReduce jobs for data analysis of wind direction paterns, computation of average sky ceiling height and determination of visibility distance trends.
- Hive and Pig for querying and data transformation
- PySpark for distributed data processing

## Technologies Used
- **Big Data Tools**: Hadoop (HDFS, MapReduce), Apache Spark, Hive, Pig
- **Programming Languages**: Python
- **Libraries**: PySpark, MRJob, Pandas
- **Environment**: Linux command-line tools

## Usage
- Load the weather data into HDFS.
- Run the MapReduce jobs or Spark scripts to perform data analysis.
- Query the processed data using Hive or Pig to extract insights.

## Key Findings
- Wind direction patterns show seasonal variations: Wind direction tends to shift eastward during winter months, influenced by cold fronts and coastal winds. This pattern is more pronounced in coastal regions and aligns with the typical seasonal wind patterns observed in meteorological studies.
- Average sky ceiling height varies significantly across geagraphic locations: The range of sky ceiling height is greater in mountainous regions, where lower cloud cover is more frequent, compared to plains and coastal areas, which typically experience higher sky ceiling heights due to clearer skies.
- Visibility distance trends indicate a correlation with weather conditions and geographical features: Visibility is often reduced in areas with frequent fog or heavy precipitation, such as coastal and mountainous regions, especially during the winter months. In contrast, visibility improves significantly in dry conditions during the summer or in arid regions.

- ## Challenges Overcome
- Handling the massive scale of NCDC data efficiently
- Optimizing MapReduce jobs for better performance
- Integrating multiple big data technologies seamlessly

## Future Improvements
- Implement real-time data processing using Apache Kafka and Storm
- Develop a web interface for interactive data exploration
- Extend the analysis to include temperature and precipitation patterns
- Integrate machine learning models for weather prediction

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
