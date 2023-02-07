def add_task(mdFile,data):
    mdFile.new_header(level=2, title=data['task-1'])
    mdFile.new_paragraph(data['task-1-description-1'])
    mdFile.new_paragraph()

def add_topic_description(mdFile,data):
    mdFile.new_paragraph(data['paragraph-level-1'])
    mdFile.new_paragraph()
