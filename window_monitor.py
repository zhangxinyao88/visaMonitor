#!/usr/bin/env python3
"""Add an optional inclusive lower bound to visaMonitor alert runs."""

import datetime as dt
import os

import monitor


def _install_start_filter() -> None:
    raw_start = os.environ.get("VISA_START", "").strip()
    if not raw_start:
        return
    start = dt.date.fromisoformat(raw_start)
    original_find_matches = monitor.find_matches

    def find_matches_in_window(data: dict, today: dt.date, cutoff: dt.date) -> list[dict]:
        matches = original_find_matches(data, today, cutoff)
        in_window = []
        for match in matches:
            dates = [date for date in match["dates"] if dt.date.fromisoformat(date) >= start]
            if dates:
                in_window.append({**match, "dates": dates})
        return in_window

    monitor.find_matches = find_matches_in_window


if __name__ == "__main__":
    _install_start_filter()
    monitor.main()
