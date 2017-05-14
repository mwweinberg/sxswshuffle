
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




print(f"shared: {shared}")
print(f"input1_only: {input1_only}")
print(f"input2_only: {input2_only}")



#TODO: compare files in input2 to the lists and copy accordingly

for root, dirs, files in os.walk("input2", topdown=False):
    for filename in files:
        print(filename)
        if filename in input2_only:
            print('yay')
            out = "outputs/" + filename
            shutil.copy(os.path.join(root, filename), out)


# for file in directory:
    #if file in shared:
        #copy file to /shared
    #elif file in input1_only:
        #copy file to /input1_only
    #elif file in input2_only:
        #copy file to /input2_only
    #else:
        #print("error")

#TODO: rewrite mp3 tags
