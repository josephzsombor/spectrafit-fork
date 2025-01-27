"""Tools for generating spectra for testing."""
import math

from pathlib import Path

import numpy as np
import pandas as pd
import scipy.stats as stats


def double_peak(fname: str) -> None:
    """Generate a spectrum with two Gaussian peaks.

    Args:
        fname (str): The file name of the `csv` file to write.
    """
    variance = 1
    sigma = math.sqrt(variance)
    x = np.linspace(0, 10, 100)
    pd.DataFrame(
        {
            "energy": x,
            "y_1": stats.norm.pdf(x, 1, sigma) + 0.75 * stats.norm.pdf(x, 5, sigma),
            "y_2": stats.norm.pdf(x, 1, sigma)
            + np.random.rand(100) / 10.0
            + 0.75 * stats.norm.pdf(x, 5, sigma)
            + np.random.rand(100) / 10.0,
            "y_3": stats.norm.pdf(x, 1, sigma)
            + np.random.rand(100) / 100.0
            + 0.75 * stats.norm.pdf(x, 5, sigma)
            + np.random.rand(100) / 100.0,
        }
    ).to_csv(Path(fname), index=False)


if __name__ == "__main__":
    """Start Generator."""
    double_peak("double_peak.csv")
