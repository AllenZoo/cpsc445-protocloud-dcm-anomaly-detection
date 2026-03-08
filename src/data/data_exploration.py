import scanpy as sc
import pandas as pd
from pathlib import Path

# Load the h5ad file
root = Path(__file__).resolve().parents[2]  # project root
path = root / "data" / "raw" / "hca_heart_global_ctl200723_freeze.h5ad"


adata = sc.read_h5ad(path)

print("\n=== BASIC INFO ===")
print(adata)

print("\n=== SHAPE ===")
print(f"Cells: {adata.n_obs}")
print(f"Genes: {adata.n_vars}")

print("\n=== CELL METADATA COLUMNS (obs) ===")
print(list(adata.obs.columns))

print("\n=== GENE METADATA COLUMNS (var) ===")
print(list(adata.var.columns))

print("\n=== OTHER DATA ===")
print("uns:", list(adata.uns.keys()))
print("obsm:", list(adata.obsm.keys()))
print("varm:", list(adata.varm.keys()))

print("\n=== FIRST 5 CELL IDS ===")
print(adata.obs_names[:5])

print("\n=== FIRST 5 GENE NAMES ===")
print(adata.var_names[:5])