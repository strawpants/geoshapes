#!/bin/python3
## script to add/update shapes in the inventroy file

import yaml
import os
import sys
import datetime

import argparse

def loadinventory(inventFile):
    #read last used settings
    if os.path.exists(inventFile):
        #Read parameters from yaml file
        with open(inventFile, 'r') as fid:
            return yaml.safe_load(fid)
    else:
        return {}

def saveinventory(inventFile,  inventory):
    with open(inventFile,'w') as fid:
        yaml.dump(inventory, fid, default_flow_style=False)

def main(argv):
    parser = argparse.ArgumentParser(description="Register/update geojson shapes in the inventory file")
    parser.add_argument("file",help="The relative link from the inventory file to the dataset")
    parser.add_argument('-d','--descr',required=True,type=str,metavar="Description",help="Provide a description of the shape")
    args = parser.parse_args(argv[1:])
    
    # load the current inventory
    inventfile="inventory.yaml"
    inventory=loadinventory(inventfile)
    
    inventory[args.file]={"Description":args.descr,"lastupdate":datetime.datetime.now()}
    

    saveinventory(inventfile,inventory)
    



if __name__ == "__main__":
    main(sys.argv)

