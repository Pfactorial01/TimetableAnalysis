#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


#To-do List
#- read all 5 pages of the schedule into a single pandas dataframe
#- figure out which are grad and which are undergrad classes
#- display the undergrad 8am classses
#- display the undergrad friday classes


# In[62]:


# Save website url to variable
website = 'https://portal.engineering.utoronto.ca/sites/timetable/fall.html'

# Web scrape html into datalist
datalist = pd.read_html(website)

# Create empty dataframe to store combined datalist
time_table = pd.DataFrame()

# Store combined datalist into empty dataframe
time_table = time_table.append(datalist[1:13])


# Function to create new columns which show course nummber and CourseType(Grad/Ugrad)
def determine_grad_ugrad(time_table):
    # Create coursenumber column and store course number from sliced coursename
    time_table['COURSENUM'] = time_table['NAME'].str[3:6]
    # Create course type column set initially to none
    time_table['Type'] = 'None'
    # Assign either U/G to each course by checking if coursenum >/< 500
    time_table['Type'][time_table['COURSENUM'].astype(int) >= 500] = 'G'
    time_table['Type'][time_table['COURSENUM'].astype(int) <= 500] = 'U'
    return time_table
    


# In[121]:


# call function to determine ugrad/grad
datalist1 = determine_grad_ugrad(time_table)

# Save only graduate courses to ugrad variable
ugrad = datalist1[datalist1['Type'] == 'U']
# Request user input to know if user wants to see 9am or Friday classes
choice = input("Do you want 9am Classes or Friday classes? Enter 9 or F:  ").upper()
# If block for user choice
if choice == '9':
    df = ugrad[ugrad['START'].str.find('09:00')>=0]
elif choice == 'F':
    df = ugrad[ugrad['DAY'].str.find("Fri")>=0]
else:
    print('Please read the instructions')

df


# In[110]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




