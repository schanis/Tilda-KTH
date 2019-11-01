class Node:
    def __init__(self,data,next=None): #klass för noden
        self.data=data
        self.next=next
    def __str__(self):
        return '{self.data}'.format(self=self)
class LinkedQ:
    def __init__(self,first=None,last=None):
        self.__first=first
        self.__last=last

    def __str__(self):
        return str(self.__first.data) + " " + str(self.__last.data)
    def getlast(self):
        return self.__last

    def enqueue(self,x): #stoppar in värde sist i kön

        if self.__first==None:

            self.__first=Node(x)
            self.__last=self.__first
        else:
            self.__last.next=Node(x)
            self.__last=self.__last.next

    def isEmpty(self): #returnerar true om kön är tom
        return self.__first==None

    def Size(self):#returnerar element i vår länkade lista
        count=0
        current=self.__first
        while current != None:
            count=count +1
            current=current.next
        return count


    def dequeue(self): #poppar sista elementet
        if not self.isEmpty():
            temp=self.__first.data
            self.__first=self.__first.next
            if self.Size()==1:
                self.__last=self.__first
            return temp
    def peek(self):
        if not self.isEmpty():
            temp=self.__first.data
            return temp
            
if __name__=="__main__": # gör så koden här inte körs om vi inte kör från denna fl
    q=LinkedQ()
    q.enqueue(1)
    q.enqueue(2)
    f=q.dequeue()
    print(f)
    f=q.dequeue()
    print(f)
    q.enqueue(9)
    f=q.Size()

    print(q)
