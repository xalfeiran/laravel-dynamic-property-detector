# Laravel Dynamic Property Detector

This Python script scans a Laravel project and detects dynamically used but undeclared properties in PHP classes. It can help identify potential issues where properties are used without being explicitly declared.

## Features

- Recursively scans Laravel project folders, excluding the `vendor` directory.
- Identifies properties used in `$this->propertyName` format that are not explicitly declared in the class.
- Filters out known Laravel properties and handles inherited properties from extended classes.
- Supports PHP docblock comments and type hints in property declarations.

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/xalfeiran/laravel-dynamic-property-detector.git
   ```
2. Navigate to the project directory:
   ```bash
   cd laravel-dynamic-property-detector
   ```

## Usage

1. Place this script in the root directory of your Laravel project.
2. Update the `project_path` variable in the script to point to your Laravel project directory.
3. Run the script:
   ```bash
   python3 detect_dynamic.py
   ```

The script will output a list of PHP files with dynamically used properties that aren’t explicitly declared in those files.

### Example Output

```
File: /path/to/laravel/app/SomeClass.php
Dynamic Properties: {'someUndeclaredProperty', 'anotherDynamicProperty'}

File: /path/to/laravel/app/AnotherClass.php
Dynamic Properties: {'yetAnotherProperty'}
```

## Configuration

### Known Properties

The script includes a base set of known Laravel-specific properties, which can be configured in the `KNOWN_PROPERTIES` variable. Add any additional properties you wish to exclude from the findings to this list.

### Exclusion of Parent Class Properties

The script also supports excluding inherited properties from a parent class if the analyzed class extends another class in your Laravel project.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to improve the script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Author

Created by [Xavier Alfeiran](https://github.com/xalfeiran).
