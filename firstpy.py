# course=str(input("Course_Code:"))
# print(course.replace('M','X'))
from array import*
# sum=0;
# hasCar=False;
# for i in range(5):
#     if(hasCar):
#         print("hasCar Finally");
#         break
#     if(i==2): hasCar=True
#     print("filthy poor");

arr=array('i',[-1,5,10,1,6,7,7,3,11]);

index=-1

def SayWord(name):
  print("It's "+name)

def SelectionSort(arr,size):
   index=-1;
   min=999999999;
   for i in range(size):
    for j in range(i,size):
      if(arr[j]<min):
        min=arr[j];
        index=j;
    if(index==-1):
      continue #just continue the for loop
    else:
      arr[index]=arr[i];
      arr[i]=min;
      min=99999999;
   return arr

def printArr(arr,size):
  for i in range(size):
    print(arr[i]);

def PrintArrReverse(arr,size,level=0):# a function that prints an array in reverse order recursively
  if(level==size-1):
    print(arr[level])
    return
  PrintArrReverse(arr,size,level+1)
  print(arr[level])
  
# SelectionSort(arr,9);
# printArr(arr,9);
# PrintArrReverse(arr,9);
# SayWord("Mohamed");

class Person(object):
  def __init__(self,name,age,gpa):
    self.name=name;
    self.age=age;
    self.gpa=gpa;
  def getName(self):
    return self.name
  def getAge(self):
    return self.age 
  def setAge(self,a):
    self.age=a;
  def setGPa(self,g):
    self.gpa=g  
  def printInfo(self):
    print("Name="+self.name+" and age="+str(self.age)+" and gpa="+str(self.gpa));


# p=Person("ahmed",19,3.7);
# p.printInfo();
# p.setAge(21);
# p.setGPa(3.6);
# p.printInfo();


class Node(object):
  def __init__(self,d,next=None):
    self.data=d
    self.next=next
  def getdata(self):
    return self.data
  def getnext(self):
    return self.next     
  def setData(self,newD):
    self.data=newD
  def setnext(self,newNext):
    self.next=newNext  


class LinkedList(object):
    head=Node('head',None);
    count=0;
    def getHead(self):
       return self.head
    def setHead(self,newHead):
      self.head=newHead
    def isEmpty(self):
      return self.head.getnext()==None  
    def Push(self,newVal):
      newNode=Node(newVal,None);
      # if(self.isEmpty()):
      newNode.setnext(self.head.getnext())
      self.head.setnext(newNode)
      self.count=self.count+1;
    def getCount(self):
      return self.count;
    def Pop(self):
      temp=self.getHead();
      temp=self.head.getnext();
      temp=temp.getnext();
      self.head.setnext(temp);
      self.count=self.count-1;
    def PrintList(self):
      temp=self.getHead().getnext();
      while temp:
        print(temp.getdata());
        temp=temp.getnext();
    def PrintReverse(self):
        self.__PrintReverse(self.head)
         # PrintReverse() is the public method we use
    def __PrintReverse(self,temp):# this is the private method we need to use in order to pass it the head
      if(temp.getnext()==None):
        return;
      temp=temp.getnext()  
      self.__PrintReverse(temp)
      print(temp.getdata())
    # def InsertionSort(self):
    #    if (self.getCount()==0 or self.getCount()==1):
    #     return true
    #    temp=self.getHead().getnext();
    #    if 

class TNode(object):
  def __init__(self,data):
    self.Left=None
    self.Right=None
    self.data=data

class Tree(object):
  def __init__(self):
    self.root=None;
  # def Insert(self,data):
  #   if(self.root==None):
  #     self.root=TNode(data)
  #   else:

      

l1=LinkedList();
l1.Push(11);
l1.Push(12);
l1.Push(13);
l1.Push(14);
# l1.PrintList();
# l1.Pop();
# l1.Pop();
# l1.PrintList();
# l1.PrintReverse(l1.head)
# l1.PrintReverse()


t1=tuple((1,56,"Ahmed"))
list1=[2,5];
fruits=set["apple", "banana"]
arr=array("i",[5,3,2,5])
print(arr);

words={
  "I":"Love",
  "i":"you",
  5:fruits
}

german_dict={
  "ich":"I",
   1:"eins",
  "fruits":fruits,
  "pie":3.14,
  "veggies":["cucumber","tomato","parcely"],
  "animals":['dog','cat','zebra'],
  t1:3.5
}

english_dict={
  1:"one",
  2:fruits,
  "one":1,
  fruits:"apple"
}
print("--english dict--")
print(english_dict.get(fruits,"DNE"))
# ---------
print("----german dictionary----")
print(german_dict.get('veggies',"Doesn't exist"))
print(german_dict.get("animals"),"Nein")
print(german_dict.get(t1))
print(german_dict.get("animal","Nein"))
# ----






#Note the Queue ADT below is implemented in a way such that the front and rear are initialized nodes 
class Queue(object):
  front=Node('front',None);
  rear=Node('rear',None);
  count=0;
  def getFront(self):
    return self.front;
  def isEmpty(self):
    return self.front.getnext()==None;
  def Enqueue(self,data):
    newNode=Node(data,None)
    if (self.isEmpty()):
      self.front.setnext(newNode)
      self.rear.setnext(newNode)
    else:
      temp=self.rear.getnext();
      temp.setnext(newNode)  
      newNode.setnext(None)
      self.rear.setnext(newNode)
    self.count=self.count+1;
  def Dequeue(self):
    temp=None;
    if(self.front.getnext()==self.rear.getnext()):
     temp=self.front.getnext();
     self.front.setnext(None);
     self.rear.setnext(None);
    else:
      temp=self.front.getnext().getnext();
      self.front.setnext(temp);
    if(temp):
         val=temp.getdata();
    else:
        val=0;   
    del temp
    return val;  
  def Print(self):
    temp=self.front.getnext();
    while temp:
      print(temp.getdata());
      temp=temp.getnext();  

      

class Person(object):
  def __init__(self,name,age):
    self.name=name;
    self.age=age;
  def getname(self):
    return self.name
  def ChangeAge(self,newage):
    self.age=newage;
  def getAge(self):
    return self.age  
  def PrintInfo(self):
    print(self.name+" of age "+str(self.age));  

class Engineer(Person):
  def __init__(self, name, age,GPA):
    self.GPA=GPA;
    super().__init__(name, age)    
  def getGPA(self):
    return self.GPA  
  def PrintInfo(self):
    print(self.name+" and age "+str(self.age)+" and GPA "+str(self.GPA))  

class SoftwareEngineer(Engineer):
  def __init__(self, name, age, GPA):
    super().__init__(name, age, GPA)

# e1=Engineer("Mohamed Gamal",20,3.5);
# e1.PrintInfo();
# print(e1.getAge());
# e2=SoftwareEngineer('Hamada',21,3.9);
# print(e2.getGPA());
# file=open(r"C:\Users\DELL\source\repos\MatrixClass\InputFile404.txt");#the proper way to reading a file,
# # you add the r before the file's name

# nums=array("i");
# nums.append(9)
# nums=file.read(9);

# # t=0;
# # for i in range(9):
# #   t=file.read(9);
# #   nums[int(i)]=t

# printArr(nums,9);  