"""Fetch the CERES explorer's zarr arrays (clim for all bases, map year-chunks for a few bases/years) into the mirror.

Run:  .venv/bin/python -I scripts/fetch_ceres_zarr.py
Only fetches URLs under joymonteiro.github.io/intro_climate_science/tutorials/ceres-energy-budget/ ; the downloaded files are
untrusted data and are only ever decoded as int16 arrays (gzip + numpy), never executed.
"""
import json
import os
import urllib.request

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MIRROR = os.path.join(ROOT, "earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/tutorials/ceres-energy-budget/assets/data")
BASE = "https://joymonteiro.github.io/intro_climate_science/tutorials/ceres-energy-budget/assets/data/"

fields = json.load(open(os.path.join(MIRROR, "fields.json")))
bases = list(fields["base"].keys())
MAP_BASES = ["toa_sw_all", "toa_lw_all", "toa_net_all", "toa_sw_clr", "toa_lw_clr"]
MAP_YEARS = [2010, 2011, 2015, 2016, 2020, 2021, 2023, 2024]


def get(rel):
    dst = os.path.join(MIRROR, rel)
    if os.path.exists(dst):
        return dst
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    req = urllib.request.Request(BASE + rel, headers={"User-Agent": "course-notes-fetch/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    open(dst, "wb").write(data)
    return dst


n = 0
for b in bases:
    get(f"ceres.zarr/clim/{b}/zarr.json")
    get(f"ceres.zarr/clim/{b}/c/0/0/0")
    n += 2
for b in MAP_BASES:
    get(f"ceres.zarr/map/{b}/zarr.json")
    for y in MAP_YEARS:
        get(f"ceres.zarr/map/{b}/c/{y - 2010}/0/0")
        n += 1
# zonal series (small JSON), if present
for z in ["asr", "olr", "toa_net", "solar", "toa_cre_net", "toa_cre_sw", "toa_cre_lw"]:
    try:
        get(f"series/zonal/{z}.json")
        n += 1
    except Exception as e:  # not every id exists
        print("skip zonal", z, type(e).__name__)
print("fetched/present:", n)
