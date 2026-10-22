# Socio-Economic Emergence Engine (V1 Baseline)

A zero-dependency, ultra-fast simulation engine written strictly in **pure Python**. Built from first principles, V1 establishes a high-performance computational baseline for modeling agent survival, memory pruning, and evolutionary complex system dynamics.

---

## 🚀 Key Features

- **Zero-Dependency Architecture**: 100% pure Python execution without heavy external AI or simulation frameworks.
- **Ultra-High Performance**: Executes tens of thousands of generations in seconds (e.g., over 24,000 generations in ~1 second).
- **Dynamic Context Compression (Memory Pruning)**: KV-Cache-like memory management preventing state bloat over long horizons.
- **9:1 Resource Distribution**: Dynamically allocates resources based on fitness ranks, channeling major boosts to the top 10% elite agents to drive evolutionary selection.
- **The Elder Protocol**: An anti-extinction fail-safe mechanism that triggers mutation and backup seed derivation when the population drops down to a single survivor.

---

## 🛠️ Quick Start

Clone the repository and run the engine locally:

```bash
# Clone the repository
git clone [https://github.com/0esky/socio-economic-engine.git](https://github.com/0esky/socio-economic-engine.git)

# Navigate to directory
cd socio-economic-engine

# Run the V1 engine
python sandbox_v1.py
