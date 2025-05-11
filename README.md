# Analysis of the SAT Algorithms

This respository contains the implementation of the SAT algorithms(propositional resolution, DP, DPLL), which solve the SAT problem of a formula in CNF and analysis of efficiency and performance when the formula is becoming larger and more complex.

## 📌 Project Overview
This project analyzes the efficiency of different **SAT-solving algorithms**, including:
- **Resolution Algorithm**
- **Davis-Putnam Algorithm**
- **Davis-Putnam-Logemann-Loveland (DPLL) Algorithm**
  
The goal is to compare their **execution times**, **scalability**, and **performance** on various datasets.

## 📊 Algorithms Implemented
- **Resolution Algorithm**

- **Davis-Putnam Algorithm**

- **Davis-Putnam-Logemann-Loveland Algorithm**

## 📈 Performance Analysis
The project includes execution time comparisons for different datasets:

Small datasets (few clauses, few literals)

Medium datasets (thousands of clauses)

Large datasets (tens of thousands of clauses)

### **Example Results**
| Algorithm       | Small Dataset | Medium Dataset | Large Dataset |
|----------------|--------------|---------------|--------------|
| Resolution     | 0.5s         | 3.2s          | 15.8s        |
| Davis-Putnam   | 0.3s         | 2.1s          | 10.5s        |
| DPLL           | 0.1s         | 1.6s          | 6.8s         |

## Repository structure 
- 📂 Analysis-of-the-SAT-algorithms/
  - 📁 analysis/                    ( Contains scripts for running and analyzing SAT algorithms )
    - 📁 test_data/                 ( Contains test datasets used for evaluation )
      - 📝 clauzemici.csv           ( Small dataset (few clauses, few literals) )
      - 📝 clauzemedii.csv          ( Medium dataset (thousands of clauses) )
      - 📝 clauzemari.csv           ( Large dataset (tens of thousands of clauses) )
    - 🟥 resolution.py              ( Resolution-based SAT solver )
    - 🔵 davisputnam.py             ( Davis-Putnam SAT solver )
    - 🟢 davisputnamll.py           ( Davis-Putnam-Logemann-Loveland (DPLL) SAT solver )



