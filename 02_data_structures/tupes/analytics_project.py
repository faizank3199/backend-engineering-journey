"""
======================================================
 Data Processing analytical (mini Project)    
======================================================
--------------------------------------------------------
sales_data = (
    ("Laptop", 20800, 5),
    ("Phone", 25000, 8),
    ("Tablet", 13000, 3)
)
- Calculate total revenue 
- Find best selling product 
- Average revenue per product
- Most Expensive Product
- Total unit sold
---------------------------------------------------------

Author : Mohammad Faizan
Date : 17/03/2026

"""
#==========================================================

# Dataset

sales_data = (
    ("Laptop", 20800, 5),
    ("I Phone", 150000, 8),
    ("Tablet", 13000, 3)
)

# Calculate Total Revenue 

def calculate_total_revenue()-> int:
    total_revenue = 0
    
    for product,price, qty in sales_data:
        revenue = price * qty
        total_revenue += revenue 
        
    return total_revenue 

# Best Selling Product 

def find_best_selling_prod()-> tuple:
    
    best_product = ""
    max_qty = 0
    
    for product, price, qty in sales_data:
        if qty > max_qty:
            max_qty = qty
            best_product = product
            
    return best_product, max_qty

# Average revenue per product 

def average_revenue_per_product()->float:
    
    total_revenue = calculate_total_revenue()
    average  =  total_revenue/ len(sales_data)
    
    return average 
        
def find_most_expensive_prod()->tuple:
    
    expensive_product = ""
    max_price = 0
    
    for product, price, qty in sales_data:
        if price > max_price:
            max_price = price
            expensive_product = product
            
    return expensive_product, max_price

def total_unit_sold()->int:
    
    total_unit = 0
    
    for product, price, qty in sales_data:
        total_unit += qty
        
    return total_unit
    
    
# Main Program 

def main():
    
    total_revenue = calculate_total_revenue()
    best_product, qty = find_best_selling_prod()
    average = average_revenue_per_product()
    most_expensive_prod, price = find_most_expensive_prod() 
    total_unit = total_unit_sold()
    
    print(f"Total Revenue:  {total_revenue}")
    print(f"Best Selling Product: {best_product}, ({qty} units)")
    print(f"Average revenue per product: {average:.2f}")
    print(f"Most Expensive Product: {most_expensive_prod} price: {price}")
    print(f"Total Unit Sold: {total_unit}" )

#=======================================================================

if __name__ == "__main__":
    main()