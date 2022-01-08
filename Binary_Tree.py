
class employee:
    def __init__(self,id,employee_name,email,age,gender):
        self.id=id
        self.employee=employee_name
        self.email=email
        self.age=age
        self.gender=gender
    def printinfo(self):
        print(self.id,self.employee,self.email,self.age,self.gender)
res1=employee(16,'rahul','xxxxxx@gmail.com',19,'male')
res2=employee(33,'abishek','xxxxxx@gmail.com',18,'male')
res3=employee(3,'xxxx','xxxxxx@gmail.com',29,'male')
res4=employee(100,'xxxx','xxxxxxx@gmail.com',19,'male')
res5=employee(98,'xxxx','xxxxxx@gmail.com',22,'male')
res6=employee(41,'xxxxx','xxxxxxx@gmail.com',26,'male')
res7=employee(51,'xxxxx','xxxxxx@gmail.com',33,'male')
res8=employee(26,'xxxxx','xxxxxxxx@gmail.com',43,'male')
res9=employee(99,'xxxxx','xxxxxxxx@gmail.com',25,'male')
res10=employee(77,'xxxx','xxxxxxxxx@gmail.com',18,'male')
lis=[res1,res2,res3,res4,res5,res6,res7,res8,res9,res10]
class NODE:
    def __init__(self,left,right,key,parent):
        self.left=left
        self.right=right
        self.key = key
        self.parent=parent

class BST():
    def __init__(self,root):
        self.root=root

    def insertnode(self,value):
        node = NODE(None, None, value, None)
        if self.root==None:
            self.root=node

        else:
            x=self.root
            temp=None
            while x!=None:
                temp = x
                if node.key.id<x.key.id:
                    x=x.left

                else:
                    x=x.right
            node.parent=temp
            if node.key.id>temp.key.id:
                temp.right=node
            else:
                temp.left=node

        return self.root
    def searchnode(self,var,m):

            for i in range(len(lis)):
                for j in g:
                    if j.id==m.key:
                        break
            if j.id==m.key:
                if m.key==var.key.id:
                    return var
                if m.key < var.key.id:
                        return bst.searchnode(var.left,m)
                if m.key > var.key.id:
                        return bst.searchnode(var.right,m)
            else:
                return None


    def deleteleafnode(self,var,id):
        d = bst.searchnode(var,id)
        global rk
        if d==None:
            global t
            t=1
            print("ID NOT PRESENT \n")
        else:
            if d.left==None and d.right==None:
                if d.parent.left==None:
                    rk = d.parent.right.key
                    d.parent.right=None
                elif d.parent.right==None:
                    rk = d.parent.left.key
                    d.parent.left=None
                else:
                    if d.parent.left.key==d.key:
                        rk=d.parent.left.key
                        d.parent.left=None
                    else:
                        rk = d.parent.right.key
                        d.parent.right=None

            else:
                global lef
                lef=1
                print("ID IS NOT A LEAF NODE  \n")
    def printnode(self,var):
            p=2
            lz=[var]
            l1=[var]
            while l1:
                l2 = []
                for n in l1:
                        if n.left!=None:
                            l2.append(n.left)
                        if n.right!=None:
                            l2.append(n.right)
                l1 = l2
                lz.append(l2)
            print("Level", 1, ":-\t",var.key.id,"\n")
            for i in lz[1:len(lz)-1]:
                print("Level", +p, ":-\t",end='')
                for j in i:
                    print(j.key.id,"\t", end='')
                p+=1
                print("\n")


bst = BST(None)
g=lis.copy()
s=0
rk=0
while True:
    print("Select Your Option\n"
          "1-insert,\n"
                  "2-Search,\n"
                  "3-Delete,\n"
                   "4-Print by level\n"
                   "5-exit")
    ans = int(input())
    if ans == 1:
        lis=g.copy()
        q = 0
        bst = BST(None)
        print("Enter one of the below id  as root node \n")
        for m in lis:
            print(m.id,end=' , ')
        print("\n")
        r=int(input())
        for i in lis:
            if r==i.id:
                y=i
                lis.pop(lis.index(i))
            else:
                q+=1
        while q==len(lis):
            q=0
            r=int(input("Root object Not present,Reenter with any one of the roots given above \n"))
            for i in lis:
                if r == i.id:
                    y = i
                    lis.pop(lis.index(i))
                else:
                    q += 1
        s = bst.insertnode(y)
        for j in lis:
            s=bst.insertnode(j)
    elif ans==2:
        if s==0:
            print("TREE IS EMPTY\n")
        else:
             a=int(input("enter the id you want to search\n"))
             A=NODE(None,None,a,None)
             w=bst.searchnode(s,A)
             if w==None:
                 print("ID NOT PRESENT IN TREE \n")
             else:
                 w.key.printinfo()
    elif ans==3:
        if s==0:
            print("TREE IS EMPTY\n")
        else:
            h = int(input("enter the node you want to delete\n"))
            h = NODE(None, None, h, None)
            lef = t = 0
            bst.deleteleafnode(s,h)
            try:
                g.pop(g.index(rk))
            except:
                pass

            if t!=1 and lef==0:
                bst.printnode(s)

    elif ans==4:
        if s==0:
            print("TREE IS EMPTY \n")
        else:
            bst.printnode(s)
    elif ans==5:
        break
    else:
        print("enter a valid input")