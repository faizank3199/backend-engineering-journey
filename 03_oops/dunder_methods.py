from datetime import datetime


"""
Dunder Methods:
 - Magic methods (also called dunder methods) are special methods in Python
   that start and end with double underscores like __init__, __str__, etc.

 - They allow you to define how your objects behave with built-in operations 
   like printing, addition, comparison, and more.
    
Topic covered:
 1. __init__
 2. __str__
 3. __repr__
 4. __add__
 5. __mul__
 6. __eq__
 7. __lt__
 8. __getitem__
 9. __getattr__
 10. __call__
 11. __len__
 12. __contains__
 12. All dunder method covered with examples
 
 ================
Author: Mohammad Faizan
    
"""

#======================================
#      Playlist Example
#======================================

class Playlist:
    def __init__(self, limit=4):
        self.limit = limit
        self.songs = []
        
    def _normalize(self, song):
        return song.strip().lower()
        
    def add_song(self, song):
        song = self._normalize(song)
        
        if song in self.songs:
            return {"status": "error", "message":f"'{song}' already exists"}
        
        if len(self.songs) >= self.limit:
            return {"status": "error", "message":"playlist is full"}
        
        self.songs.append(song)
        return {"status": "success", "message":f"'{song}' added"}
    
    def search_song(self, song):
        song = self._normalize(song)
        
        if song not in self.songs:
            return {"status": "error", "message":f"'{song}' not found"}
        
        return {"status": "success", "message":f"'{song}' found"}
    
    def remove_song(self, song):
          song = self._normalize(song)
          
          if song not in self.songs:
              return {"status": "error", "message":f"'{song}' not found"}
          
          self.songs.remove(song)
          return {"status": "success", "message":f"'{song}' removed"}
      
    def __contains__(self, song):
        if not isinstance(song, str):
            return False
        return self._normalize(song) in self.songs
      
    def __getitem__(self, index):
        if not isinstance(index, (int, slice)):
            raise TypeError(f"Index must be int or slice")
        
        return self.songs[index]
    
    def __len__(self):
        return len(self.songs)
    
    def __iter__(self):
        return iter(self.songs)
    
    def __str__(self):
        return "Playlist:\n" + "\n".join(f"- {song}" for song in self.songs)
    
    def __repr__(self):
        return f"Playlist(songs={self.songs}, limit={self.limit})"
    
#===========================================================
#  add money with same currency
#===========================================================

class Money:
    def __init__(self, amount, currency = "INR"):
        self.amount = amount
        self.currency = currency
        
    def __add__(self, other):
        
        if isinstance(other, Money):
            if self.currency != other.currency:
                raise ValueError("Can not add different currency")
            return Money(self.amount + other.amount, self.currency)
        
        elif isinstance(other, (int, float)):
            return Money(self.amount + other, self.currency)
        
        return NotImplemented
        
    def __radd__(self, other):
        return self.__add__(other)
        
        
    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        
        if self.currency != other.currency:
            raise ValueError("cannot compare different currency")
        
        return self.amount == other.amount
        
    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        
        if self.currency != other.currency:
            raise ValueError("Cannot compare different currencies")
        
        return self.amount < other.amount
    
    def __repr__(self):
        return f"Money({self.currency}:{self.amount})"
    
#=============================================================
#      Adding Cart with operator overloading
#=============================================================

class Cart:
    def __init__(self, items = None):
        self.items = items or []
        
    def __add__(self, other):
        if not isinstance(other, Cart):
            return NotImplemented
        
        return Cart(self.items + other.items)
    
    def __len__(self):
        return len(self.items)
    
    def __repr__(self):
        return f"Cart({self.items})"
    
#===============================================
#                 Api Response
#==============================================
    
class ApiResponse:
    def __init__(self, data, status = 200):
        self.data = data
        self.status = status
        
    def __getitem__(self, key):
        if key not in self.data:
            raise KeyError(f"{key} not found")
        
        return self.data.get(key)
    
    def __str__(self):
        return f"Data: {self.data}, Status = {self.status}"
    
    def __repr__(self):
        return f"ApiResponse(data={self.data}, status = {self.status})"
    
#========================================================
#                 Logger
#========================================================

class Logger:
    def __init__(self, service):
        self.service = service
        
    def __call__(self, message, level = "INFO"):
        timestamp = datetime.now().strftime("%y:%m:%d %H:%M:%S")
        print(f"[{timestamp}] [{self.service}] [{level}] {message}")
        

#=======================================================
#        Database Row Object
#======================================================

class DatabaseRow:
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, key):
        if key not in self.data:
            raise KeyError(f"{key} not found")
        return self.data.get(key)
    
    def __getattr__(self, key):
        if key not in self.data:
            raise AttributeError(f"{key} not found")
        return self.data[key]
    
#=======================================================
#      __mul__ method
#=======================================================
class CartItem:
    def __init__(self, product, price, quantity=1):
        if price < 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.product = product
        self.price = price
        self.quantity = quantity
        
    def __mul__(self, quantity):
        if not isinstance(quantity, int):
            return NotImplemented
        
        return CartItem(self.product, self.price, self.quantity * quantity)
    
    def total_price(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.product}, Quantity: {self.quantity}, Total Price: {self.total_price()}"
    
    def __repr__(self):
        return f"CartItem('{self.product}', price={self.price}, quantity={self.quantity})"


    
#======================================
#     Main Execution
#=====================================

if __name__ == "__main__":
    
    # Playlist
    playlist = Playlist()
    print("-- Adding Song --")
    print(playlist.add_song("shape of you"))
    print(playlist.add_song("Believer"))
    print(playlist.add_song("Calm down"))
    print(playlist.add_song("Alone"))
    print(playlist.add_song("him and i"))
    
    print("\n -- Searching Song -- ")
    print(playlist.search_song("calm down"))
    
    print("\n -- Remove Song --")
    print(playlist.remove_song("Believer" )) 
    
    print("\n (__contains__)")
    print("alone" in playlist)
        
    print("\n-- Slicing and Indexing --")
    print(playlist[1])
    print(playlist[1:3])    
    
    print("\n -- Total Item (__len__ ) --")
    print("Total Item:",len(playlist))
    
    print("\n --Songs in Playlist--")
    for song in playlist:
        print(song)
        
    print("\n -- Playlist(__str__) --")
    print(playlist)
    
    print("\n__repr__")
    print([playlist])
    #===========================================   
    # Money
    print("\n===== Money ======")
    m1 = Money(200)
    m2 = Money(300)
    m3 = Money(500)
    print("\n -- Total Amount--")
    m4 = m1 + m2 + m3
    print(m4)
    print("\nm2 + 300")
    print(m2 + 300)
    print("\n400 + m3")
    print(400 + m3)
    print("\n __lt__")
    print(m1 < m3)
    print("\n__eq__")
    print(m2 == m3)
    
    # Adding Cart with operator overload
    c1 = Cart(["Apple", "Banana"])
    c2 = Cart(["Pineapple"])
    cart = c1 + c2
    print("\n--Adding Cart with operator overloading--")
    print(cart)
    print("Total item in cart:",len(cart))
    
    # ApiResponse
    res = ApiResponse({"user":"faizan", "role":"admin"})
    print("\n -- ApiResponse --")
    print(res["user"])
    print(res)
    print([res])
    
    # Logger
    print("\n -- Logger --")
    log = Logger("Auth_service")
    log("Login Successfull")
    log("Invalid Password", level = "ERROR")
    
    # DatabaseRow
    row = DatabaseRow({"User":"Ashu", "Age":24})
    print("\n -- Databaserow --")
    print(row["User"])
    print(row.Age)
    
    # __mul__ method
    item = CartItem("Laptop", 50000, 1)
    print("\n __mul__")
    print(item)
    item2 = item * 3
    print(item2)
