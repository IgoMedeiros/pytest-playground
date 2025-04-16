# pytest-playground

A sandbox project for exploring and practicing testing in Python using `pytest`. This repository contains various modules and corresponding test cases to demonstrate different testing strategies, including mocking, database interactions, and service simulations.

## Features

- **API Testing**: Validate API endpoints and their responses.
- **Class-Based Testing**: Test object-oriented components and class behaviors.
- **Database Testing**: Interact with SQLite databases to test CRUD operations.
- **Mocking and Faking**: Utilize mocks and fakes to isolate units under test.
- **Service Layer Testing**: Test service abstractions and business logic.

## Project Structure

```
├── api.py
├── class_study.py
├── db_sqlite.py
├── main.py
├── mock_fake.py
├── service_fake.py
├── test_api.py
├── test_class_study.py
├── test_db_sqlite.py
├── test_main.py
├── test_mock.py
├── test_service.py
├── requirements.txt
└── .gitignore
```

- `api.py` & `test_api.py`: Contains API-related functions and their tests.
- `class_study.py` & `test_class_study.py`: Demonstrates class implementations and corresponding tests.
- `db_sqlite.py` & `test_db_sqlite.py`: Handles SQLite database operations and tests.
- `main.py` & `test_main.py`: Entry point and its tests.
- `mock_fake.py` & `test_mock.py`: Showcases mocking techniques.
- `service_fake.py` & `test_service.py`: Simulates service layers and tests.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IgoMedeiros/pytest-playground.git
   cd pytest-playground
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

Execute all tests using `pytest`:

```bash
pytest
```

For more detailed output:

```bash
pytest -v
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

---

Feel free to customize this `README.md` further to suit your project's specific needs. 