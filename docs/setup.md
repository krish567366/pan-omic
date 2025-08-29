# PCE Setup Guide

This guide will help you set up and run the Pan-Omics Consciousness Engine (PCE) on your system.

## Prerequisites

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: At least 4GB RAM (8GB recommended)
- **Storage**: 2GB free space

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/pce-project/pce.git
cd pce
```

### 2. Set Up Python Environment

#### Using conda (recommended):
```bash
conda create -n pce python=3.8
conda activate pce
```

#### Using venv:
```bash
python -m venv pce_env
# On Windows:
pce_env\Scripts\activate
# On macOS/Linux:
source pce_env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -e .
```

### 4. Verify Installation

```bash
python -c "import pce; print(f'PCE v{pce.__version__} ready!')"
```

Expected output:
```
PCE v1.0.0-alpha ready!
```

## Quick Test

Run the complete system test to verify everything is working:

```python
import pce

# Create test dataset
data = pce.create_toy_dataset('toy_genomics', 10, 5)
print(f'Dataset: {data.name} with {len(data.get_all_entities())} entities')

# Run consciousness analysis
metrics = pce.quick_consciousness_analysis(
    data, 
    integration_cycles=3, 
    save_results=False
)

# Display results
print(f'Consciousness φ (Phi): {metrics.phi:.6f}')
print(f'Consciousness Level: {metrics.consciousness_level:.6f}')
print(f'Category: {metrics.consciousness_category.name}')
```

Expected output:
```
Dataset: Toy Genomics Dataset with 5 entities
Consciousness φ (Phi): 0.000639
Consciousness Level: 0.107696
Category: SUBCONSCIOUS
```

## Optional Dependencies

For enhanced performance and features, install optional dependencies:

```bash
# Scientific computing (recommended)
pip install scipy scikit-learn

# Visualization (optional)
pip install matplotlib seaborn plotly

# Development tools (if contributing)
pip install pytest black flake8 mypy
```

## System Configuration

PCE can be configured through environment variables:

```bash
# Set log level
export PCE_LOG_LEVEL=INFO

# Set number of parallel processes
export PCE_NUM_PROCESSES=4

# Enable GPU acceleration (if available)
export PCE_USE_GPU=true
```

## Troubleshooting

### Common Issues

1. **Import Error: No module named 'pce'**
   ```bash
   # Make sure you installed with -e flag
   pip install -e .
   ```

2. **Numerical Warnings**
   - These are normal for small datasets and don't affect functionality
   - Can be suppressed with: `export PCE_SUPPRESS_WARNINGS=true`

3. **Slow Performance**
   - Install optional dependencies: `pip install scipy scikit-learn`
   - Reduce integration cycles for testing: `integration_cycles=2`
   - Use smaller datasets for initial testing

4. **Memory Issues**
   - Reduce population size in E³DE: modify config files
   - Use fewer simulation steps in HDTS
   - Process smaller datasets initially

### Getting Help

If you encounter issues:

1. Check the [FAQ](docs/faq.md)
2. Search [existing issues](https://github.com/pce-project/pce/issues)
3. Create a new issue with:
   - Your operating system
   - Python version
   - Complete error message
   - Steps to reproduce

## Next Steps

Once PCE is installed and verified:

1. **Explore Examples**: Check `examples/` directory for usage patterns
2. **Read Documentation**: See detailed API documentation
3. **Run Benchmarks**: Test with different dataset sizes
4. **Contribute**: See contributing guidelines for development setup

## Performance Expectations

For the toy genomics dataset (5 entities):

- **Hypergraph Construction**: ~0.003s
- **Neural Network Encoding**: ~0.15s  
- **Quantum Optimization**: ~4.4s
- **Evolutionary Simulation**: ~0.3s
- **Multi-scale Simulation**: ~90s
- **Consciousness Integration**: ~0.15s
- **Total Runtime**: ~95s

Performance scales with dataset size and system complexity.

## System Requirements by Use Case

### Research/Development
- **CPU**: 4+ cores recommended
- **RAM**: 8GB minimum, 16GB recommended
- **Storage**: 5GB for development environment

### Production/Large Datasets
- **CPU**: 8+ cores, preferably with AVX support
- **RAM**: 32GB+ recommended
- **GPU**: CUDA-compatible GPU for acceleration
- **Storage**: SSD recommended, 50GB+ for large datasets

Congratulations! You now have a working PCE installation. 🎉
