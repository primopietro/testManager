class Page:
    #A name variable
    #Desktop first, mobile second
    pageUrls=[]
    #List of languages in page
    pageLanguages = []
	
    def __init__(self,pageUrls):
        self.pageUrls = pageUrls
		#override those if needed at runtime
        self.pageLanguages = ["us","ca","fr-ca"]
            