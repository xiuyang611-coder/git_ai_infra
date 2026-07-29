"""一个简单的两层 MLP 模型"""


class TwoLayerMLP:
    def __init__(self, input_dim, hidden_dim, output_dim):
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim

    def forward(self, x):
        """假 forward，阶段 3 才会真实现"""
        raise NotImplementedError("阶段 3 用 CUDA 实现")
