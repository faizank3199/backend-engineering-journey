# Log File Reader Using Python Generators

## Overview

This project demonstrates how Python generators can be used to process large log files efficiently without loading the entire file into memory.

## Features

* Read logs lazily using generators
* Filter ERROR logs
* Filter WARNING logs
* Count total ERROR entries
* Memory-efficient processing

## Concepts Used

* Generators
* yield
* File Handling
* Lazy Evaluation
* Generator Pipelines

## Example Output

=== ERROR LOGS ===

[25-05-31 10:00:00] ERROR Database connection failed

[25-05-31 10:00:01] ERROR Invalid password

[25-05-31 10:00:02] ERROR API timeout

=== COUNT ERRORS ===

Total ERRORS: 3

## Author

Mohammad Faizan
