# Examples

## Basic Genomics Analysis

```python
import pce

# Load genomics data
genomics_data = pce.create_toy_dataset('toy_genomics', 100, 50)

# Configure analysis
config = pce.get_config()
config.mogil.embedding_dim = 256
config.qlem.temperature = 310.0

# Run analysis
metrics = pce.quick_consciousness_analysis(genomics_data)
print(f"Genomics φ: {metrics.phi:.6f}")
```

## Multi-Omics Integration

```python
# Create multi-omics dataset
multi_omics = pce.create_toy_dataset('toy_multi_omics', 50, 25)

# Advanced analysis
pce_system = pce.create_pce_system()
hypergraph = pce_system.mogil.build_hypergraph(multi_omics)
embedding = pce_system.mogil.encode(hypergraph)
consciousness_metrics = pce_system.integrate_consciousness(embedding)
```

## Custom Configuration

```python
# Custom PCE configuration
custom_config = {
    'mogil': {'embedding_dim': 512, 'attention_heads': 8},
    'qlem': {'alpha': 2.0, 'beta': 1.0},
    'e3de': {'population_size': 50, 'generations': 20},
    'hdts': {'simulation_time': 0.5},
    'cis': {'integration_cycles': 10}
}

# Run with custom settings
metrics = pce.quick_consciousness_analysis(
    data, 
    config=custom_config,
    save_results=True,
    output_dir='results/'
)
```
