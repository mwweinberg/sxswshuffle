#input folders need to be
#michael_input and jessica_input
#you also need to create michael_out and jessica_out before running



import glob
import os
import shutil
import eyed3

#lists for the file names
michael_input_only = []
jessica_input_only = []
shared = []





#######################
####create list of file names
###########################

#turns all of the mp3 files in the input1 dir into a list
michael_input = glob.glob('michael_input/*.mp3')
#removes the directory heading from each entry in the list
michael_input_cleaned = ([s.strip('michael_input/') for s in michael_input])

#turns all of the mp3 files in the input1 dir into a list
jessica_input = glob.glob('jessica_input/*.mp3')
#removes the directory heading from each entry in the list
jessica_input_cleaned = ([s.strip('jessica_input/') for s in jessica_input])

#########################
####Sort file names into lists
###########################

#analyize input1
#for the first one you need to add files to the shared folder too
for root, dirs, files in os.walk("michael_input", topdown=False):
    #for each file in input1
    for name in files:
        #see if it is in input2_cleaned
        if name in jessica_input_cleaned:
            #if it is addit to shared
            shared.append(name)
        else:
            #if it isn't add it to input1_only
            michael_input_only.append(name)

#analyize input2
#since shared is already built, only need to copy input2_only
for root, dirs, files in os.walk("jessica_input", topdown=False):
    #for each file in input2
    for name in files:
        #see if it is in input1_cleaned
        if name not in michael_input_cleaned:
            jessica_input_only.append(name)


#############################
#####Sort files
##############################

#compares files against the lists and copies accordingly
#for files in input 1
for root, dirs, files in os.walk("michael_input", topdown=False):
    for filename in files:
        #if the file shows up in the input1_only list
        if filename in michael_input_only:
            #this creates the output filename (includes director)
            michael_out = "michael_out/" + filename
            #copies the file to the target
            shutil.copy(os.path.join(root, filename), michael_out)
        #same thing for files in the shared list
        elif filename in shared:
            shared_out = "shared_out/" + filename
            shutil.copy(os.path.join(root, filename), shared_out)
        #error message
        else:
            print(f"There was an error with {filename}")

for root, dirs, files in os.walk("jessica_input", topdown=False):
    for filename in files:
        if filename in jessica_input_only:
            jessica_out = "jessica_out/" + filename
            shutil.copy(os.path.join(root, filename), jessica_out)
        #this may not be necessary
        #it doesn't appear to double copy, but if it does just cut it
        elif filename in shared:
            shared_out = "shared_out/" + filename
            shutil.copy(os.path.join(root, filename), shared_out)
        else:
            print(f"There was an error with {filename}")


###############################
############rewrite mp3 album tags
#################################

#loads the cover art
imagedata = open("sxsw2016.jpg", "rb").read()

#rename the album for Jessica only files
for root, dirs, files in os.walk("jessica_out/", topdown=False):
    for filename in files:
        #create the name of the file that includes the dir and the filename
        alt_name = "jessica_out/" + filename
        #create teh eyed3 object based on that file name
        new_audio = eyed3.load(alt_name)
        #rewrite the audio tag
        new_audio.tag.album = u"SXSW 2016 Showcasing Artist (Jessica)"
        #add the cover art
        #3 is front image, imagedata is the image object from above, image/png is mime type
        new_audio.tag.images.set(3,imagedata,"image/jpeg")
        #save the change
        new_audio.tag.save()

#rename the album for Michael only files
for root, dirs, files in os.walk("michael_out/", topdown=False):
    for filename in files:
        alt_name = "michael_out/" + filename
        new_audio = eyed3.load(alt_name)
        new_audio.tag.album = u"SXSW 2016 Showcasing Artist (Michael)"
        new_audio.tag.save()
