library(anndata)
library(Seurat)

load("GSE183852_DCM_Cells.Robj")

gene_names <- rownames(HDCM@assays$RNA@counts)

adata_r <- AnnData(
  X = t(HDCM@assays$RNA@counts), 
  obs = HDCM@meta.data,
  var = data.frame(gene_symbol = gene_names, row.names = gene_names)
)

write_h5ad(adata_r, "GSE183852_cleaned.h5ad")
