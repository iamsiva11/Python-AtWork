def parse_ipaddr(self):
		"""Reads log file and parses ip address and stores in a dictionary		
		Returns:
        	defaultdict : Parsed ip addresses
		"""
		ipaddr_dict = defaultdict(int)
		try:
			with open(self.LOG_FILE, "r") as log_text:
			    # Reads file line by line without loading the whole contents into memory
			    for columns in ( raw.strip().split() for raw in log_text ):  
			        ipaddr_dict[str(columns[2])]=1	
		except IOError:
			print "IOError: Could not read file:", LOG_FILE
		return ipaddr_dict