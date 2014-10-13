CS4032: Distributed Systems Labs
=============

## Lab 1
A simple echo server/client pair. The echo server is written in PHP and my matching echo client is in Python. The echo client partially implements HTTP standards, well kinda.

## Lab 2
A multithreaded server with a simple thread pool. The main thread accepts connections off a socket and if the connection queue isn't full the connection is added to the queue for one of the worker threads to process. There is a limited number of worker threads as well to prevent resource wastage.