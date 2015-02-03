from flask import Flask, request, render_template
import subprocess
import tempfile
import shutil
import os


app = Flask(__name__)


@app.route("/llvm", methods=["POST"])
def llvm():
    code = request.form["code"]

    dirpath = tempfile.mkdtemp()
    print "llvm: Creating temporary directory: {}".format(dirpath)

    # Write the code out to a file
    codepath = os.path.join(dirpath, "code.c")
    respath = os.path.join(dirpath, "code.ll")
    errpath = os.path.join(dirpath, "err.txt")

    with open(codepath, "w") as f:
        f.write(code)

    # Run clang
    with open(errpath, "w") as ef:
        status = subprocess.call([
            "clang", "-emit-llvm", "-S", "-O0", codepath, "-o", respath
        ], stderr=ef)

    if status != 0:
        with open(errpath, "r") as f:
            result = f.read()
    else:
        with open(respath, "r") as f:
            result = f.read()

    shutil.rmtree(dirpath)
    print "llvm: Removed temporary directory: {}".format(dirpath)

    return result

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=3000, debug=True)
