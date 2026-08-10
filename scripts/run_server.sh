#!/bin/bash

set -e

MODEL="mlx-community/Qwen2.5-Coder-7B-Instruct-4bit"

echo "======================================"
echo " QA AI Platform"
echo " MLX Server"
echo "======================================"

uv run mlx_lm.server \
  --model "$MODEL" \
  --host 127.0.0.1 \
  --port 8080 \
  --log-level INFO \
  --temp 0.2 \
  --max-tokens 4096