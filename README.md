# Piemon

Piemon is a tool that helps develop Python applications which contain a continuous event loop. 
It automatically restarts the event loop whenever a change in the main file is detected. 

## Getting started 

Clone the repository on your machine
```
git clone https://github.com/shivanshsharma8834/piemon.git
cd piemon
```

Then install the package

```
pip install . 
```

The only dependency this project requires is Watchdog version v3.0.0 and above.

To use it with your main file just do 

```
piemon [filename].py [args] 
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.
License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
