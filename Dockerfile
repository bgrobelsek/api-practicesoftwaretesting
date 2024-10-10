# Python image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Install curl to install poetry
RUN apt-get update && apt-get install -y curl

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy project files into the container
COPY . .

# Install project dependencies using Poetry (without dev dependencies)
RUN poetry config virtualenvs.create false && poetry install

# Command to run pytest using Poetry and generate the test report
CMD ["poetry", "run", "pytest"]
