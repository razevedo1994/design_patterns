import json
from datetime import datetime
import pandas as pd


class MessySalesReport:
    def generate(
        self,
        input_file: str,
        output_file: str,
        start_date: datetime | None = None,
        end_date: datetime | None = None,
    ) -> None:
        df = pd.read_csv(input_file, parse_dates=["date"])

        if start_date:
            df = df[df["date"]] >= pd.Timestamp(start_date)
        if end_date:
            df = df[df["date"]] <= pd.Timestamp(end_date)
