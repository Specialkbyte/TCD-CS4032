Lab 4: Chat Server
==========

Building on the mutlithreaded socket server from lab 2, the goal of this lab is to build a chat room that clients can join, post messages to and retrieve messages from. My chat room is implemented using TCP, ignores any kind of failure recovery or latecommers to a chat room being able to see past messages.

## Development
To run the code in development mode may require some of the packages in the `dev-requirements.txt` file. To install them run the following `pip` command:

`pip install -r dev-requirements.txt`

### Tests
Python's `nosetests` is used to run the test suite, it is installed using the instructions above. Once installed run the following command in the `lab2` directory.

`nosetests`

You need to have the server running in at the same time on port `8080`. I couldnt' quite find a nice way of spinning up the server for each unit test.