class Test:
    page = None
    browsers = []
    name = ""	
   
    def __init__(self,name,page):
        self.name = name
        self.page = page
		#Override at runtime if needed
        self.browsers = ["chrome"]
	