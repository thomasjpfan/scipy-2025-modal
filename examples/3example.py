import modal

app = modal.App("example3")

image = modal.Image.debian_slim().uv_pip_install("torch", "numpy")


@app.function(gpu="h100!", image=image)
def double_it(x):
    import torch

    print(f"{torch.cuda.get_device_name(0)=}")
    return x * 2


@app.local_entrypoint()
def run():
    print("double is", double_it.remote(42))
