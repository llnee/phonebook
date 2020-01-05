#Name: Laura Nee
#phonebook.py

#Purpose: to create a phonebook using specially designed classes
#Certification of Authenticity:
#   I certify that this lab is entirely my own work.

class phoneBookEntry:
    #properties: name, phone number
    def __init__(self, name, phoneNumber):
        #name & num are both str's
        if type(name) == str and type(phoneNumber) == str:
            if len(phoneNumber) == 10: #phone nums have 10 digits
                self.name = name
                self.number = phoneNumber
        else: #set defaults
            self.name = "John Smith"
            self.number = "9999999999"

    #getters
    def getName(self):
        return self.name
    def getPhone(self):
        return self.number

    #setter
    def setPhone(self, phoneNumber):
        if len(phoneNumber) == 10: #phone nums have 10 digits
            self.number = phoneNumber

    #str method
    def __str__(self):
        formattedNum = "(" + self.number[0:3] + ")" + self.number[3:
                                            6] + "-" + self.number[6:]
        return self.name + ": " + formattedNum

class Phonebook:
    def __init__(self):
        #entries is a list of phoneBookEntry objs
        self.phoneBook = []

        #defaults
        self.isSorted = False

    def addEntry(self, name, phoneNumber): #V
        #create an entry using the phoneBookEntry class
        entry = phoneBookEntry(name, phoneNumber)
        #append that entry to the phonebook class
        self.phoneBook.append(entry)

    def sort(self):
        self.isSorted = True

        #selection sort
        minPos = 0
        for front in range(len(self.phoneBook) - 1):
            minPos = front
            for i in range(minPos + 1, len(self.phoneBook)):
                #if the firstLetter of phoneBook[i] is earlier
                #than the firstLetter of phoneBook[minPos],
                # then the actual minPos is at i
                if ord(self.phoneBook[i].getName()[0]) < ord(self.phoneBook
                        [minPos].getName()[0]):
                    minPos = i
            #swap 'em
            lowest = self.phoneBook[minPos]
            self.phoneBook[minPos] = self.phoneBook[front]
            self.phoneBook[front] = lowest

                
    def findPhoneNumber(self, name): #returns phoneNumber
        #create list of sorted names from phoneBook
        namesInPhonebook = []
        for entry in self.phoneBook:
            Name = entry.getName()
            namesInPhonebook.append(Name)
                
        if self.isSorted: #binary search
            #search list of names for the specified name
            low = 0
            high = len(namesInPhonebook)
            mid = (low + high) // 2
            while namesInPhonebook[mid] != name and low <= high:
                if name < namesInPhonebook[mid]: #adjust high
                    high = mid - 1
                else: #adjust low
                    low = mid + 1
                mid = (low + high) // 2
            if low > high: #name not in phoneBook
                mid = -1
        else: #not sorted, linear search
            for i in range(len(namesInPhonebook)):
                if name == namesInPhoneBook[i]:
                    mid = i
                else:
                    mid = -1

        if mid == -1:
            return ""
        else:
            return self.phoneBook[mid].getPhone()

    def __str__(self):
        rtnStr = ""
        for entry in self.phoneBook:
            rtnStr += str(entry) + "\n"
        return rtnStr


def main():
    #valid entry that prints a single phoneBookEntry obj
    ent1 = phoneBookEntry("Jane", "8435555555")
    print(ent1)
    #invalid entries that trigger default values
    ent2 = phoneBookEntry(7, "8435555555")
    print(ent2)
    ent3 = phoneBookEntry("Jane", 5.2)
    print(ent3)

    #create a phone book
    myPhonebook = Phonebook()
    names = ["Jane", "Fred", "Bob", "Peter", "Alex", "Vic"]
    nums = ["8435555555", "8436666666", "8437777777", "8432222222",
                "8430000000", "8433333333"]
    for i in range(len(names)):
        myPhonebook.addEntry(names[i], nums[i])
    print("\nUnsorted: \n" + str(myPhonebook))

    myPhonebook.sort()
    print("\nSorted: \n" + str(myPhonebook))

    #find phoneNumber of someone in the book
    print("Bob's phone number is", myPhonebook.findPhoneNumber("Bob"))
    #find phoneNumber of someone not in the book, returns empty str
    print("Susan's phone number is", myPhonebook.findPhoneNumber("Susan"))
    

main()
        
    
