<img src="logo.png" alt="ML4VRP Logo" width="215">

# ML4VRP Competition Resources

This repository is used for the Machine Learning for Evolutionary Computation - for Vehicle Routing Problems ([ML4VRP](https://sites.google.com/view/ml4vrp)) competition in [GECCO 2023](https://gecco-2023.sigevo.org/Call-for-Competition-Entries). 

<!--This competition aims to serve as a vehicle to bring together the latest developments of machine learning-assisted evolutionary computation for vehicle routing problems (VRPs). The focus of this competition is on solving VRP with Time Window constraints (VRPTW). 

Participants must submit descriptions of the developed algorithms and the produced solutions for the corresponding VRPTW instances. Submissions of the produced solutions for the corresponding VRPTW instances will be evaluated on randomly selected instances from the provided VRPTW instances with an evaluator. The most widely adapted evaluation function, i.e. to minimise the number of vehicles and total travel distance, is used to determine the best machine learning assisted evolutionary algorithms for solving VRPs. The algorithms which produced the best average fitness for solving VRPs will receive the highest score. -->

In this repository, you will find:
- [VRPTW Problem Data](#vrps) for the competition
- [VRPTW Solution Evaluator](#api)

## <a id='vrps'>VRPTW Problem Data </a>
Solomon [Sol87] dataset and Homberger and Gehring [HG99] data set are widely studied VRPTW benchmark data sets. Both data sets consist of [six types of instances](http://web.cba.neu.edu/~msolomon/problems.htm), i.e., C1, C2, R1, R2, RC1, RC2, which differ with respect to the customers’ geographical locations, vehicle capacity, density and tightness of the time windows. 

The problem instances provided in the competition are taken from two sources, i.e., 
- Solomon [Sol87] dataset of 100 customer problems,
- Homberger and Gehring [HG99] data sets of 200 customer problems and 400 customer problems.

The provided problem instances provided are randomly selected from these three sized problem instances, covering different instance types. The competition will conduct the evaluation of the submitted solution results using a subset of the provided instances (unknown to the participants before the results are presented). 

The problem instances provided in the competition are available to download on the folder [Instances](https://github.com/ML4VRP2023/ML4VRP2023/tree/main/Instances) of this repo. All the VRPTW instances can also be found in [CVRPLIB](http://vrp.galgos.inf.puc-rio.br/index.php/en/). 

In addition to the benchmark VRPTW instances, we provide an example problem instance `toy`, locating at 
- `Instances/text/Customer6/toy.txt` and 
- `Instances/json/Customer6/toy.json`. 

### Text File Format
The text files corresponding to the problem instances can be found under the `Instances/text/` directory. Each text file is named with respect to its corresponding instance name, e.g.: the text file corresponding to problem instance **C102** is `C102.txt`, and locates at `Instances/text/Customer100/C101.txt` since the instance size (number of customers) is 100.

See [Solomon's website](http://web.cba.neu.edu/~msolomon/problems.htm) for the detailed instance description. 

<!--Below is a description of the format of the text file that defines each problem instance (assuming 100 customers).

```
<Instance name>
<empty line>
VEHICLE
NUMBER     CAPACITY
  K           Q
<empty line>
CUSTOMER
CUST NO.  XCOORD.   YCOORD.    DEMAND   READY TIME  DUE DATE   SERVICE TIME
<empty line>
    0       x0        y1         q0         e0          l0            s0
    1       x1        y2         q1         e1          l1            s1
  ...      ...       ...        ...        ...         ...           ...
  100     x100      y100       q100       e100        l100          s100
```
-->

### JSON Format
The JSON files corresponding to the problem instances can be found under the `Instances/json/` directory. Like the text files, each JSON file is named with respect to its corresponding instance name, e.g.: the JSON file corresponding to problem instance **C102** is `C102.json`, and locates at `Instances/json/Customer100/C102.json`. 

**Remarks:**
The JSON files are converted from the **text file format** by `text2json.py` Python script from the [iRB-Lab's repository](https://github.com/iRB-Lab/py-ga-VRPTW). See [iRB-Lab's repository](https://github.com/iRB-Lab/py-ga-VRPTW#json-format) for the detailed description of the JSON file format. 

## <a id='api'>VRPTW Solution Evaluator </a>
<!--http://dimacs.rutgers.edu/files/8516/3848/0275/VRPTW_Competition_Rules.pdf
https://github.com/iRB-Lab/py-ga-VRPTW-->

A Python Implementation of a solution evaluator to VRPTW. 

### How to start
Let's prepare the environment and download the resources to work.
1. Download/clone the resources in the repository. Note the `Instances/` directory where **text file format** and **JSON file format** of the problem instances are needed.
2. Install `Python 3`.
3. Install the [DEAP](https://github.com/deap/deap) framework in Python.
4. Prepare the solution files in the specific format as described in the [competition website](https://sites.google.com/view/ml4vrp#h.j2mwimqjm1ge).

The Python script `evaluator.py` is the solution evaluation program to use. The solution evaluator takes a solution and the corresponding problem instance to
- check feasibility of the solution,
- calculate the objective function value of the solution (following the objective function as stated on the [competition website](https://sites.google.com/view/ml4vrp#h.8tn33nmddfdh)) for feasible solution.

### Usage example
Navigating to the repository directory, use the following command in the terminal or command prompt:
```sh
python evaluator.py <instance_size> <instance_name> <path_to_solution_file>
```

### Example
Solutions for solving `toy` are provided in `Solutions/` directory. 
- The solution file `toy_solution.txt` gives a feasible solution (in terms of the time window and vehicle capacity constraints).
- The solution file `toy_solution_infeasible.txt` provides an invalid solution. 

#### Evaluation of feasible solutions
To evaluate `toy_solution`, run:
```sh
python evaluator.py 6 toy Solutions/toy_solution.txt
```
The output is (similar to) as shown below:
```sh
Instance size:  6  Instance name:  toy  Solution path:  toy_solution.txt
File: .../Instances/json/Customer6/toy.json exists.
Objective function value:  2153.8226859041124
Number of vehicles:  2 , Total distance:  153.82268590411263
```
#### Evaluation of infeasible solutions
To evaluate `toy_solution_infeasible`, run:
```sh
python evaluator.py 6 toy Solutions/toy_solution_infeasible.txt
```
The infeasible solution cannot pass the feasibility check, thus no objective function value will be returned. The output is (similar to) as shown below:
```sh
Instance size:  6  Instance name:  toy  Solution path:  toy_solution_infeasible.txt
File: .../Instances/json/Customer6/toy.json exists.
invalid capacity
invalid time window: too late to serve customer 6
Please upload a feasible solution!
```
## File Structure
```
├── Instances/
│   ├── json/
│   │   ├── Customer100
│   │   │   ├──<Instance name>.json
│   │   │   └── ...
│   │   ├── Customer200
│   │   │   ├──<Instance name>.json
│   │   │   └── ...
│   │   ├── Customer400
│   │   │   ├──<Instance name>.json
│   │   │   └── ...
│   ├── text/
│   │   ├── Customer100
│   │   │   ├──<Instance name>.txt
│   │   │   └── ...
│   │   ├── Customer200
│   │   │   ├──<Instance name>.txt
│   │   │   └── ...
│   │   ├── Customer400
│   │   │   ├──<Instance name>.txt
│   │   │   └── ...
├── vrptw_evaluator/
│   ├── __init__.py
│   ├── core.py
│   └── utils.py
├── evaluator.py
├── Solutions
│   ├── toy_solution.txt
│   ├── toy_solution_wrong.txt
├── requirements.txt
├── README.md
├── LICENSE
└── logo.png
```

## Organisers
Rong Qu,         University of Nottingham, UK, rong.qu@nottingham.ac.uk

Nelishia Pillay, University of Pretoria, South Africa, nelishia.pillay@up.ac.za

Weiyao Meng, University of Nottingham, UK, weiyao.meng2@nottingham.ac.uk

Please contact [Weiyao Meng](weiyao.meng2@nottingham.ac.uk) in case of any problems or if you require help for the problem instances and the solution evaluator in this repository.

## References
[HG99] J. Homberger and H. Gehring, "Two evolutionary metaheuristics for the vehicle routing problem with time windows," INFOR: Information Systems and Operational Research, 37(3):297–318, 1999. [PDF](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=a34e12bf0a30deb56233c26d82a0979987bb6ce4)

[Sol87] M. M. Solomon, "Algorithms for the vehicle routing and scheduling problems with time window constraints," Operations Research, 35(2):254–265, 1987. [PDF](https://www.jstor.org/stable/pdf/170697.pdf?casa_token=ltF2XRa2-nAAAAAA:OV4ClhhdAM_ds_p3-XIzKaz3hDYb9Jy2yHa7-jniGyYLzy2Rg2JC1b-ope2_gtsoQ1eOfFcgeTvtFmGZdPWDACEySwlfASLdRl-mhJRQE4f_6Kc5jJRnYg)