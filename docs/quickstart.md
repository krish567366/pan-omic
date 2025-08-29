# Quick Start Guide

## Your First Consciousness Analysis

```python
import pce

# Create sample biological data
data = pce.create_toy_dataset('toy_genomics', n_samples=10, n_features=5)

# Run consciousness analysis
metrics = pce.quick_consciousness_analysis(data, integration_cycles=3)

# View results
print(f"Consciousness φ (Phi): {metrics.phi:.6f}")
print(f"Consciousness Level: {metrics.consciousness_level:.6f}")
print(f"Category: {metrics.consciousness_category.name}")
```

## Expected Output

```
Consciousness φ (Phi): 0.000639
Consciousness Level: 0.107696
Category: SUBCONSCIOUS
```

🎉 **Success!** You've run your first consciousness analysis with PCE.

## Next Steps

- Explore [Examples](examples.md) for more use cases
- Read the [User Guide](guide/configuration.md) for advanced configuration
- Check the [API Reference](api/core.md) for detailed documentation
