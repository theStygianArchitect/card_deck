# Deck of Cards

A Python project built with **Python 3.13.1**, featuring **pytest** for testing and **coverage** for test coverage
analysis.

## Features

- Comprehensive testing using `pytest`.
- Test coverage analysis with `coverage`.
- Easy setup and simple execution.

## Requirements

- **Python 3.13.1** or later
- Installed Python packages:
   - `pytest`
   - `coverage`

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/theStygianArchitect/card_deck.git
   cd card_deck
   git checkout card
   ```

2. [Optional] Create a virtual environment and activate it:
   ```bash
   uv venv
   source env/bin/activate  # On Windows, use: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

## Usage

Run your Python scripts or start your project. Example:

```bash
TBD
```

## Running Tests

This project uses `pytest` for testing. To run the tests, use:

```bash
uv run pytest tests/
```

To check the test coverage:

```bash
uv run coverage run -m pytest
uv run coverage report
```

## Contributing

Contributions are always welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b <branch-name>
   ```
3. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Your commit message"
   ```
4. Push your branch:
   ```bash
   git push origin <branch-name>
   ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Update this section if another license applies.
