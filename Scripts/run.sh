cd ~/Downloads/afl_preprocessing
python3.7 ./instrumentor.py
gcc examples/example_1_instrumented.c -pthread -fsanitize=thread