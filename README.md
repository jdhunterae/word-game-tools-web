# Word Game Tools Web

A collection of Python tools to help solve various word games, including the NYT Spelling Bee. This project includes both command-line tools and (coming soon) a web interface for interactive solving.

## Features

Current tools:

- Spelling Bee Helper: Find valid words for the NYT Spelling Bee puzzle
- More games coming soon!

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/word-game-tools-web.git
cd word-game-tools-web
```

Install in development mode:

```bash
pip install -e .
```

## Usage

### Spelling Bee Helper

The Spelling Bee helper takes a center letter (must be used) and 6 additional letters. It returns possible valid words sorted by length and frequency of the center letter.

```bash
bee-helper C I D A Y E M
```

Or run as a module:

```bash
python -m wordgames.cli.bee_helper C I D A Y E M
```

## Project Structure

```
wordgames/
├── core/          # Core functionality and utilities
├── games/         # Game-specific logic
├── cli/           # Command-line interfaces
└── web/           # Web interface (coming soon)
```

## Development

### Requirements

- Python 3.8+
- Additional requirements listed in requirements.txt

### Setting up a development environment

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install development dependencies:

```bash
pip install -r requirements.txt
```

### Running Tests

```bash
python -m pytest
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## Planned Features

- Web interface using Flask
- Additional word games:
  - Wordle helper
  - Anagram solver
  - Word ladder solver
- Performance optimizations for larger dictionaries
- Additional dictionary sources and word lists

## License

[MIT License](LICENSE)

## Acknowledgments

- Word list sourced from [source of your dictionary file]
- Inspired by the New York Times word games
