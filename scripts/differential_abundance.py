"""Differential abundance analysis for microbiome data."""
import yaml
from pathlib import Path


def load_config():
    """Load analysis parameters."""
    config_path = Path(__file__).parent.parent / "config" / "analysis_params.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


def filter_low_abundance(asv_table, min_prevalence=0.1, min_abundance=0.001):
    """
    Filter ASVs with low prevalence or abundance.

    Removes rare taxa that may represent sequencing errors
    or have insufficient power for statistical testing.

    Args:
        asv_table: ASV count table
        min_prevalence: Minimum fraction of samples with taxon
        min_abundance: Minimum relative abundance threshold

    Returns:
        Filtered ASV table
    """
    print(f"Filtering: prevalence >= {min_prevalence}, abundance >= {min_abundance}")
    return asv_table


def run_deseq2(counts, groups, alpha=0.05):
    """
    Run DESeq2 differential abundance analysis.

    DESeq2 uses negative binomial regression to identify
    differentially abundant taxa between conditions.

    Args:
        counts: Raw count matrix
        groups: Sample group assignments
        alpha: Significance threshold for adjusted p-values

    Returns:
        DataFrame with log2 fold changes and adjusted p-values
    """
    print(f"Running DESeq2 with alpha={alpha}...")

    # Simulated results
    results = [
        {"taxon": "Bacteroides", "log2fc": 2.1, "padj": 0.001},
        {"taxon": "Prevotella", "log2fc": -1.5, "padj": 0.02},
        {"taxon": "Akkermansia", "log2fc": 1.8, "padj": 0.003},
    ]
    return results


def run_ancom(counts, groups):
    """
    Run ANCOM differential abundance analysis.

    ANCOM (Analysis of Composition of Microbiomes) accounts
    for the compositional nature of microbiome data.

    Args:
        counts: Count matrix
        groups: Sample group assignments

    Returns:
        ANCOM results with W statistics
    """
    print("Running ANCOM analysis...")

    results = [
        {"taxon": "Bacteroides", "W": 45, "detected": True},
        {"taxon": "Faecalibacterium", "W": 38, "detected": True},
    ]
    return results


def run_aldex2(counts, groups):
    """
    Run ALDEx2 differential abundance analysis.

    ALDEx2 uses centered log-ratio transformation and
    models per-feature technical variation.

    Returns:
        ALDEx2 effect sizes and p-values
    """
    print("Running ALDEx2 analysis...")
    return []


def run_differential_analysis():
    """Execute differential abundance pipeline."""
    config = load_config()

    print("=" * 50)
    print("DIFFERENTIAL ABUNDANCE ANALYSIS")
    print("=" * 50)
    print(f"Method: {config['differential_method']}")
    print(f"Significance threshold: {config['significance_threshold']}")
    print(f"Min prevalence: {config['min_prevalence']}")

    # Simulated data
    asv_table = {"ASV1": [100, 50, 75], "ASV2": [200, 150, 180]}
    groups = ["treatment", "control", "treatment"]

    filtered = filter_low_abundance(
        asv_table,
        config["min_prevalence"],
        config["min_abundance"]
    )

    method = config["differential_method"]
    if method == "deseq2":
        results = run_deseq2(filtered, groups, config["significance_threshold"])
    elif method == "ancom":
        results = run_ancom(filtered, groups)
    elif method == "aldex2":
        results = run_aldex2(filtered, groups)
    else:
        raise ValueError(f"Unknown method: {method}")

    sig_taxa = [r for r in results if r.get("padj", 0) < config["significance_threshold"]
                or r.get("detected", False)]
    print(f"\nFound {len(sig_taxa)} differentially abundant taxa")

    return results


if __name__ == "__main__":
    run_differential_analysis()
