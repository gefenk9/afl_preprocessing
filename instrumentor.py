import os

sleep_indicators = ["pthread_mutex_lock"]

for root, dirs, files in os.walk("./examples/before"):
    for name in files:
        file_path = (os.path.join(root, name))


        with open(file_path) as f:
            lines = f.readlines()

        new_lines = lines.copy()
        for line in lines:
            if lines.index(line) == 0:
                # globals
                new_lines.insert(new_lines.index(line), '#include <stdio.h>\n')
            for indicator in sleep_indicators:
                if indicator in line:
                    new_lines.insert(new_lines.index(line), 'int sec=0;\n scanf("%d", &sec);\n if (sec >= 0 && sec <= 1) sleep(sec);\n')

        with open('./examples/after/'+name.split('.')[0]+'_instrumented.c', 'w') as fw:
            for line in new_lines:
                fw.write(line)


