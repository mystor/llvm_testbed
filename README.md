# llvm_testbed

A simple program. Serves a website where you enter C code, and will execute clang with `-S -emit-llvm` to generate the IR for the code, and then displays it on the right.

## Running

```
$ pip install -r requirements.txt
$ python main.py
$ firefox http://localhost:3000
```
