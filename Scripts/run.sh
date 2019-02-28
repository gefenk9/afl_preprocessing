cd ~/Downloads/afl_preprocessing
python3.7 ./instrumentor.py
gcc examples/example_1_instrumented.c -pthread -fsanitize=thread
mkdir input
"\n">test
mkdir output
TSAN_OPTIONS="abort_on_error=1" afl-fuzz -m none  -i input/ -o output/  ~/Downloads/a.out