from pathlib import Path

from mlx_lm.utils import load


MODEL_NAME = "mlx-community/Qwen2.5-Coder-7B-Instruct-4bit"


def main():

    print("=" * 60)
    print("QA AI Platform")
    print("=" * 60)
    print()

    print(f"Downloading model:")
    print(f"{MODEL_NAME}")
    print()

    # download + cache
    model, tokenizer = load(MODEL_NAME)

    print()
    print("=" * 60)
    print("Model downloaded successfully.")
    print("=" * 60)

    print()
    print("Model cache location:")

    cache = Path.home() / ".cache" / "huggingface"

    print(cache)


if __name__ == "__main__":
    main()