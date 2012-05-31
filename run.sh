#!/bin/bash
rm callgrind*
valgrind --tool=callgrind --instr-atstart=no --trace-children=yes sage bench.py
