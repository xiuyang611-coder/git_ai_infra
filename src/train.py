"""训练入口——用 argparse 接收命令行参数"""

import argparse
from model import TwoLayerMLP
from utils import setup_logger


def main():
    parser = argparse.ArgumentParser(description="训练两层 MLP")
    parser.add_argument("--batch_size", type=int, default=32, help="批次大小")
    parser.add_argument("--epochs", type=int, default=10, help="训练轮数")
    parser.add_argument("--lr", type=float, default=0.001, help="学习率")
    args = parser.parse_args()

    logger = setup_logger(__name__)
    logger.info(f"batch_size={args.batch_size}, epochs={args.epochs}, lr={args.lr}")

    model = TwoLayerMLP(input_dim=784, hidden_dim=256, output_dim=10)
    logger.info(f"模型已创建: {model.__class__.__name__}")


if __name__ == "__main__":
    main()
