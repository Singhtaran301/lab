import os
import re

def generate_toc_for_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    toc = []
    updated_lines = []
    for line in lines:
        match = re.match(r'^(#{1,6}) (.+)', line)
        if match:
            level = len(match.group(1))
            title = match.group(2)
            anchor = title.lower().replace(' ', '-').replace('.', '').replace(',', '')
            toc.append(f"{'  ' * (level - 1)}- [{title}](#{anchor})")
        updated_lines.append(line)

    toc_content = "\n".join(toc)
    updated_lines.insert(1, f"\n## Table of Contents\n\n{toc_content}\n\n")

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

    print(f"TOC added to {file_path}")

def generate_toc_for_markdown_files():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                generate_toc_for_file(file_path)

if __name__ == "__main__":
    generate_toc_for_markdown_files()
