#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
    
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print('Flipping the page...wow, you read fast!')

    def get_page_count(self):
        return self.page_count
    
    def set_page_count(self,page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else :
            self.page_count = page_count

    

    
        

   
    
    