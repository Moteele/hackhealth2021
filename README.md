# hackhealth2021
Team Punk. solution for Challenge #1
To tackle the Challenge #1, we developed a simple app, which is able to measure a person's Photoplethysmogram (PPG) by pressing his finger on a camera. The user can see the actual heart rate and the measured data are sent to a simple web server we developed for post-processing. The post-processing is based on the [HeartPy library](https://python-heart-rate-analysis-toolkit.readthedocs.io/en/latest/index.html). The library focuses on analysis of PPG from noisy data.

*server.py* - a simple web server using flask accepting the data as input and outputting a results of the analysis as well as a tagged graph.

*post.py* - testing POST request with measured data

*mypulse* - flutter-based app, which means it's cross-platorm (Android, iPhone) with a simplistic GUI.

