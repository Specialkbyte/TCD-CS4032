Lab 2: Multithreaded Socket Server
==========

A multithreaded server with a simple thread pool. The main thread accepts connections off a socket and if the connection queue isn't full the connection is added to the queue for one of the worker threads to process. There is a limited number of worker threads as well to prevent resource wastage.

### Connection Queue
The connection queue is implemented using Python's `Queue` package, which provides a thread-safe queue implementation. 

## Development
To run the code in development mode may require some of the packages in the `dev-requirements.txt` file. To install them run the following `pip` command:

`pip install -r dev-requirements.txt`

### Tests
Python's `nosetests` is used to run the test suite, it is installed using the instructions above. Once installed run the following command in the `lab2` directory.

`nosetests`
