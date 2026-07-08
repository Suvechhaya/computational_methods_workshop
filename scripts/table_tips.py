from pathlib import Path

import pandas as pd


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
tips = pd.read_csv(url)

tips["tip_percentage"] = 100 * tips["tip"] / tips["total_bill"]

Path("tables").mkdir(exist_ok=True)

table = (
    tips.groupby("size")
    .agg(
        observations=("tip_percentage", "size"),
        average_tip_percentage=("tip_percentage", "mean"),
        median_tip_percentage=("tip_percentage", "median"),
    )
    .reset_index()
)

table = table.rename(
    columns={
        "size": "Party size",
        "observations": "Observations",
        "average_tip_percentage": "Mean tip (%)",
        "median_tip_percentage": "Median tip (%)",
    }
)

table["Mean tip (%)"] = table["Mean tip (%)"].round(1)
table["Median tip (%)"] = table["Median tip (%)"].round(1)

latex_table = table.to_latex(
    index=False,
    caption="Tip percentage by party size.",
    label="tab:tips-party-size",
)

Path("tables/tips_by_party_size.tex").write_text(latex_table)

# print(table)