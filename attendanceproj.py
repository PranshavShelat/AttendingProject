import pandas as pd
df=pd.read_csv("updated_academic_calendar.csv")
num= int(input("Enter number of subjects: "))
i=0
arr=[]
for i in range(0,num):
    arr.append(input(f"Enter name of subj {i+1}: "))
print(arr)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
schedule = {day: {subject: int(input(f"Enter number of {subject} classes on {day}: ")) for subject in arr} for day in days}

sub=input("Enter subject to check for attendance: ")
nos=int(input("Enter number of classes attended: "))
dos=int(input("Total number of classes completed for this subject: "))
currdate=pd.to_datetime(input("Enter current date(yyyy-mm-dd): "))

df["Start Date"]=pd.to_datetime(df["Start Date"])
df["End Date"]=pd.to_datetime(df["End Date"])
week_row = df[(df["Start Date"] <= currdate) & (df["End Date"] >= currdate)]

print(week_row)

currday=(currdate-week_row.iloc[0]["Start Date"]).days
print(days[currday])

print(schedule)
cr=schedule[days[currday]][sub]

for i in range(currday+1,5):
    cr+=schedule[days[i]][sub]
holidays=week_row["Holidays"].values[0].split("; ")
for i in range(0,len(holidays)):
  if(days.index(holidays[i])>currday):
    cr=cr-schedule[holidays[i]][sub]
print(cr)

inaweek=0
for i in range(0,5):
    inaweek+=schedule[days[i]][sub]
print(inaweek)

count=0
last=int(df.iloc[-1]["Week No"])
now=int(week_row['Week No'])
for i in range(now,last):
  count=count+1
print(count)

counter=inaweek*count



for i in range(now, last-1):
  checking=int(df.iloc[i]["Working Days"])
  if(checking!=5):
    holidays=df.iloc[i]["Holidays"].split("; ")
    for j in holidays:
      counter=counter-schedule[j][sub]
print(counter)

counter=counter+cr
ndos=dos+counter
mandatory=(75/100)*ndos
print("Number of classes to attend: ",mandatory-nos)

print("Number of classes Mandatory: ",mandatory)
print("Total number of classes: ",ndos)

