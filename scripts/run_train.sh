#!/bin/bash
# 启动训练脚本

cd "$(dirname "$0")/.." || exit

python src/train.py \
    --batch_size 32 \
    --epochs 10 \
    --lr 0.001
