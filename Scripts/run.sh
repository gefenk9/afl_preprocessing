python3.7 ./instrumentor.py
mkdir input
echo "" >input/test
rm -r output
mkdir output
afl-gcc examples/after/example_1_instrumented.c -pthread -fsanitize=thread
TSAN_OPTIONS="abort_on_error=1" afl-fuzz -m none -t 1500 -i input/ -o output/  $PWD/a.out
