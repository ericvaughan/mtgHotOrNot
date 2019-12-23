#!/usr/bin/env python3
import json
import os
from typing import Dict
import argparse

import ingester
import card_ui

script_dir = os.path.dirname(os.path.abspath(__file__))

def gen_cfg() -> Dict[str, str]:
    cfg = {}
    cfg["images_dir"] = os.path.join(script_dir, "images")
    cfg["data_file"] = os.path.join(script_dir, "data.json")
    return cfg

def load_cfg() -> Dict[str, str]:
    cfg_name = "settings.json"
    if os.path.isfile(os.path.join(script_dir, cfg_name)):
        cfg = json.load(cfg_name)
    else:
        cfg = gen_cfg()     

    return cfg

def setup_dirs(cfg: Dict[str, str]) -> None:
    if not os.path.isdir(cfg["images_dir"]):
        os.mkdir(cfg["images_dir"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hot Or Not ranking tool for your cube")
    parser.add_argument("--load_list", type=str, help="List of cards to be loaded")
    parser.add_argument("--rank")
    
    args = parser.parse_args()

    # Try to load settings file, if not exist, then create one
    cfg = load_cfg()
    
    # Check env against the cfg
    setup_dirs(cfg)

    # Ingest card list and download images
    ingester.load_list(cfg, args.load_list) 
