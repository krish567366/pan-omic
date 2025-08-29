#!/usr/bin/env python3
"""
Setup script for PCE documentation using MkDocs.
Creates the complete documentation structure and builds the site.
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"📋 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return None

def setup_mkdocs_environment():
    """Set up MkDocs environment."""
    print("🚀 Setting up PCE Documentation with MkDocs")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("mkdocs.yml").exists():
        print("❌ mkdocs.yml not found. Please run this script from the repository root.")
        return False
    
    # Install MkDocs requirements
    run_command(
        "pip install -r docs/requirements.txt",
        "Installing MkDocs dependencies"
    )
    
    # Verify MkDocs installation
    result = run_command("mkdocs --version", "Verifying MkDocs installation")
    if result:
        print(f"📦 MkDocs version: {result.stdout.strip()}")
    
    return True

def create_documentation_structure():
    """Create additional documentation files."""
    print("\n📁 Creating documentation structure...")
    
    docs_structure = {
        "docs/installation.md": """# Installation Guide

## System Requirements

- Python 3.8+
- 8GB RAM minimum (16GB recommended)
- CUDA-capable GPU (optional, for acceleration)

## Quick Install

```bash
# Clone repository
git clone https://github.com/pan-omic/pce.git
cd pce

# Install in development mode
pip install -e .

# Verify installation
python -c "import pce; print('PCE installed successfully!')"
```

## Detailed Installation

See [Setup Guide](setup.md) for comprehensive installation instructions.
""",
        
        "docs/quickstart.md": """# Quick Start Guide

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
""",
        
        "docs/examples.md": """# Examples

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
""",

        "docs/javascripts/mathjax.js": """window.MathJax = {
  tex: {
    inlineMath: [["\\\\(", "\\\\)"]],
    displayMath: [["\\\\[", "\\\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => { 
  MathJax.typesetPromise()
})
""",

        "docs/stylesheets/extra.css": """.md-header {
  background: linear-gradient(45deg, #673AB7, #9C27B0);
}

.md-tabs {
  background: linear-gradient(45deg, #673AB7, #9C27B0);
}

.md-footer {
  background: linear-gradient(45deg, #673AB7, #9C27B0);
}

/* Consciousness metrics styling */
.consciousness-metric {
  background: linear-gradient(135deg, #E1BEE7, #F3E5F5);
  border-left: 4px solid #9C27B0;
  padding: 1rem;
  margin: 1rem 0;
  border-radius: 4px;
}

/* Patent information styling */
.patent-info {
  background: linear-gradient(135deg, #E8F5E8, #F1F8E9);
  border-left: 4px solid #4CAF50;
  padding: 1rem;
  margin: 1rem 0;
  border-radius: 4px;
}

/* Code highlighting for consciousness values */
.consciousness-phi {
  background: #E1BEE7;
  color: #4A148C;
  padding: 2px 6px;
  border-radius: 3px;
  font-weight: bold;
}
"""
    }
    
    # Create documentation files
    for file_path, content in docs_structure.items():
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        if not path.exists():
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Created {file_path}")
        else:
            print(f"⚠️  {file_path} already exists, skipping")

def build_documentation():
    """Build the MkDocs documentation."""
    print("\n🔨 Building documentation...")
    
    # Build the documentation
    result = run_command("mkdocs build", "Building MkDocs site")
    if result:
        print("✅ Documentation built successfully in 'site/' directory")
        
        # Check if site was created
        if Path("site/index.html").exists():
            print("📄 Site files created successfully")
        else:
            print("❌ Site files not found")
    
    return result is not None

def serve_documentation():
    """Start the MkDocs development server."""
    print("\n🌐 Starting documentation server...")
    print("📋 The documentation will be available at: http://localhost:8000")
    print("📋 Press Ctrl+C to stop the server")
    
    try:
        subprocess.run("mkdocs serve", shell=True, check=True)
    except KeyboardInterrupt:
        print("\n👋 Documentation server stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start documentation server: {e}")

def main():
    """Main setup function."""
    print("🧠 Pan-Omics Consciousness Engine (PCE)")
    print("📚 Documentation Setup Script")
    print("=" * 50)
    
    # Setup environment
    if not setup_mkdocs_environment():
        print("❌ Failed to setup MkDocs environment")
        return 1
    
    # Create documentation structure
    create_documentation_structure()
    
    # Build documentation
    if not build_documentation():
        print("❌ Failed to build documentation")
        return 1
    
    # Ask user if they want to start the server
    response = input("\n🤔 Would you like to start the documentation server? (y/N): ")
    if response.lower().startswith('y'):
        serve_documentation()
    else:
        print("\n✅ Documentation setup complete!")
        print("📋 To view the documentation:")
        print("   mkdocs serve")
        print("📋 To deploy to GitHub Pages:")
        print("   mkdocs gh-deploy")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
