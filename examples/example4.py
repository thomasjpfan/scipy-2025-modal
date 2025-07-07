import modal

app = modal.App("example4")

image = modal.Image.debian_slim().uv_pip_install("torch", "numpy")


@app.function(gpu="h100", image=image)
def double_it(x):
    return x * 2


@app.local_entrypoint()
def run():
    values = list(range(100))
    results = double_it.map(values)
    print(list(results))
