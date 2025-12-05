# Gut Microbiome Diversity Study

16S rRNA analysis pipeline for comparing gut microbiome composition between treatment and control groups.

## Analysis Pipeline

1. **Preprocessing** (`scripts/preprocess.py`)
   - Quality filtering with Phred scores
   - DADA2 denoising to generate ASVs
   - Taxonomy assignment via SILVA

2. **Diversity Analysis** (`scripts/diversity_analysis.py`)
   - Rarefaction for normalization
   - Alpha diversity (Shannon, Chao1)
   - Beta diversity (Bray-Curtis)
   - PERMANOVA statistical testing

3. **Differential Abundance** (`scripts/differential_abundance.py`)
   - DESeq2/ANCOM/ALDEx2 methods
   - Multiple testing correction

## Configuration

All parameters are in `config/analysis_params.yaml`.

## Running

```bash
python scripts/preprocess.py
python scripts/diversity_analysis.py
python scripts/differential_abundance.py
```

## LabWeave Integration

This project is monitored by LabWeave for:
- Parameter change tracking
- Method usage detection
- Daily research insights
