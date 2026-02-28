##creating the mini project where we are  calculating the total expenditure of room
# inputs :- rent amount , food bills , electricity bills , room charges , members are present 
class Solution :
    def inputs (self , rent , food , electricity_bill , room_rent , members):
        self.rent=rent
        self.food =food
        self.electricity_bill =electricity_bill
        self.room_rent=room_rent
        self.members =members
    def calculating  (self) :
        add = (self.rent + self.food + self.electricity_bill + self.room_rent) // self.members
        return add 
obj = Solution()
rent = int (input ('input the rent of the room :'))
food = int (input('input the total bills of food :'))
electricity_bill =int(input ('input the electricity bills :'))
room_rent = int(input('input the room rent :'))
members = int(input('input how many members r present :'))
obj.inputs(rent,food,electricity_bill,room_rent,members)
print (f'Each peron should pay : {obj.calculating()}')