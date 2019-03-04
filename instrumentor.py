import os

sleep_indicators = ["pthread_mutex_lock" ,"pthread_mutex_wait", "pthread_mutex_sleep"]

for root, dirs, files in os.walk("./examples/before"):
    for name in files:
        file_path = (os.path.join(root, name))


        with open(file_path) as f:
            lines = f.readlines()

        new_lines = lines.copy()
        for line in lines:
            if lines.index(line) == 0:
                # globals
                new_lines.insert(new_lines.index(line), '#include <stdio.h>\n #include <unistd.h>\n')
            for indicator in sleep_indicators:
                if indicator in line:
                    new_lines.insert(new_lines.index(line), '{char sec=getchar();\n if (sec >= 0x30 && sec <= 0x39) usleep(11);\n}')

        with open('./examples/after/'+name.split('.')[0]+'_instrumented.c', 'w') as fw:
            for line in new_lines:
                fw.write(line)


