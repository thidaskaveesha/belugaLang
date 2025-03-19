# Beluga Programming Language

Beluga is a simple, beginner-friendly programming language inspired by C and Python. It is designed to help you learn the basics of programming language design and implementation. Beluga supports basic data types, functions, and expressions, with the following features:

## Features
- **Keywords**: `function`, `if`
- **Data Types**: `int`, `float`, `bool`, `string`
- **Comments**: Single-line comments starting with `//`
- **No Loops Yet**: Loops will be added in future versions.
- **Syntax**: Data types are specified before variable names and function parameters.
  - Example: `string name = "Thidas";`
  - Example: `int function (int a, int b) {}`

## Getting Started

### Prerequisites
- Python 3.8 or higher installed on your system.

### Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd beluga
   ```
2. Run the Beluga compiler:
   ```bash
   python beluga.py <filename>.beluga
   ```

## Writing Your First Program
Create a file with the `.beluga` extension, e.g., `example.beluga`. Here's a simple example:

```beluga
int function add(int a, int b) {
    int result = a + b;
    return result;
}
```

### Running Your Program
Run the Beluga compiler on your `.beluga` file:
```bash
python beluga.py example.beluga
```
If the program compiles successfully, the output will be displayed.

## Language Specification

### Data Types
- `int`: Integer values
- `float`: Floating-point values
- `bool`: Boolean values (`true` or `false`)
- `string`: String values (enclosed in double quotes)

### Functions
- Functions are defined using the `function` keyword.
- The return type is specified before the `function` keyword.
- Parameters include their data types, and all types are declared before names.
  
**Example:**
```beluga
int function multiply(int x, int y) {
    int product = x * y;
    return product;
}
```

### Variables
- Variables must be declared with their type before use.
- Example:
  ```beluga
  string message = "Hello, Beluga!";
  int number = 42;
  ```

### Comments
- Single-line comments start with `//`.
  ```beluga
  // This is a comment
  int number = 10; // Inline comment
  ```

## Error Handling
The Beluga compiler provides meaningful syntax error messages to help you debug your code. Example errors include:
- Missing semicolons
- Mismatched braces
- Incorrect data type usage

## Roadmap
- Adding loop support (e.g., `for`, `while`)
- Expanding the standard library
- Support for advanced data structures

## Contributing
We welcome contributions to improve the Beluga language! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the GNU License. See the LICENSE file for details.

## Acknowledgments
Special thanks to the programming community for inspiring this project.
