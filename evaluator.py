#!/usr/bin/env python
# coding: utf-8

# In[2]:


# -*- coding: utf-8 -*-

'''sample_C1_4_3.py'''

from vrptw_evaluator.core import run_solution_evaluator
import sys

def main(instance_size,instance_name,solution_path):
    '''main()'''
    solution = "Solution/Customer"+str(instance_size)+"/"+instance_name+".txt"

    
    feasibility, objective, nv, td = run_solution_evaluator(instance_name=instance_name, instance_size = instance_size, solution_path=solution_path)
    if(feasibility == 1):
        print("Objective function value: ", objective)
        print("Number of vehicles: ", nv, ", Total distance: ", td)
    else:
        print("Please upload a valid solution!")
if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Error: Please provide arguments as stated in README.")
        sys.exit()
    param_1 = sys.argv[1]
    param_2 = sys.argv[2]
    param_3 = sys.argv[3]
    if not param_1.isdigit():
        print("Error: The instance size must be an integer.")
        sys.exit()
    if not param_3.endswith(".txt"):
        print("Error: The solution path must end with '.txt'.")
        sys.exit()
    print('Instance size: ', param_1, " Instance name: ",param_2, " Solution path: ",param_3)
    main(instance_size=param_1,instance_name=param_2, solution_path=param_3)
