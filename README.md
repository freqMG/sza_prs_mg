# sza_prs_mg

A modular pipeline for calculating polygenic risk scores (PRS), percentile ranking, and relative risk estimation using Plink2 and GWAS-derived score files. This repository is customized for PRS analysis in, using both individual sample VCFs and 1000 Genomes reference data.

## Features

- Biallelic filtering and variant ID normalization (Plink2)
- PRS scoring using harmonized GWAS Catalog files
- Percentile and relative risk estimation in Python
- Compatible with custom pipelines or workflow tools (Nextflow/Snakemake-ready)

## Directory structure

- `data/`: Contains example input files
- `scripts/`: Shell and Python scripts for preprocessing and analysis
- `results/`: Example outputs
- `requirements.txt`: Required Python packages
- `README.md`: This documentation

