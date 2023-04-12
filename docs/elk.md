# ELK - Elasticsearch - Logstash - Kibana stack


* Write documents from Python.
* Write documents from Shell.
* Search for documents.
* Write some time series using Python.
* Use Logstash to collect data from log files and write it in Elasticsearch.
* Use Kibana to look at that data.


Separation by users in visualize so one person can experiment without the fear of changing something to the others.

* Don't save
* Copy the Exisiting Visualizations and experiment on the copy  (In Management export  Virtualization, edit the file , change the name, remove the id field.  Import the virtualization)


* Time series
  Host: some-host-name
  Alive: 1 Sum the numbers in the last X min and display the count  (eg. Up till 5)
  Make it green if it is in the top range (e.g. 5, yellow if it is in the middle (2-4), red if it is 0-1

