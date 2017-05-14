
import glob
import os
import shutil


input1_only = []
input2_only = []
shared = []



#######################
####create list of file names
###########################

#turns all of the mp3 files in the input1 dir into a list
input1 = glob.glob('input1/*.mp3')
#removes the directory heading from each entry in the list
input1_cleaned = ([s.strip('input1/') for s in input1])

#turns all of the mp3 files in the input1 dir into a list
input2 = glob.glob('input2/*.mp3')
#removes the directory heading from each entry in the list
input2_cleaned = ([s.strip('input2/') for s in input2])

#########################
####Sort file names into lists

#analyize input1
#for the first one you need to add files to the shared folder too
for root, dirs, files in os.walk("input1", topdown=False):
    #for each file in input1
    for name in files:
        #see if it is in input2_cleaned
        if name in input2_cleaned:
            #if it is addit to shared
            shared.append(name)
        else:
            #if it isn't add it to input1_only
            input1_only.append(name)

#analyize input2
#since shared is already built, only need to copy input2_only
for root, dirs, files in os.walk("input2", topdown=False):
    #for each file in input2
    for name in files:
        #see if it is in input1_cleaned
        if name not in input1_cleaned:
            input2_only.append(name)


#############################
#####Sort files
##############################

#compares files against the lists and copies accordingly
#for files in input 1
for root, dirs, files in os.walk("input1", topdown=False):
    for filename in files:
        #if the file shows up in the input1_only list
        if filename in input1_only:
            #this creates the output filename (includes director)
            in1_outs = "in1_outputs/" + filename
            #copies the file to the target
            shutil.copy(os.path.join(root, filename), in1_outs)
        #same thing for files in the shared list
        elif filename in shared:
            shared_out = "shared_out/" + filename
            shutil.copy(os.path.join(root, filename), shared_out)
        #error message
        else:
            print(f"There was an error with {filename}")

for root, dirs, files in os.walk("input2", topdown=False):
    for filename in files:
        if filename in input2_only:
            in2_outs = "in2_outputs/" + filename
            shutil.copy(os.path.join(root, filename), in2_outs)
        #this may not be necessary
        #it doesn't appear to double copy, but if it does just cut it
        elif filename in shared:
            shared_out = "shared_out/" + filename
            shutil.copy(os.path.join(root, filename), shared_out)


#TODO: rewrite mp3 tags
