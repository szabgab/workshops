# Regular expressions for fun and profit

Regular expressions are a mysterious subject for many people.
Even to some hard-core engineers.
During this workshop you'll learn the basics. Just enough to be dangerously productive with it.

The main tasks that you normally do with Regexes is pattern matching.

e.g. You have a file with entries like this:

```
07:00 Get up
07:20 Have breakfast

# Some Comment
```

* How do you extrad the timestamps from and the description of each even avoiding the comments and the seemingly empty rows?

In another case you might have a file with many lines like these:

```
Jul 6 17:35:10 sdc-prius motion_planner[1284]: new destination: [55.733510, 37.587401]
Jul 6 17:35:11 sdc-prius control[1284]: next waypoint: [55.733668, 37.587143]
Jul 6 17:35:11 sdc-prius control[1281]: steering: 212, throttle: 420
```

* How do you extract the coordinates and the dates of the waypoints from this?


What if you have a line like this:

```
My phone number is 12345 and my age is: 23
```

* How do you extract the phone number out of this?
* How do you extract the age?

