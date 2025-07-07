import modal

app = modal.App("example2")


@app.function(gpu="h100")
def double_it(x):
    return x * 2


@app.local_entrypoint()
def run():
    print("double is", double_it.remote(42))
