<img src="logo.png" alt="ML4VRP Logo" width="215">

# ML4VRP Competition Resources

This repository is used for the Machine Learning for Evolutionary Computation - for Vehicle Routing Problems ([ML4VRP](https://sites.google.com/view/ml4vrp)) competition in [GECCO 2023](https://gecco-2023.sigevo.org/Call-for-Competition-Entries). 

This competition aims to serve as a vehicle to bring together the latest developments of machine learning-assisted evolutionary computation for vehicle routing problems (VRPs). 

There are two tracks in this competition:
- VRP: The first track concerns the benchmark CVRP problem, a simplified scenario, and the most basic model.
- VRPTW: The second track concerns VRP with time windows, which are derived from real-world scenarios.

Participants must submit descriptions of the developed algorithms and the produced solutions for the corresponding CVRP/VRPTW instances. Submissions of the produced solutions for the corresponding CVRP/VRPTW instances will be evaluated on randomly selected instances from the benchmark VRP instances with an evaluator. The most widely adapted evaluation function, i.e. to minimise the number of vehicles and total travel distance, is used to determine the best machine learning assisted evolutionary algorithms for solving VRPs. The algorithms which produced the best average fitness for solving VRPs will receive the highest score. 

In this repository, you will find:
- [VRP Problem Data](#vrps) for the competition
- [API evaluator](#api) (available soon!)

## VRP Problem Data {#vrps}
### CVRP Instances
<!-- >> **_NOTE: about problem instances_**  
> 1. To decide which CVRP instances to include. Too many instances - too large the submission? 
> [Related competition](http://dimacs.rutgers.edu/programs/challenge/vrp/cvrp/) uses 141 instances.-->

CVRP is a well-studied variant with many instances appearing in the literature. Many diversified benchmark instances have been proposed. In this competition, a selection of CVRP instances will be used in CVRP track for algorithm evaluation. All instances can be found in [CVRPLIB](http://vrp.galgos.inf.puc-rio.br/index.php/en/). The selected CVRP instances are also available on the [Instances_CVRP folder](https://github.com/Ambergogoal/ML4VRP_resources/tree/main/Instances_CVRP) of this repo, including
- Set 1
- Set 2
- ..

CVRP instances will given in [the TSPLIB95 format](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp95.pdf). This is the format used in CVRPLIB.

### VRPTW Instances
In the VRPTW track, the competition will conduct evaluation of the submitted solution results using two classic sets of instances: 
- The 56 instances of Solomon [Sol87], each containing 100 customers.
- The 300 instances of Homberger and Gehring [HG99] ranging from 200 to 1,000 customers.

All VRPTW instances are available to download on the [Instances_VRPTW folder](https://github.com/Ambergogoal/ML4VRP_resources/tree/main/Instances_VRPTW) of this repo.

## API Evaluator {#api}
API evaluator with instructions to evaluate the solutions (available soon!)
 

## Organisers
Rong Qu,         University of Nottingham, UK, rong.qu@nottingham.ac.uk

Nelishia Pillay, University of Pretoria, South Africa, nelishia.pillay@up.ac.za

Weiyao Meng, University of Nottingham, UK, weiyao.meng2@nottingham.ac.uk


## References
[HG99] J. Homberger and H. Gehring, "Two evolutionary metaheuristics for the vehicle routing problem with time windows," INFOR: Information Systems and Operational Research, 37(3):297–318, 1999.

[Sol87] M. M. Solomon, "Algorithms for the vehicle routing and scheduling problems with time window constraints," Operations Research, 35(2):254–265, 1987.