# Python UDP example
UDP send/receive using coroutines

# Running:
```
/usr/bin/python36 async_udp_example.py
```

# Testing:
Install nmap-ncat. Open second console.

Run
```
nc -u -4 -l localhost 11234
```
to receive randomly generated number strings

Run
```
nc -u -4 localhost 11235
```
to start netcat as a client. Then type something and press &lt;enter&gt;.
The string should appear on the console where example is running
  
# Stopping:
Pressing &lt;ctrl&gt;+&lt;c&gt; should gracefully stop example execution. The same way you can terminate netcat.
