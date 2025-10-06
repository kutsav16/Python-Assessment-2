import json
rental_bookings={}

# lode data from json file
with open("book.json","r") as f:
    rental_bookings=json.load(f)
    
# create function for give book for rent
def book_rental():
    print("---book rental booking---")
    cust_name=input("Enter customer name:") # get customer name
    book_title=input("Enter book title:") # get book title
    flags=1
    try:
        day=int(input("Enter return day (1-31):")) # get return day of book
    except ValueError: 
        flags=0
        print("Pls enter INT value.")
    if flags==1:
        if day > 0 and day <= 31:
            return_day=day
        else:
            print("Enter valide return day.")
            
        # return_month=int(input("Enter return month (1-12):"))
        # return_year=int(input("Enter return year :"))
        
        # add customer data in over dict
        rental_bookings[book_title]={"cust_name":cust_name,
                            "book_title":book_title,
                            "return_day":return_day,
                            #    "return_month":return_month,
                            #    "return_year":return_year
                            }
        
        # add data in over json file
        with open("book.json", "w") as f:   
            json.dump(rental_bookings, f,indent=4)
            f.write("\n")   
  
        print(f"Rental recorded: {book_title} rented by {cust_name}") 
    else:
        print("Pls enter day value (1-31)")
        
    
# create function for return book   
def book_return():
    if len(rental_bookings)>0:
        print("---book return and late fee---")
        cust_name=input("Enter customer name:") # get customer name
        book_title=input("Enter book title:") # get book tital
        
        # cheak customer in over dict
        if cust_name in rental_bookings[book_title]["cust_name"]:
            # cheak book title in over dict
            if book_title in rental_bookings:
                book_info = rental_bookings[book_title]  
                return_day = book_info["return_day"]
                try:
                    today_date=int(input("Enter today date :")) # get today date 
                    
                    Day_count=today_date - return_day # count late day
            
                    if Day_count==0:
                        print("Thank you..") 
                
                    else:
                        Late_fee=10
                        Late_fee_count=Day_count*Late_fee # count late fee
                
                    print("\n------ RECEIPT ------")
                    print(f"Customer Name : {cust_name}")
                    print(f"Book Title    : {book_title}")
                    print(f"Return Day    : {return_day}")
                    print(f"Today Date    : {today_date}")
                    print(f"Late Days     : {Day_count}")
                    print(f"Late Fee      : Rs. {Late_fee_count}")
                    print("---------------------")
                    
                    # after return book and delete record from over dict
                    del rental_bookings[book_title]
                    # update record in dict
                    with open("book.json", "w") as f:
                        json.dump(rental_bookings, f, indent=4)
        

                except ValueError:
                    print("Pls enter day value (1-31)")
                
            else:
                print("Book not found in rental bookings.")
                
        else:
            print("Customor not found in rental booking.")
        
        
    else:
        print("Enter first data in rental_booking.")
        
        
    
while True:
    print("\n--- RentTrack System ---")
    print("1. Book Rental Booking")
    print("2. Book Return & Late Fee")
    print("3. Exit")

    choice = input("Enter choice (1-3): ") # enter choice

    match choice:
        case "1":
            book_rental()
        case "2":
            book_return()
        case "3":
            print("Goodbye!")
            break
        case _:
            print("Try again.")