<img src="logo.png" alt="ML4VRP Logo" width="215">

# ML4VRP Competition Resources

This repository is used for the Machine Learning for Evolutionary Computation - for Vehicle Routing Problems ([ML4VRP](https://sites.google.com/view/ml4vrp)) competition in [GECCO 2023](https://gecco-2023.sigevo.org/Call-for-Competition-Entries). 

<!--This competition aims to serve as a vehicle to bring together the latest developments of machine learning-assisted evolutionary computation for vehicle routing problems (VRPs). The focus of this competition is on solving VRP with Time Window constraints (VRPTW). 

Participants must submit descriptions of the developed algorithms and the produced solutions for the corresponding VRPTW instances. Submissions of the produced solutions for the corresponding VRPTW instances will be evaluated on randomly selected instances from the provided VRPTW instances with an evaluator. The most widely adapted evaluation function, i.e. to minimise the number of vehicles and total travel distance, is used to determine the best machine learning assisted evolutionary algorithms for solving VRPs. The algorithms which produced the best average fitness for solving VRPs will receive the highest score. -->

In this repository, you will find:
- [VRP Problem Data](#vrps) for the competition
- [API evaluator](#api) (available soon!)

## <a id='vrps'>VRP Problem Data </a>
The competition will conduct evaluation of the submitted solution results using two classic sets of VRPTW instances: 
- The 56 instances of Solomon [Sol87], each containing 100 customers.
- The 120 instances of Homberger and Gehring [HG99], ranging from 200 to 400 customers.

All VRPTW instances are available to download on the folder [Instances](https://github.com/Ambergogoal/ML4VRP_resources/tree/main/Instances_VRPTW) of this repo.

## <a id='api'>API Evaluator </a>
API evaluator with instructions to evaluate the solutions will be available soon!
 

## Organisers
Rong Qu,         University of Nottingham, UK, rong.qu@nottingham.ac.uk

Nelishia Pillay, University of Pretoria, South Africa, nelishia.pillay@up.ac.za

Weiyao Meng, University of Nottingham, UK, weiyao.meng2@nottingham.ac.uk


## References
[HG99] J. Homberger and H. Gehring, "Two evolutionary metaheuristics for the vehicle routing problem with time windows," INFOR: Information Systems and Operational Research, 37(3):297–318, 1999.

[Sol87] M. M. Solomon, "Algorithms for the vehicle routing and scheduling problems with time window constraints," Operations Research, 35(2):254–265, 1987.