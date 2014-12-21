CS4032: Distributed Systems Labs
=============

## Lab 1: Echo server client pair.
The echo server is written in PHP and my matching echo client is in Python. The echo client partially implements HTTP standards, well kinda.

## Lab 2: Multithreaded socket server
A multithreaded server with a simple thread pool. The main thread accepts connections off a socket and if the connection queue isn't full the connection is added to the queue for one of the worker threads to process. There is a limited number of worker threads as well to prevent resource wastage.

## Lab 4: Chat room
Building on the mutlithreaded socket server from lab 2, the goal of this lab is to build a chat room that clients can join, post messages to and retrieve messages from. My chat room is implemented using TCP, ignores any kind of failure recovery or latecommers to a chat room being able to see past messages.

## Project: Distributed File System