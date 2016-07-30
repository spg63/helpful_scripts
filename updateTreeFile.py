#!/usr/bin/env python
#
# Makes use of the "tree" scripts, creates a tree file, then reads the file in and removes 
# lines that *I* don't care about and re-writes the file. This could be customized to ignore 
# any types of files one wishes
#
# Sean Grimes

import os
import sys
import subprocess

def update_tree():
    tree_file = os.getcwd() + "/" + "_tree.txt"
    f = open(tree_file, "w")
    subprocess.call("tree", shell=True, stdout=f)
    f.close()
    flines = []
    finalized = []
    with open(tree_file) as f:
        flines = f.readlines()
    
    skip_these = []
    skip_these.append(".DocumentRev")
    skip_these.append("reverseStore")
    skip_these.append("tmp.SnowLeo")
    skip_these.append(".TemporaryItems")
    skip_these.append("folders.0")
    skip_these.append(".DS_Store")
    skip_these.append(".Spotlight-V")
    skip_these.append(".Trashes")
    skip_these.append("fseventsd")
    skip_these.append("870048A9")
    skip_these.append("Store-V")
    skip_these.append("journalAttr")
    skip_these.append("6DCD")
    skip_these.append("000000000")
    skip_these.append("VolumeConfig")
    skip_these.append("store.db")
    skip_these.append("0.directory")
    skip_these.append("0.index")
    skip_these.append("0.shadow")
    skip_these.append("Cab.")
    skip_these.append("indexState")
    skip_these.append("journalE")
    skip_these.append("journals.")
    skip_these.append("retire.")
    skip_these.append("Lion.")
    skip_these.append("live.0.")
    skip_these.append("live.1.")
    skip_these.append("live.2.")
    skip_these.append("live.3.")
    skip_these.append("permStore")
    skip_these.append("reverseDir")
    skip_these.append("reverseDirectory")
    skip_these.append("shutdown_time")
    skip_these.append("store.updates")
    skip_these.append("store_generation")
    skip_these.append("tmp.Cab")
    skip_these.append("tmp.Lion")
    skip_these.append("tmp.snowLeopard")
    skip_these.append("tmp.spotlight.")
    skip_these.append("VolumeCon")
    skip_these.append(".md5")
    skip_these.append("_tree")
    skip_these.append(".swp")

    for line in flines:
        finalized.append(line)
        for skip in skip_these:
            if skip in line:
                try:
                    finalized.remove(line)
                except:
                    pass
    


    f = open(tree_file, "w")        
    for line in finalized:
        f.write("%s" % line)


if __name__ == "__main__":
    update_tree()
