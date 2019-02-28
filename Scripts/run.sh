cd ~/Downloads/afl_preprocessing
python3.7 ./instrumentor.py
mkdir input
echo "" >input/test
mkdir output
afl-gcc examples\after\example_1_instrumented.c -pthread -fsanitize=thread

TSAN_OPTIONS="abort_on_error=1" afl-fuzz -m none  -i input/ -o output/  ~/Downloads/afl_preprocessing/a.out