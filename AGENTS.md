# PhyloData Python Library - Agent Guidelines

## Development Guidelines

### Code Style & Standards

- **Python 3.10+**: Use modern Python features and syntax
- **Pytest**: Testing framework
- **Click**: CLI interface framework

## Best Practices for Agents

### When Working on This Project

- **Understand the Domain**: Familiarize yourself with the terminology
- **Use Modern Python**: Leverage Python 3.10+ features like pattern matching and improved type hints
- **Type Everything**: Add comprehensive type hints to all functions and classes
- **Docstrings**: Add docstrings for everything but internal provate functions. Arguments need only be described in user-facing methods
- **Modular Design**: Think about software design. Design components in a modular but concise way
- **Handle Errors Gracefully**: Use custom exceptions and proper error messages
- **Use Path Objects**: Prefer `pathlib.Path` over string paths
- **Top-down approach**: Have the main functions first, followed by smaller helper functions

### Code Quality Standards

- **No Unnecessary Comments**: Use descriptive variable names and docstrings instead
- **Consistent Style**: Follow existing code patterns and naming conventions
- **Small, Focused Changes**: Break down large changes into manageable tasks