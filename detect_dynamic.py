import os
import re

# Define known properties to exclude from the findings
KNOWN_PROPERTIES = {
    'timestamps', 'incrementing', 'connection', 'table', 'primaryKey', 'keyType',
    'fillable', 'guarded', 'hidden', 'casts', 'dates', 'appends', 'with', 'withCount',
    'dispatchesEvents', 'observables', 'touches', 'perPage', 'incrementing', 'exists'
}

def get_php_files(root_dir):
    """Recursively find all PHP files in the Laravel project, excluding the vendor folder."""
    php_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        if 'vendor' in dirpath:  # Skip the vendor directory
            continue
        for file in filenames:
            if file.endswith('.php'):
                php_files.append(os.path.join(dirpath, file))
    return php_files

def extract_class_properties(file_content):
    """Extract properties used in the class but not explicitly declared."""
    # Remove lines that start with // to avoid matching commented-out properties
    file_content = "\n".join(line for line in file_content.splitlines() if not line.strip().startswith("//"))
    
    # Find all properties used in the class that are not followed by parentheses (e.g., $this->propertyName)
    used_properties = re.findall(r'\$this->(\w+)\b(?!\()', file_content)
    
    # Enhanced regex to find declared properties, including optional type hints and docblocks
    declared_properties = re.findall(
        r'(?:\/\*\*[^*]*\*\/\s*)?'          # Optional docblock (/** ... */)
        r'(?:public|protected|private)\s+'   # Access modifier
        r'(?:[\w|\s]+)?\s*'                 # Optional type hint (e.g., string, array)
        r'\$(\w+)',                         # Property name
        file_content,
        re.DOTALL | re.MULTILINE
    )
    
    # Get unique dynamic properties, excluding known properties
    dynamic_properties = (set(used_properties) - set(declared_properties)) - KNOWN_PROPERTIES
    
    return dynamic_properties

def map_dynamic_properties(project_path):
    """Map each PHP class with its dynamically used but undeclared properties."""
    php_files = get_php_files(project_path)
    dynamic_properties_map = {}
    
    for file_path in php_files:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            dynamic_properties = extract_class_properties(content)
            if dynamic_properties:
                dynamic_properties_map[file_path] = dynamic_properties
    
    return dynamic_properties_map

# Example usage:
project_path = '/path/to/laravel/project'  # Replace with your Laravel project path
dynamic_properties_map = map_dynamic_properties(project_path)

for file, properties in dynamic_properties_map.items():
    print(f"File: {file}")
    print(f"Dynamic Properties: {properties}\n")

