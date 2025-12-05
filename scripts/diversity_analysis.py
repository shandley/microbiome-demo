"""Alpha and beta diversity analysis for microbiome data."""
import yaml
from pathlib import Path


def load_config():
    """Load analysis parameters."""
    config_path = Path(__file__).parent.parent / "config" / "analysis_params.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


def rarefy_samples(asv_table, rarefaction_depth=10000):
    """
    Rarefy samples to even sequencing depth.

    Rarefaction normalizes for unequal sequencing effort by
    randomly subsampling to a fixed depth.

    Args:
        asv_table: ASV count table
        rarefaction_depth: Number of reads to subsample to

    Returns:
        Rarefied ASV table
    """
    print(f"Rarefying to {rarefaction_depth} reads per sample...")
    return asv_table


def calculate_alpha_diversity(rarefied_table, metrics=None):
    """
    Calculate alpha diversity metrics.

    Alpha diversity measures within-sample diversity.

    Metrics:
        - Shannon: Accounts for richness and evenness
        - Chao1: Estimates total species richness
        - Observed OTUs: Simple richness count

    Args:
        rarefied_table: Rarefied ASV table
        metrics: List of metrics to calculate

    Returns:
        Dict of diversity values per sample
    """
    if metrics is None:
        metrics = ["shannon", "chao1", "observed_otus"]

    print(f"Calculating alpha diversity: {', '.join(metrics)}")

    # Simulated results
    results = {
        "sample1": {"shannon": 3.2, "chao1": 150, "observed_otus": 120},
        "sample2": {"shannon": 2.8, "chao1": 130, "observed_otus": 100},
    }
    return results


def calculate_beta_diversity(rarefied_table, metric="bray_curtis"):
    """
    Calculate beta diversity distance matrix.

    Beta diversity measures between-sample diversity.

    Metrics:
        - Bray-Curtis: Quantitative, abundance-weighted
        - Jaccard: Qualitative, presence/absence
        - UniFrac: Phylogenetic, requires tree
        - Weighted UniFrac: Phylogenetic + abundance

    Args:
        rarefied_table: Rarefied ASV table
        metric: Distance metric to use

    Returns:
        Distance matrix
    """
    print(f"Calculating beta diversity using {metric}...")

    # Simulated distance matrix
    return [[0, 0.3, 0.5], [0.3, 0, 0.4], [0.5, 0.4, 0]]


def run_permanova(distance_matrix, groups, permutations=999):
    """
    Run PERMANOVA test for group differences.

    PERMANOVA (Permutational Multivariate ANOVA) tests whether
    centroids and dispersion differ between groups.

    Args:
        distance_matrix: Beta diversity distances
        groups: Group assignments
        permutations: Number of permutations for p-value

    Returns:
        PERMANOVA results with F-statistic and p-value
    """
    print(f"Running PERMANOVA with {permutations} permutations...")

    # Simulated results
    return {"F_statistic": 4.2, "p_value": 0.012, "R2": 0.15}


def run_diversity_analysis():
    """Execute full diversity analysis pipeline."""
    config = load_config()

    print("=" * 50)
    print("DIVERSITY ANALYSIS")
    print("=" * 50)
    print(f"Rarefaction depth: {config['rarefaction_depth']}")
    print(f"Beta metric: {config['beta_metric']}")
    print(f"PERMANOVA permutations: {config['permanova_permutations']}")

    # Simulated ASV table
    asv_table = {"ASV1": [100, 50, 75], "ASV2": [200, 150, 180]}

    rarefied = rarefy_samples(asv_table, config["rarefaction_depth"])
    alpha = calculate_alpha_diversity(rarefied, config["alpha_metrics"])
    beta = calculate_beta_diversity(rarefied, config["beta_metric"])
    permanova = run_permanova(beta, ["treatment", "control", "treatment"],
                               config["permanova_permutations"])

    print(f"\nPERMANOVA results: F={permanova['F_statistic']}, p={permanova['p_value']}")
    return alpha, beta, permanova


if __name__ == "__main__":
    run_diversity_analysis()
