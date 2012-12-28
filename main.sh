#!/bin/bash
python download.py
cat bunsen.txt | xargs -n 1 -P 8 wget -q
