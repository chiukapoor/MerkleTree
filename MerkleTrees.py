import hashlib
from collections import OrderedDict
print ("-------------------MerkleTree------------------\n")
global a
global b
global c
global d
a = raw_input("Enter the value of A: ")
b = raw_input("Enter the value of B: ")
c = raw_input("Enter the Value of C: ")
d = raw_input("Enter the value of D: ")

def company3(a,b,c,d):
        global tampered_Tree
        tampered_Tree = MerkTree()
        tampered_Tree_transaction = [a,b,c,d]
        tampered_Tree.listoftransaction = tampered_Tree_transaction
        tampered_Tree.create_tree()
        global tampered_Tree_past_transaction
        tampered_Tree_past_transaction = tampered_Tree.Get_past_transacion()
        print (' '*50+'ABCD')
        print (' '*20+'AB'+' '*58+'CD')
        print (' '*10+'A'+' '*19+'B'+' '*39+'C'+' '*18+'D')
        global comp3x
        global comp3y
        comp3x = hashlib.sha256(tampered_Tree_past_transaction[a]+tampered_Tree_past_transaction[b])
        comp3y = hashlib.sha256(tampered_Tree_past_transaction[c]+tampered_Tree_past_transaction[d])
        comp3y = comp3y.hexdigest()
        comp3x = comp3x.hexdigest()
        print ('\n\nABCD: '+tampered_Tree.Get_Root_leaf())
        print('AB:   '+comp3x)
        print('CD:   '+comp3y)
        print('A:    '+tampered_Tree_past_transaction[a])
        print('B:    '+tampered_Tree_past_transaction[b])
        print('C:    '+tampered_Tree_past_transaction[c])
        print('D:    '+tampered_Tree_past_transaction[d])
         
def company1(a,b,c,d):
        global Tree
        Tree = MerkTree()
        transaction = [a,b,c,d]
        Tree.listoftransaction = transaction
        Tree.create_tree()
        global past_transaction
        past_transaction = Tree.Get_past_transacion()
        print (' '*50+'ABCD')
        print (' '*20+'AB'+' '*58+'CD')
        print (' '*10+'A'+' '*19+'B'+' '*39+'C'+' '*18+'D')
        global comp1x
        global comp1y
        comp1x = hashlib.sha256(past_transaction[a]+past_transaction[b])
        comp1y = hashlib.sha256(past_transaction[c]+past_transaction[d])
        comp1y = comp1y.hexdigest()
        comp1x = comp1x.hexdigest()
        print ('\n\nABCD: '+Tree.Get_Root_leaf())
        print('AB:   '+comp1x)
        print('CD:   '+comp1y)
        print('A:    '+past_transaction[a])
        print('B:    '+past_transaction[b])
        print('C:    '+past_transaction[c])
        print('D:    '+past_transaction[d])

def company2(a,b,c,d):
        ground_truth_Tree = MerkTree()
        ground_truth_transaction = [a,b,c,d]
        ground_truth_Tree.listoftransaction = ground_truth_transaction
        ground_truth_Tree.create_tree()
        ground_truth_past_transaction = ground_truth_Tree.Get_past_transacion()
        ground_truth_root = ground_truth_Tree.Get_Root_leaf()
        print (' '*50+'ABCD')
        print (' '*20+'AB'+' '*58+'CD')
        print (' '*10+'A'+' '*19+'B'+' '*39+'C'+' '*18+'D')
        x = hashlib.sha256(ground_truth_past_transaction[a]+ground_truth_past_transaction[b])
        y = hashlib.sha256(ground_truth_past_transaction[c]+ground_truth_past_transaction[d])
        y = y.hexdigest()
        x = x.hexdigest()
        print ('\n\nABCD: '+ground_truth_Tree.Get_Root_leaf())
        print('AB:   '+x)
        print('CD:   '+y)
        print('A:    '+ground_truth_past_transaction[a])
        print('B:    '+ground_truth_past_transaction[b])
        print('C:    '+ground_truth_past_transaction[c])
        print('D:    '+ground_truth_past_transaction[d])

class MerkTree:

        def __init__(self,listoftransaction=None):
                self.listoftransaction = listoftransaction
                self.past_transaction = OrderedDict()

        def create_tree(self):

                
                listoftransaction = self.listoftransaction
                past_transaction = self.past_transaction
                temp_transaction = []

                for index in range(0,len(listoftransaction),2):
 
                        current = listoftransaction[index]

                        if index+1 != len(listoftransaction):
                                current_right = listoftransaction[index+1]

                        else:
                                current_right = ''

                        current_hash = hashlib.sha256(current)

                        if current_right != '':
                                current_right_hash = hashlib.sha256(current_right)
 
                        past_transaction[listoftransaction[index]] = current_hash.hexdigest()

                        if current_right != '':
                                past_transaction[listoftransaction[index+1]] = current_right_hash.hexdigest()

                        if current_right != '':
                                temp_transaction.append(current_hash.hexdigest() + current_right_hash.hexdigest())

                        else:
                                temp_transaction.append(current_hash.hexdigest())

                if len(listoftransaction) != 1:
                        self.listoftransaction = temp_transaction
                        self.past_transaction = past_transaction

                        self.create_tree()

        def Get_past_transacion(self):
                return self.past_transaction
        
        def Get_Root_leaf(self):
                last_key = self.past_transaction.keys()[-1]
                return self.past_transaction[last_key]
        
def compare(a,b):
        if(a==b):
                return 0
        else:
                print("True Value: "+a+" Altered value: "+b)

while(True):
        
        # Declare the main part of the function to run
        if __name__ == "__main__":
                print("----------------------------------------------------------")
                print ("1. Company 1\n2. Company 2\n3. Company 3\n4. Alter data of Company 3")
                x = input("Enter your choice: ")
                if(x == 1):
                        company1(a,b,c,d)
                elif(x == 2):
                        company2(a,b,c,d)
                elif(x == 3):
                        company3(a,b,c,d)
                elif(x == 4):
                        print("----------------------------------------------------------")
                        print("1. A\n2. B\n3. C\n4. D\n\n")
                        x = input ("Choose the value you want to alter: ")
                        if(x == 1):
                                at = raw_input("Enter new value of A: ")
                                print('\nAltered tree')
                                company3(at,b,c,d)
                                print('\nActual tree')
                                company1(a,b,c,d)
                                print('\n\n')
                                compare(past_transaction[a],tampered_Tree_past_transaction[at])
                        elif(x == 2):
                                bt = raw_input("Enter new value of B: ")
                                print('\nAltered tree')
                                company3(a,bt,c,d)
                                print('\nActual tree')
                                company1(a,b,c,d)
                                print('\n\n')
                                compare(past_transaction[b],tampered_Tree_past_transaction[bt])
                        elif(x == 3):
                                ct = raw_input("Enter new Value of C: ")
                                print('\nAltered tree')
                                company3(a,b,ct,d)
                                print('\nActual tree')
                                company1(a,b,c,d)
                                print('\n\n')
                                compare(past_transaction[c],tampered_Tree_past_transaction[ct])
                        elif(x == 4):
                                dt = raw_input("Enter new value of D: ")
                                print('\nAltered tree')
                                company3(a,b,c,dt)
                                print('\nActual tree')
                                company1(a,b,c,d)
                                print('\n\n')
                                compare(past_transaction[d],tampered_Tree_past_transaction[dt])
                        else:
                                print("Enter a valid number")
                        compare(comp1x,comp3x)
                        compare(comp1y,comp3y)
                        compare(Tree.Get_Root_leaf(),tampered_Tree.Get_Root_leaf())
                        break
        
                else:
                        print("Enter a valid number")
