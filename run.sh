#!/bin/bash
valgrind --tool=callgrind --instr-atstart=no sage bench.py
