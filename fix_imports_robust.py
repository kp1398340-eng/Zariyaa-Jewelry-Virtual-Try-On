
import os
import re

def fix_all_imports():
    lib_path = 'lib'
    package_name = 'zariya_app'
    
    # 1. Map all files to their package paths
    file_map = {} # basename -> package path
    for root, dirs, files in os.walk(lib_path):
        for file in files:
            if file.endswith('.dart'):
                full_path = os.path.join(root, file)
                # Convert lib/core/utils/constants.dart -> package:zariya_app/core/utils/constants.dart
                rel_path = os.path.relpath(full_path, lib_path).replace('\\', '/')
                package_path = f"package:{package_name}/{rel_path}"
                file_map[file] = package_path
    
    print(f"Mapped {len(file_map)} files.")

    # 2. Find and replace all relative imports
    # Regex to find: import '...'; or import "...";
    import_pattern = re.compile(r"import\s+['\"]([^'\"\n]+)['\"]")
    
    for root, dirs, files in os.walk(lib_path):
        for file in files:
            if file.endswith('.dart'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                changed = False
                new_lines = []
                for line in lines:
                    match = import_pattern.search(line)
                    if match:
                        imported_path = match.group(1)
                        # Skip if it's already a package or dart import
                        if not (imported_path.startswith('package:') or imported_path.startswith('dart:')):
                            basename = os.path.basename(imported_path)
                            if basename in file_map:
                                new_package_path = file_map[basename]
                                # Replace the path in the line
                                line = line.replace(imported_path, new_package_path)
                                changed = True
                    new_lines.append(line)
                
                if changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)
                    print(f"Fixed imports in: {filepath}")

if __name__ == "__main__":
    fix_all_imports()
