#!/usr/bin/env bash
#
#
# mamba dies doing r-plotly
conda create --prefix=conda/r-ggplot2-plotly R r-ggplot2 r-plotly --solver=classic

