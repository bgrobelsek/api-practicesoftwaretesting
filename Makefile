DOCKER_COMPOSE = docker-compose

# Targets
.PHONY: up down clean

# Builds the project and runs the tests
up:
	$(DOCKER_COMPOSE) up --build

# Rerun the tests once the project is built
run:
	$(DOCKER_COMPOSE) up

# Removes all the cache files and the report (works only for Linux and macOS)
clean:
	find . -name ".pytest_cache" -exec rm -rf {} +
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.html" -path "./reports/*" -exec rm -f {} +

# Stops and removes the containers
down:
	$(DOCKER_COMPOSE) down


