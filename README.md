
# Logs Analysis

#### Description

Log analysis is an app allow user to run report from database by using virtual machine. 
 
#### How to open the file? 
######  (Example below will be using **vagrant**)

1. Download the app to the folder name **vagrant**.
2. Open the terminal and then go directly to the location where you store the file
3.  Before running the command line before, please bring the virtual machine online with`vagrant up`. Then log into it with `vagrant ssh`
4.  After you saw something like **vagrant@vagrant**, type code below and hit enter.
```
$ cd /vagrant
```
5. Run the command line below
```
$ python newsdatadb.py
```
#### View definitions

###### 1. Table name: statustotal
    create view statustotal as
    select date(time),
    count(*) as total
    from log
    group by date(time);

###### 2. Table name: errortotal
    create view errortotal as
    select date(time),
    count(*) as errors
    from log
    where status != '200 OK'
    group by date(time);

###### 3. Table name: errorpercent
    create view errorpercent as 
    select st.date, st.total, et.errors, 
    round(((et.errors * 1.00) / st.total), 3) as result
    from statustotal st inner join errortotal et
    on st.date = et.date;
# logs_analysis
