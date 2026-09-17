import fire
import numpy as np
import pandas as pd

DAYS_PER_MONTH = 30
DEGREE = 3


def load_feeding_plan(path="plan_pandas.csv"):
    df = pd.read_csv(path).set_index("weight")
    df.columns = df.columns.astype(int)
    return df


class FeedingPlan:
    """Query the daily feeding ration for a puppy that should reach `weight` kg."""

    def __init__(self, weight=25, path="plan_pandas.csv"):
        self.df = load_feeding_plan(path)
        self.weight = weight
        x = self.df.columns.to_numpy(dtype=float)
        y = self.df.loc[weight].to_numpy(dtype=float)
        self.coefficients = np.polyfit(x, y, DEGREE)

    def _ration(self, age_days):
        age_months = np.asarray(age_days, dtype=float) / DAYS_PER_MONTH
        return np.polyval(self.coefficients, age_months)

    def age(self, age, duration=1, export=None):
        """Print the daily ration for `age` (in days) and, optionally, the following `duration` days.

        Pass `export` with a file name (e.g. `plot.png`) to additionally save a plot of the
        best-fit feeding plan with the queried day(s) highlighted.
        """
        ages = np.arange(age, age + duration)
        rations = self._ration(ages)
        for a, ration in zip(ages, rations):
            print(f"day {a}: {ration:.1f} g")

        if export is not None:
            self._plot(export, highlight_ages=ages)

    def _plot(self, path, highlight_ages=None):
        import matplotlib.pyplot as plt

        x = self.df.columns.to_numpy(dtype=float)
        y = self.df.loc[self.weight].to_numpy(dtype=float)
        x_pred = np.linspace(x.min(), x.max(), 200)
        y_pred = np.polyval(self.coefficients, x_pred)

        fig, ax = plt.subplots()
        ax.step(x, y, where="post", marker="o", linestyle="--", label="ground truth")
        ax.plot(x_pred, y_pred, label="fitted")

        if highlight_ages is not None:
            highlight_months = np.asarray(highlight_ages, dtype=float) / DAYS_PER_MONTH
            ax.scatter(
                highlight_months,
                self._ration(highlight_ages),
                color="red",
                zorder=3,
                label="queried day(s)",
            )

        ax.set_xlabel("dog age (month)")
        ax.set_ylabel("daily ration (g)")
        ax.set_title(f"{self.weight} kg feeding plan")
        ax.legend()
        fig.savefig(path, transparent=True)
        plt.close(fig)
        print(f"saved plot to {path}")


if __name__ == "__main__":
    fire.Fire(FeedingPlan)
