"""Working with module pandas."""

import re
from re import Pattern

# +
from typing import Callable, cast

import numpy as np
import pandas as pd
from pandas import DataFrame as PdDataFrame
from pandas import Series as PdSeries


def _tokenize_lower(source_text: str) -> list[str]:
    """Return lowercased words without punctuation and digits."""
    clean_pattern: Pattern[str] = re.compile(r"[^A-Za-zА-Яа-яЁё\s]+")
    normalized_text: str = clean_pattern.sub(" ", source_text.lower())
    return [word for word in normalized_text.split() if word]


def length_stats(text: str) -> PdSeries[int]:
    """Return Series with unique words as index and their lengths as values."""
    words_sorted: list[str] = sorted(set(_tokenize_lower(text)))
    lengths: list[int] = [len(word) for word in words_sorted]
    return cast(
        PdSeries[int],
        pd.Series(lengths, index=words_sorted, dtype=np.int64),
    )


# +
def _normalize_words_v2(text: str) -> list[str]:
    """Return sorted unique lowercase words; strip digits and punctuation."""
    normalized: str = "".join(ch if (ch.isalpha() or ch == " ") else " " for ch in text)
    return sorted(set(normalized.lower().split()))


def length_stats_v2(text: str) -> "tuple[PdSeries[int], PdSeries[int]]":
    """Return two Series: (odd, even) word-length stats from text."""
    words: list[str] = _normalize_words_v2(text)
    base = pd.Series([len(word) for word in words], index=words, dtype="int64")
    odd = cast("PdSeries[int]", base[base % 2 == 1])
    even = cast("PdSeries[int]", base[base % 2 == 0])
    return odd, even


# -


def cheque(price_list: "PdSeries[int]", **purchases: int) -> "PdDataFrame":
    """Return receipt DataFrame sorted by name."""
    product_names: list[str] = sorted(purchases)
    unit_prices: list[int] = [int(price_list.at[name]) for name in product_names]
    quantities: list[int] = [purchases[name] for name in product_names]
    costs: list[int] = [price * qty for price, qty in zip(unit_prices, quantities)]
    receipt = pd.DataFrame(
        {
            "product": product_names,
            "price": unit_prices,
            "number": quantities,
            "cost": costs,
        }
    )
    return receipt.sort_values("product").reset_index(drop=True)


# +
def cheque_v2(price_list: "PdSeries[int]", **purchases: int) -> "PdDataFrame":
    """Build sorted receipt DataFrame from price list and purchases."""
    product_names: list[str] = sorted(purchases)
    unit_prices: list[int] = [int(price_list.at[name]) for name in product_names]
    quantities: list[int] = [purchases[name] for name in product_names]
    costs: list[int] = [price * qty for price, qty in zip(unit_prices, quantities)]
    receipt = pd.DataFrame(
        {
            "product": product_names,
            "price": unit_prices,
            "number": quantities,
            "cost": costs,
        }
    )
    return receipt.sort_values("product").reset_index(drop=True)


def discount_v2(receipt: "PdDataFrame") -> "PdDataFrame":
    """Apply 50% discount where quantity > 2 and return a copy."""
    discounted = receipt.copy()
    mask = discounted["number"] > 2
    discounted.loc[mask, "cost"] = discounted.loc[mask, "cost"] / 2
    return discounted


# -


def get_long(data: "PdSeries[int]", min_length: int = 5) -> "PdSeries[int]":
    """Return items whose values are >= min_length."""
    return data[data >= min_length]


def best(journal: "PdDataFrame") -> "PdDataFrame":
    """Return rows where maths, physics, and computer science > 3."""
    frame: "PdDataFrame" = journal.copy()
    maths_ok = frame["maths"] > 3
    physics_ok = frame["physics"] > 3
    cs_ok = frame["computer science"] > 3
    passed_mask = maths_ok & physics_ok & cs_ok
    return frame[passed_mask]


def need_to_work_better(journal: "PdDataFrame") -> "PdDataFrame":
    """Return rows where any of maths, physics, CS is < 3."""
    frame: "PdDataFrame" = journal.copy()
    maths_bad = frame["maths"] < 3
    physics_bad = frame["physics"] < 3
    cs_bad = frame["computer science"] < 3
    need_mask = maths_bad | physics_bad | cs_bad
    return frame[need_mask]


def update(journal: "PdDataFrame") -> "PdDataFrame":
    """Add 'average' and sort by average desc, then name asc."""
    updated: "PdDataFrame" = journal.copy()
    subjects: list[str] = ["maths", "physics", "computer science"]
    updated["average"] = updated[subjects].mean(axis=1)
    return updated.sort_values(["average", "name"], ascending=[False, True])


# +
x_left, y_top = map(int, input().split())
x_right, y_bottom = map(int, input().split())

x_min, x_max = sorted((x_left, x_right))
y_min, y_max = sorted((y_bottom, y_top))

data2 = pd.read_csv("data.csv")
x_ok = (data2["x"] >= x_min) & (data2["x"] <= x_max)
y_ok = (data2["y"] >= y_min) & (data2["y"] <= y_max)

print(data2[x_ok & y_ok])


def values(
    func: "Callable[[float], float]",
    start: float,
    end: float,
    step: float,
) -> "PdSeries[float]":
    """Return Series of func(x) for x in [start, end] with given step."""
    index_array = np.arange(start, end + step, step, dtype=float)
    values_list: list[float] = [func(float(value)) for value in index_array]
    return pd.Series(values_list, index=index_array, dtype="float64")


def min_extremum(data: "PdSeries[float]") -> float:
    """Return the smallest index where the minimum value occurs."""
    return float(data.idxmin())


def max_extremum(data: "PdSeries[float]") -> float:
    """Return the largest index where the maximum value occurs."""
    max_value: float = float(data.max())
    mask = data == max_value
    return float(data.index[mask].max())
