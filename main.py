from mdutils.mdutils import MdUtils
import yaml
import sys

from helper import add_task,add_topic_description
import time
if len(sys.argv) < 2:
    print("Please provide a YAML file")
    print("Usage: python main.py <yaml-file>")
    sys.exit(1)


with open(sys.argv[1], "r") as stream:
    data = yaml.safe_load(stream)
    mdFile = MdUtils(file_name=data['filename'], title=data['filename'])

    mdFile.new_header(level=1, title=data['heading-level-1'])  # style is set 'atx' format by default.

    # Create a new Topic Description here by calling the function again
    
    # Topic 1
    add_topic_description(mdFile,data)

    # Create tasks here  by calling the function again

    # Task 1
    add_task(mdFile, data)
    
    # add Quote Here
    mdFile.new_paragraph(data['quote'])

print(f"Creating Markdown file from {sys.argv[1]}")
mdFile.create_md_file()