# System 1 vs System 2 Neural Network

Inspired by Daniel Kahneman's dual-process theory.

## Concepts
- System 1: fast, intuitive, automatic
- System 2: slow, logical, deliberate

## Architecture
Input → System1 + System2 → Gating → Output

y = alpha * S1 + (1-alpha) * S2

## Install
pip install torch

## Run (2 lines)
from dual_process_model import DualProcessModel; import torch
print(DualProcessModel(10)(torch.randn(1,10)))

## Insight
Model dynamically balances intuition vs reasoning.
