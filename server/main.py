
######################################
# Object Processing                  #
# MD MEZBAH UDDIN                    #
# Nantong University(China)          #
# CSE                                #
#                                    #
######################################

import glob
import shutil
import os

source_path = '../source/*'
destination_path = '../destination'

postfix = [1,2,3]

#usubg while loop
while True:

    #without while loop
    source_object = glob.glob(source_path)
    # print(source_object)

    if len(source_object) > 0:
        object_path = source_object[0]
        # print(object_path)

        shutil.copy(object_path,'.')



        object_name = object_path.split('\\')[-1].split('.')
        # print(object_name)
        prifix=object_name[0]
        postfix2=object_name[1]
        # print(prifix)
        # print(postfix2)
        # print(object_name)

        for item in range(len(postfix)):
            # print(item)
            filename = prifix + '_' + str(item) + '.' + postfix2
            # print(filename)
            # shutil.copy(object_path,filename) #add txt file
            shutil.copy(object_path,f"{destination_path}/{filename}")

        os.remove(object_path)

        os.remove(object_path.split('\\')[-1])

