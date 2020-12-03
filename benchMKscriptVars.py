


noAlternating=[
	
    "/dev/1-1", 
			 
	"/dev/1-2", 
			 
	"/dev/1-3", 
			 
	"/dev/1-4", 
			 
	"/dev/1-5", 
			 
	"/dev/1-6", 
			 
	"/dev/1-7", 
			 
	"/dev/1-8",
        
    "/dev/1-9",
			 
	"/dev/1-10", 
			 
	"/dev/1-11",
			 
	"/dev/1-12",
			 
	"/dev/1-13",
			 
	"/dev/1-14",
			 
	"/dev/1-15",
			 
	"/dev/1-16",
			 
	"/dev/2-1",
			 
	"/dev/2-2", 
			 
	"/dev/2-3", 
			 
	"/dev/2-4", 
			 
	"/dev/2-5", 
			 
	"/dev/2-6", 
			 
	"/dev/2-7", 
			 
	"/dev/2-8", 
    
    "/dev/2-9",
			 
	"/dev/2-10", 
			 
	"/dev/2-11",
			 
	"/dev/2-12",
			 
	"/dev/2-13",
			 
	"/dev/2-14",
			 
	"/dev/2-15",
			 
	"/dev/2-16"]

alternatingPorts=[	
    
    "/dev/1-1", 
 			 
	"/dev/1-5", 
			 
	"/dev/1-9", 
			 
	"/dev/1-13",  
			 
	"/dev/1-2", 
			 
	"/dev/1-6",
			 
	"/dev/1-10",
			 
	"/dev/1-14",
			 
	"/dev/1-3", 
	
	"/dev/1-7", 
			 
	"/dev/1-11", 
    
	"/dev/1-15", 
    
    "/dev/1-8",

    "/dev/1-4",
	
    "/dev/1-12",
			 
	"/dev/1-16", 
	
	"/dev/2-1", 
 			 
	"/dev/2-5", 
			 
	"/dev/2-9", 
			 
	"/dev/2-13",  
			 
	"/dev/2-2", 
			 
	"/dev/2-6",
			 
	"/dev/2-10",
			 
	"/dev/2-14",
			 
	"/dev/2-3", 
	
	"/dev/2-7", 
			 
	"/dev/2-11", 
    
	"/dev/2-15", 
    
    "/dev/2-8",

    "/dev/2-4",
	
    "/dev/2-12",
			 
	"/dev/2-16"
	]
    
alternatingPortsAndCards=[	
    
    "/dev/1-1", 
			 
	"/dev/2-1", 
			 
	"/dev/1-5", 
			 
	"/dev/2-5", 
			 
	"/dev/1-9", 
			 
	"/dev/2-9", 
			 
	"/dev/1-13", 
			 
	"/dev/2-13", 
			 
	"/dev/1-2", 
			 
	"/dev/2-2",
			 
	"/dev/1-6",

	"/dev/2-6", 
			 
	"/dev/1-10",
			 
	"/dev/2-10",
			 
	"/dev/1-14",
	
	"/dev/2-14",
			 
	"/dev/1-3", 

	"/dev/2-3",
			 
	"/dev/1-7", 
	
	"/dev/2-7", 
			 		 
	"/dev/1-11", 
			 
	"/dev/2-11", 
	
    "/dev/1-15",
    
	"/dev/2-15", 
    
    "/dev/1-8",
			 
	"/dev/2-8", 

    "/dev/1-4",
    
	"/dev/2-4", 
	
    "/dev/1-12",
	
    "/dev/2-12",
			 
	"/dev/1-16",
			 
	"/dev/2-16"]
    
alternatingCards=[	
    
    "/dev/1-1", 

	"/dev/2-1",
			 
	"/dev/1-2", 
	
	"/dev/2-2",
			 
	"/dev/1-3", 
			 
	"/dev/2-3", 
			 
	"/dev/1-4", 
	
	"/dev/2-4",
			 
	"/dev/1-5", 
	
	"/dev/2-5", 
			 
	"/dev/1-6", 
	
	"/dev/2-6", 
			 
	"/dev/1-7", 
	
	"/dev/2-7",
			 
	"/dev/1-8", 
	
	"/dev/2-8",
    
    "/dev/1-9", 
	
	"/dev/2-9",
			 
	"/dev/1-10", 
	
	"/dev/2-10",
			 
	"/dev/1-11",
	
	"/dev/2-11",
			 
	"/dev/1-12",
	
	"/dev/2-12",
			 
	"/dev/1-13",
	
	"/dev/2-13",
			 
	"/dev/1-14",
	
	"/dev/2-14",
			 
	"/dev/1-15",
	
	"/dev/2-15",
			 
	"/dev/1-16",
	
	"/dev/2-16"]
    
driveOrders=[noAlternating, alternatingPorts, alternatingCards, alternatingPortsAndCards]

directoryNames=[
                "read_noAlt", "read_altPorts", "read_altCards", "read_altPortsAndCards",
                "write_noAlt", "write_altPorts", "write_altCards", "write_altPortsAndCards",
                "randrw_noAlt", "randrw_altPorts", "randrw_altCards", "randrw_altPortsAndCards"
                ]
	
globalSection = "[global]\n \
			name=name\n \
			filesize=16g\n\
			bs=1M\n\
			ioengine=libaio\n\
			readwrite=read\n\
            iodepth=32\n\
            direct=1\n\
			numjobs=1\n\
			group_reporting\n"
				
globalSection2 = "[global]\n\
			name=name\n\
			filesize=4g\n\
			bs=4k\n\
			ioengine=libaio\n\
			readwrite=write\n\
            iodepth=32\n\
            direct=1\n\
			numjobs=1\n\
			group_reporting\n"
           
globalSection3 = "[global]\n \
			name=name\n \
			filesize=8g\n\
			bs=64k\n\
			ioengine=libaio\n\
			readwrite=randrw\n\
            iodepth=32\n\
            direct=1\n\
			numjobs=1\n\
			group_reporting\n"
            
globalSections= [globalSection, globalSection2, globalSection3]
				
				
				