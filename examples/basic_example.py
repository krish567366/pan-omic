#!/usr/bin/env python3
"""
PCE Basic Example: Consciousness Analysis from Multi-Omics Data

This example demonstrates the basic usage of the Pan-Omics Consciousness Engine
to analyze consciousness emergence from synthetic multi-omics data.

Usage:
    python basic_example.py
"""

import sys
import json
from pathlib import Path

# Add src to path if running directly
if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pce
from pce.utils.logging import get_logger

# Set up logging
logger = get_logger(__name__)


def main():
    """Run basic PCE consciousness analysis example."""
    print("=" * 60)
    print("PCE - Pan-Omics Consciousness Engine")
    print("Basic Consciousness Analysis Example")
    print("=" * 60)
    
    # Step 1: Load or create toy data
    print("\n1. Loading multi-omics data...")
    try:
        # Create synthetic neural omics data
        data = pce.create_toy_dataset(
            "toy_neural_omics", 
            n_samples=100, 
            n_features=200
        )
        print(f"   ✓ Created synthetic dataset with {len(data.samples)} samples")
        print(f"   ✓ Omics layers: {list(data.omics_layers.keys())}")
        
    except Exception as e:
        print(f"   ✗ Error creating data: {e}")
        return
    
    # Step 2: Quick consciousness analysis
    print("\n2. Running consciousness analysis...")
    try:
        metrics = pce.quick_consciousness_analysis(
            data,
            integration_cycles=50,  # Moderate complexity for demo
            save_results=True,
            output_path="pce_example_results"
        )
        
        print("   ✓ Analysis complete!")
        
    except Exception as e:
        print(f"   ✗ Error during analysis: {e}")
        return
    
    # Step 3: Display results
    print("\n3. Consciousness Analysis Results:")
    print("-" * 40)
    
    try:
        print(f"   Consciousness φ (phi):     {metrics.phi:.6f}")
        print(f"   Global Accessibility:      {metrics.global_accessibility:.6f}")  
        print(f"   Quantum Coherence:         {metrics.quantum_coherence:.6f}")
        print(f"   Hierarchical Complexity:   {metrics.hierarchical_complexity:.6f}")
        print(f"   Consciousness Level:       {metrics.consciousness_level}")
        
    except Exception as e:
        print(f"   ✗ Error displaying metrics: {e}")
        return
    
    # Step 4: Interpret results
    print("\n4. Interpretation:")
    print("-" * 40)
    
    if metrics.phi > 0.1:
        consciousness_desc = "High consciousness emergence detected"
    elif metrics.phi > 0.01:
        consciousness_desc = "Moderate consciousness emergence"
    else:
        consciousness_desc = "Low consciousness emergence"
        
    print(f"   {consciousness_desc}")
    
    if metrics.global_accessibility > 0.5:
        print("   High global information accessibility")
    else:
        print("   Limited global information accessibility")
        
    if metrics.quantum_coherence > 0.3:
        print("   Significant quantum coherence effects")
    else:
        print("   Minimal quantum coherence effects")
    
    # Step 5: Show saved results
    results_path = Path("pce_example_results")
    if results_path.exists():
        print(f"\n5. Results saved to: {results_path.absolute()}")
        
        analysis_file = results_path / "consciousness_analysis.json"
        metrics_file = results_path / "consciousness_metrics.json"
        
        if analysis_file.exists():
            print(f"   ✓ Detailed analysis: {analysis_file}")
        if metrics_file.exists():
            print(f"   ✓ Metrics summary: {metrics_file}")
    
    print("\n" + "=" * 60)
    print("PCE Basic Example Complete!")
    print("=" * 60)


def advanced_example():
    """Run advanced PCE system example with individual subsystems."""
    print("\n" + "=" * 60)
    print("Advanced PCE System Example")
    print("=" * 60)
    
    # Create toy data
    print("\n1. Creating enhanced neural omics data...")
    data = pce.create_toy_dataset(
        "toy_mixed_omics", 
        n_samples=150, 
        n_features=300
    )
    print(f"   ✓ Created dataset with {len(data.samples)} samples")
    
    # Create integrated PCE system
    print("\n2. Initializing PCE system...")
    pce_system = pce.create_pce_system(
        mogil_config={"embedding_dim": 128, "attention_heads": 8},
        qlem_config={"state_dim": 64, "optimization_steps": 100},
        e3de_config={"population_size": 50, "max_generations": 20},
        hdts_config={"num_scales": 5, "simulation_steps": 100},
        cis_config={"integration_cycles": 100}
    )
    print("   ✓ PCE system initialized with enhanced configuration")
    
    # Process through subsystems
    print("\n3. Processing through PCE subsystems...")
    
    # MOGIL: Build hypergraph and encode
    print("   MOGIL: Building hypergraph...")
    hypergraph = pce_system.mogil.build_hypergraph(data)
    print(f"     ✓ Hypergraph: {hypergraph.num_nodes} nodes, {hypergraph.num_edges} edges")
    
    print("   MOGIL: Encoding hypergraph...")
    embedding = pce_system.mogil.encode_hypergraph(hypergraph)
    print(f"     ✓ Embedding: {embedding.dimension}D, {len(embedding.entity_ids)} entities")
    
    # Q-LEM: Quantum optimization
    print("   Q-LEM: Creating quantum state...")
    pce_system.qlem.create_quantum_state(embedding)
    print("     ✓ Quantum state created")
    
    print("   Q-LEM: Optimizing entropy...")
    pce_system.qlem.minimize_entropy(embedding)
    print("     ✓ Entropy optimization complete")
    
    # E³DE: Evolutionary simulation
    print("   E³DE: Creating evolutionary population...")
    pce_system.e3de.create_population("neural_evolution", 50, 30, embedding)
    print("     ✓ Population created")
    
    print("   E³DE: Running evolution...")
    evolution_metrics = pce_system.e3de.evolve_population("neural_evolution", 20)
    print("     ✓ Evolution complete")
    
    # HDTS: Multi-scale simulation
    print("   HDTS: Creating biological system...")
    pce_system.hdts.create_biological_system(embedding)
    print("     ✓ Biological system created")
    
    print("   HDTS: Simulating consciousness emergence...")
    pce_system.hdts.simulate_consciousness_emergence(0.5)
    print("     ✓ Multi-scale simulation complete")
    
    # CIS: Final integration
    print("   CIS: Creating connectome...")
    pce_system.create_connectome(embedding)
    print("     ✓ Connectome network created")
    
    print("   CIS: Integrating consciousness...")
    final_metrics = pce_system.integrate_consciousness(integration_cycles=100)
    print("     ✓ Consciousness integration complete")
    
    # Display advanced results
    print("\n4. Advanced Analysis Results:")
    print("-" * 40)
    print(f"   Final Consciousness φ:      {final_metrics.phi:.6f}")
    print(f"   Global Accessibility:       {final_metrics.global_accessibility:.6f}")
    print(f"   Quantum Coherence:          {final_metrics.quantum_coherence:.6f}")
    print(f"   Hierarchical Complexity:    {final_metrics.hierarchical_complexity:.6f}")
    print(f"   Consciousness Level:        {final_metrics.consciousness_level}")
    
    # Generate comprehensive report
    print("\n5. Generating comprehensive report...")
    report = pce_system.consciousness_report()
    
    # Save advanced results
    results_path = Path("pce_advanced_results")
    results_path.mkdir(exist_ok=True)
    
    with open(results_path / "comprehensive_report.json", 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"   ✓ Comprehensive report saved to: {results_path / 'comprehensive_report.json'}")
    
    print("\nAdvanced PCE Example Complete!")


if __name__ == "__main__":
    try:
        # Run basic example
        main()
        
        # Ask user if they want to run advanced example
        print(f"\nWould you like to run the advanced example? (y/N): ", end="")
        response = input().strip().lower()
        
        if response in ['y', 'yes']:
            advanced_example()
        
    except KeyboardInterrupt:
        print("\n\nExample interrupted by user.")
    except Exception as e:
        logger.error(f"Example failed: {e}")
        print(f"\nExample failed with error: {e}")
        sys.exit(1)
