#Pulz backend
We developed a simple app, which is able to measure a person's Photoplethysmogram (PPG) by pressing his finger on a camera. The user can see the actual heart rate and the measured data are sent to a simple web server we developed for post-processing. The post-processing is based on the [HeartPy library](https://python-heart-rate-analysis-toolkit.readthedocs.io/en/latest/index.html). The library focuses on analysis of PPG from noisy data.

*server.py* - a simple web server using flask accepting the data as input and outputting a results of the analysis as well as a tagged graph.

*post.py* - testing POST request with measured data

plot.png - example tagged data

This code is running on [Intersystems server](http://52773-1-5b2c2b30.labs.learning.intersystems.com). However, there is still some work to be done before it can communicate with our app.
