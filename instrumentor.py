with open('example_1.c') as f:
    lines = f.readlines()

new_lines = lines.copy()
for index, line in enumerate(lines):
    if "pthread_mutex_lock" in line:
        new_lines.insert(index, 'sleep(1);\n')

with open('exmaple_1_instrumented.c', 'w') as fw:
    for line in new_lines:
        fw.write(line)


