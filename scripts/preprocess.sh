#!/bin/bash

# Exit immediately if a command fails
set -e

# Input VCF (bgzipped and indexed)
VCF_INPUT=$1     # Example: data/1000g_chr1_22.vcf.gz
OUT_PREFIX=$2    # Example: data/1000g_pgen

if [ -z "$VCF_INPUT" ] || [ -z "$OUT_PREFIX" ]; then
  echo "Usage: bash preprocess.sh <input.vcf.gz> <out_prefix>"
  exit 1
fi

echo "Step 1: Filtering biallelic SNPs..."
bcftools view -m2 -M2 -v snps -Oz -o ${OUT_PREFIX}.biallelic.vcf.gz $VCF_INPUT
tabix -p vcf ${OUT_PREFIX}.biallelic.vcf.gz

echo "Step 2: Converting to PLINK2 format and normalizing IDs..."
plink2 \
  --vcf ${OUT_PREFIX}.biallelic.vcf.gz \
  --make-pgen \
  --set-all-var-ids '@:#:$r' \
  --new-id-max-allele-len 1010 \
  --out ${OUT_PREFIX}

echo "Preprocessing completed."
