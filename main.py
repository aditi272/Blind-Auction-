from replit import clear
import art 
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
bid_dict = {}
print("Welcome to the secret auction program.")
bidding = True
while bidding:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bid_dict[name] = bid
  ans = input("Are there any more bidders? Type 'yes' or 'no'.")
  if ans == 'yes':
    bidding = True
    clear()
  else:
    bidding = False

print(bid_dict)
high_bid = 0
high_name = ''
for i,j in bid_dict.items():
  if(j > high_bid):
    high_bid = j
    high_name = i
print(f"The winner is {high_name} with a bid of ${high_bid}.")



  
# Myway
# print(art.logo)
# print('Welcome to the secret auction program.')
# option = True
# bidders = []
# def add(name,bid):
#   bidders.append({
#     "name" : name,
#     "bid"  : bid
#   })
 
# while option:
  
#   name = str(input('What is your name?: '))
#   bid = int(input('What is your bid?: $'))
#   add(name,bid)
#   opt = input("Are there any other bidders? Type 'yes' or 'no'.\n")
#   if opt == 'yes':
#     option = True
#     clear()
#   else:
#     #logic
#    high = 0 
#    winner = ''
#    for i in range(len(bidders)):
     
#      n = bidders[i]["bid"]
     
#      if n > high:
      
#       high = n
#       winner = bidders[i]["name"]
         
    
#    print(f"The winner is {winner} with a bid of ${high}")  
#    option = False

# ########Angela

# # print(art.logo)
# # print('Welcome to the secret auction program.')
# # option = True
# # bidders = {}
# # def add(name,bid):
# #   bidders[name] = bid
# #   print(bidders)
  
# # while option:
  
# #   name = str(input('What is your name?: '))
# #   bid = int(input('What is your bid?: $'))
# #   add(name,bid)
# #   opt = input("Are there any other bidders? Type 'yes' or 'no'.\n")
# #   if opt == 'yes':
# #     option = True
# #     clear()
# #   else:
    
# #     #logic
# #     high = 0 
   
# #     winner = ''
# #     for key in bidders:
      
# #       n = bidders[key]
    
#       if n > high:
      
#         high = n
#         winner = key
#     print(f"The winner is {winner} with a bid of ${high}.")
#     option = False