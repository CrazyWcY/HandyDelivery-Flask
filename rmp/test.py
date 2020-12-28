from convertTool import print_task
from convertTool import rmpFormat2task, task2rmpFormat
from initial_data import user, tasks

for i,task in enumerate(tasks):
    try:
        print_task(rmpFormat2task(task2rmpFormat(task)))
    except Exception:
        print(i)
        exit(0)