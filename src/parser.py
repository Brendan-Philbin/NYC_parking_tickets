import sys
import argparse

x = sys.argv

def parse_this(x):
    
    print('Number of arguments entered:', len(sys.argv))
    print('Argument List:', str(sys.argv)) 
    
    new_parser = argparse.ArgumentParser()
    new_parser.add_argument('--page_size', type=int,nargs=1)
    new_parser.add_argument('--num_pages', type=int,nargs=1,default=0)
    args = new_parser.parse_args()
    print(args)
    page_size = args.page_size
    num_pages = args.num_pages
    
    page_size = page_size[0]
    if num_pages == 0:
        num_pages = num_pages
    else:
        num_pages = num_pages[0]
        
    
    print('Page Size:', page_size,'      Number of Pages:', num_pages)
    return page_size,num_pages
    
    

