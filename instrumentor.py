
sleep_indicators = ["pthread_mutex_lock"]
with open('./examples/example_1.c') as f:
    lines = f.readlines()

new_lines = lines.copy()
for line in lines:
    if lines.index(line) == 0:
        # globals
        new_lines.insert(new_lines.index(line), '#include <stdio.h>\n')
    for indicator in sleep_indicators:
        if indicator in line:
            new_lines.insert(new_lines.index(line), 'float sec=0.0;\n scanf("%f", &sec);\n if (sec >= 0 && sec <= 10) sleep(sec/10);\n')

with open('./examples/example_1_instrumented.c', 'w') as fw:
    for line in new_lines:
        fw.write(line)


