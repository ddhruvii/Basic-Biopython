# Basic-Biopython
# Foundational Bioinformatics & Computational Drug Discovery Tools

This repository contains core Python scripts designed to handle biological sequence manipulation, calculate structural metrics, and format data for Computer-Aided Drug Design (CADD) workflows. 

**The Pipeline**
1. Data Standardization: Automatically normalizes raw input sequences into uppercase format to avoid data entry mismatches.
2. GC Content Calculation: Computes the total GC%, which is crucial for determining DNA thermal stability and melting temperatures.
3. Transcription Pipeline: Simulates cellular transcription by replacing Thymine (T) bases with Uracil (U) to output exact mRNA variants.

**Core Concepts Demonstrated**
* Python string method workflows (`.upper()`, `.count()`, `.replace()`).
* Safe handling of mathematical limits (zero-division protection for empty sequence spaces).
* String formatting operations (`f-strings` restricted to two decimal places).

**Project Objective**
This repository serves as a practical showcase of my foundational coding literacy in handling dry-lab data pipelines during my M.Sc. Bioinformatics tenure.

