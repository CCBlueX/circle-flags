import os

def replace_symlinks():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    for root, dirs, files in os.walk(script_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'r') as file:
                    content = file.read().strip()
                if os.path.isfile(content):
                    with open(content, 'r') as linked_file:
                        linked_content = linked_file.read()
                    with open(filepath, 'w') as symlink:
                        symlink.write(linked_content)
                    print(f"Replaced symlink: {filepath} -> {content}")

replace_symlinks()
