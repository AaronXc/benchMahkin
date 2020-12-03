# benchMahking
stuff to run benchmark tests. There is a script to make all the job files and commands needed to run the fio tests using
those job files. All the commands generated are written in "allCommands" which is a BASH script saved to the present working directory.
Once all the job files are created, the BASH script "runTests" runs "allCommands". The "createBenchMKresults" script then makes a directory
containing iops and bandwidth data.
