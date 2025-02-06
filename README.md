# Piemon

Piemon is a tool that helps develop Python applications which contain a continuous event loop. 
It automatically restarts the event loop whenever a change in the main file is detected. 

## Getting started 

```
pip install . 
```

The only dependency this project requires is Watchdog version v3.0.0 and above.

To use it with your main file just do 

```
piemon [filename].py [args] 
```
