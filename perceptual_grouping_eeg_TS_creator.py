#beta 0.2


import csv
import numpy as np
import pickle
import os
import param_perceptual_grouping_eeg as param

#get the subjects metadata from the subjectsorigin.csv and convert them into a list
with open  ('subjectsorigin.csv', 'rb') as g:
    subjectdata = list(csv.reader(g))
 
#get the trials metadata from the trialsorigin.csv and convert them into a list        
with open  ('trialsorigin.csv', 'rb') as g:
    trialsdata = list(csv.reader(g))
    trialsdata = [map(int, x) for x in trialsdata]

#get a list of all raw data files
files = [os.path.join(root, name)
             for root, dirs, files in os.walk('rawdata')
             for name in files]

#list for trials.csv
csvrow = []
#adding header with the columns: subjectid, trial, gender, age, WM, posture, Dual_task, trialcomplete, samples  
csvrow.append([subjectdata[0][1], 'trial',subjectdata[0][2],subjectdata[0][3],subjectdata[0][4],subjectdata[0][5], 
               param.conditionnames[0], param.conditionnames[1],param.conditionnames[2],param.conditionnames[3],param.conditionnames[4],
               param.conditionnames[5],param.conditionnames[6],param.conditionnames[7],'trialtype','eyeblink','artefact','mouseclock'])
trialcount = 1  
for subjectnumber in range(1, (len(param.subjects)+1)):
    for conditionnumber in range(1, (len(param.conditions)+1)):
        #print subjectnumber, ',' ,conditionnumber
        if conditionnumber not in [7,8]:
            for trialnumbers in range(len(trialsdata)):
                if (trialsdata[trialnumbers][0] == subjectnumber) and (trialsdata[trialnumbers][1] == conditionnumber):
                    if conditionnumber == 1:
                        csvrow.append([subjectdata[subjectnumber][1], trialcount,subjectdata[subjectnumber][2],subjectdata[subjectnumber][3],
                                       subjectdata[subjectnumber][4],subjectdata[subjectnumber][5], 1,0,0,0,0,0,0,0,trialsdata[trialnumbers][3],
                                       trialsdata[trialnumbers][4], trialsdata[trialnumbers][5], trialsdata[trialnumbers][6]])
                        trialcount+=1
                    if conditionnumber == 2:
                        csvrow.append([subjectdata[subjectnumber][1], trialcount,subjectdata[subjectnumber][2],subjectdata[subjectnumber][3],
                                       subjectdata[subjectnumber][4],subjectdata[subjectnumber][5], 0,1,0,0,0,0,0,0,trialsdata[trialnumbers][3],
                                       trialsdata[trialnumbers][4], trialsdata[trialnumbers][5], trialsdata[trialnumbers][6]])
                        trialcount+=1
                    if conditionnumber == 3:
                        csvrow.append([subjectdata[subjectnumber][1], trialcount,subjectdata[subjectnumber][2],subjectdata[subjectnumber][3],
                                       subjectdata[subjectnumber][4],subjectdata[subjectnumber][5], 0,0,1,0,0,0,0,0,trialsdata[trialnumbers][3],
                                       trialsdata[trialnumbers][4], trialsdata[trialnumbers][5], trialsdata[trialnumbers][6]])
                        trialcount+=1
                    if conditionnumber == 4:
                        csvrow.append([subjectdata[subjectnumber][1], trialcount,subjectdata[subjectnumber][2],subjectdata[subjectnumber][3],
                                       subjectdata[subjectnumber][4],subjectdata[subjectnumber][5], 0,0,0,1,0,0,0,0,trialsdata[trialnumbers][3],
                                       trialsdata[trialnumbers][4], trialsdata[trialnumbers][5], trialsdata[trialnumbers][6]])
                        trialcount+=1
                    if conditionnumber == 5:
                        csvrow.append([subjectdata[subjectnumber][1], trialcount,subjectdata[subjectnumber][2],subjectdata[subjectnumber][3],
                                       subjectdata[subjectnumber][4],subjectdata[subjectnumber][5], 0,0,0,0,1,0,0,0,trialsdata[trialnumbers][3],
                                       trialsdata[trialnumbers][4], trialsdata[trialnumbers][5], trialsdata[trialnumbers][6]])
                        trialcount+=1
                    if conditionnumber == 6:                        
                        csvrow.append([subjectdata[subjectnumber][1], trialcount,subjectdata[subjectnumber][2],subjectdata[subjectnumber][3],
                                       subjectdata[subjectnumber][4],subjectdata[subjectnumber][5], 0,0,0,0,0,1,0,0,trialsdata[trialnumbers][3],
                                       trialsdata[trialnumbers][4], trialsdata[trialnumbers][5], trialsdata[trialnumbers][6]])
                        trialcount+=1
        else:
            if conditionnumber == 7:
                newcondition = [2,3,6]
            if conditionnumber == 8:
                newcondition = [1,4,5]
            for newconditionnumber in range(len(newcondition)):
                for trialnumbers in range(len(trialsdata)):
                    if (trialsdata[trialnumbers][0] == subjectnumber) and (trialsdata[trialnumbers][1] == newconditionnumber):                    
                        if conditionnumber == 7:
                            csvrow.append([subjectdata[subjectnumber][1], trialcount,subjectdata[subjectnumber][2],subjectdata[subjectnumber][3],
                                           subjectdata[subjectnumber][4],subjectdata[subjectnumber][5], 0,0,0,0,0,0,1,0,trialsdata[trialnumbers][3],
                                           trialsdata[trialnumbers][4], trialsdata[trialnumbers][5], trialsdata[trialnumbers][6]])
                            trialcount+=1
                        if conditionnumber == 8:
                            csvrow.append([subjectdata[subjectnumber][1], trialcount,subjectdata[subjectnumber][2],subjectdata[subjectnumber][3],
                                           subjectdata[subjectnumber][4],subjectdata[subjectnumber][5], 0,0,0,0,0,0,0,1,trialsdata[trialnumbers][3],
                                           trialsdata[trialnumbers][4], trialsdata[trialnumbers][5], trialsdata[trialnumbers][6]])
                            trialcount+=1

h = open ('trials.csv', 'wb')
trialwriter = csv.writer(h)
trialwriter.writerows(csvrow)
h.close()

for subject in param.subjects:     #getting the real subjectnumber for comparing with trialsorigin.csv and subjectsorigin.csv
     subjectname = subject[1:]
     #get the subjectinitials for the trials.cvs
     for i in range(len(subjectdata)):
         if subjectname in subjectdata[i]:
             currentsubject = subjectdata[i]
     for condition in param.conditions:
         print subject,',', condition
         #check if is not the specialconditions 7 or 8        
         if condition not in ['7','8']:
             #get the data and save them in data
             for name in files:
                 if condition in name:
                     if subject+'_' in name:
                         filename = name
             with open (filename, 'rb') as f:
                 swapdata = pickle.load(f)
             data = swapdata[0:64, 0:4800:].transpose(2, 1, 0)
             print data.shape
         if condition in ['7','8']:
             #for sepcial conditions 7 and 8
             newdata = []
             #get conditions for the conditions
             if condition == '7':
                 swapcondition = [param.conditions[1],param.conditions[2], param.conditions[5]]
             if condition == '8':
                 swapcondition = [param.conditions[0],param.conditions[3], param.conditions[4]]
             #save the data in an list
             print swapcondition
             for compcondition in swapcondition:
                 for name in files:
                     if compcondition in name:
                         if subject+'_' in name:
                             filename = name
                 with open (filename, 'rb') as f:
                     swapdata = pickle.load(f)
                 swapping = swapdata[0:64, 0:4800:].transpose(2, 1, 0)
                 print swapping
                 newdata.append(swapping)
             #create an array with the size of the three conditons
             data = np.empty([len(newdata[0])+len(newdata[1])+len(newdata[2]), len(newdata[0][0]), len(newdata[0][0][0])])
             #fill the array on the right places with the data saved before            
             for i in range(len(data)):
                 if i <= len(newdata[0]):
                     data[i] = newdata[0][i-1]
                     print data[i].shape
                 if i > len(newdata[0]) and i <= (len(newdata[0]) + len(newdata[1])):
                     data[i] = newdata[1][i-len(newdata[0])-1]
                     print data[i].shape
                 if i > (len(newdata[0]) + len(newdata[1])):
                     data[i] = newdata[2][i-(len(newdata[0]) + len(newdata[1]))-1]
                     print data[i].shape
         
         
         #create savefile name
         print param.conditions.index(condition)
         print param.conditionnames[param.conditions.index(condition)]
         savefilename = param.ts_prefix + param.subjectnames[param.subjects.index(subject)]+param.conditionnames[param.conditions.index(condition)]+param.ts_suffix
         #save the data in a file        
         if condition not in ['7','8']:
             np.data.tofile('Z:/travelling_waves/ts_creation/perceptual_grouping_EEG/TS1/' + savefilename + '.dat', "wb")
         if condition in ['7','8']:
             np.data.tofile('Z:/travelling_waves/ts_creation/perceptual_grouping_EEG/TS1/' + savefilename+'.dat', "wb")
                 
         print data.shape
         print savefilename