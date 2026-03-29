import torch
import torch.nn as nn

# System 1: Fast, intuitive
class System1(nn.Module):
    def __init__(self, input_dim, hidden=128, out_dim=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, out_dim)
        )
    def forward(self, x):
        return self.net(x)

# System 2: Slow, analytical
class System2(nn.Module):
    def __init__(self, input_dim, hidden=64, out_dim=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, out_dim)
        )
    def forward(self, x):
        return self.net(x)

# Gating (decides reliance)
class Gating(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.linear = nn.Linear(dim, 1)
    def forward(self, s1_out):
        return torch.sigmoid(self.linear(s1_out))

# Full Model
class DualProcessModel(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.s1 = System1(input_dim)
        self.s2 = System2(input_dim)
        self.gate = Gating(64)

    def forward(self, x):
        s1_out = self.s1(x)
        s2_out = self.s2(x)

        alpha = self.gate(s1_out)
        alpha_exp = alpha.expand_as(s1_out)

        y = alpha_exp * s1_out + (1 - alpha_exp) * s2_out
        return y, alpha

if __name__ == "__main__":
    model = DualProcessModel(10)
    x = torch.randn(1,10)
    y, alpha = model(x)
    print("Output:", y)
    print("System1 dominance:", alpha)
