#!/bin/bash

set -e

MODEL_NAME="mlx-community/Qwen2.5-Coder-7B-Instruct-4bit"

echo "========================================"
echo " QA AI Platform"
echo " Download MLX Model"
echo "========================================"

echo ""
echo "Model : ${MODEL_NAME}"
echo ""

uv run python scripts/download_model.py

echo ""
echo "========================================"
echo "Download completed!"
echo "========================================"