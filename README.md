# API testing

## Short Description
The idea of this repo is to test 3 endpoints on [practicesoftwaretesting](https://api.practicesoftwaretesting.com/api/documentation) 
through contract testing and then run an integration test for said endpoints. The integration test creates a brand,
validates it, updates the brand name and slug and then validates the update.

The whole process has been dockerized, once the docker container has been built all tests will be ran and the results will be
generated in the `/reports` folder.

What did 
* Created contract tests for the endpoints being used in this challenge
* Created an integration test that will run through said endpoints to create, validate and update existing brand
* Created `/utils` folder with helpers for brand creation (name and slug)
* Created a simple `conftest.py` for API handeling
* Utilizing [Poetry](https://python-poetry.org/) for dependency management
* Dockerizing the process to ensure a consistent testing environment


## Running the Tests
To run the tests, follow these steps:
1. Ensure you have [Docker](https://www.docker.com/) installed and running
2. Open your terminal and navigate to the project directory
3. Build and run the containers using the Makefile command:
   ```bash
   make up
    ```
4. Check the `/reports` folder for tests 

Additionally you can check the Makefile for other commands if needed: 
* `make run` - rerun the tests once the project is built 
* `make clean` - removes all the cache files and the report
* `make down` - stops and removes the containers
