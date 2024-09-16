# Maya Python Dev Tempate

## Purpose

this is is a template project that is designed for:
* Have Maya Python Code Completion
* Can Send Code To Maya

## How to configure Maya:
* open Maya Script Editor, and in the Mel tab, type in:
```
commandPort -n "localhost:7001" -stp "python"
```
Press ```Alt + Enter``` to run it.
this will tell Maya to listen for command from localhost(your machine) on port 7001
If doing remotely, need to change the command to:
```
commandPort -n "0.0.0.0:7001" -stp "python"
```
and alter the ```SendToMaya.py``` to connect to the host ip on line 11:
```
host = "Maya Computer LAN IP"
```

## How to Send Code to Maya:
use the script:
SendToMaya.py:
```
python SendToMaya.py yourScript.py
```

example:
```
python ./Src/SendToMaya.py ./Src/HelloWorld.py
```


