
# Thread Sanitizer Fuzzer
We take advantage of the (Fuzzing concept)[http://lcamtuf.coredump.cx/afl/] combined with (Thread Sanitizer)[https://github.com/google/sanitizers/wiki/ThreadSanitizerCppManual] tool, in order to achieve great abilities to find Race Condition bugs in multi-threaded code. In this article we will explain about the above terms, our research process, problems we encountered, the experiments and more.

## Usage

```python
cd Scripts/
./run.sh
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

