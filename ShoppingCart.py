input1=int(input())
dict={}

for i in range(input1):
    inp=input().split()
    name,para=inp[0],inp[1]
    dict[name]=int(para)
input2=int(input())
cart=[]
for _ in range(input2):
    inp1=input().strip().split()
    if len(inp1)==1:
        if inp1[0]=='total':
            print(sum(cart))
        elif inp1[0]=='len':
            print(len(cart))
    elif len(inp1)>1:
        if inp1[0]=='add':
            cart.append(dict[inp1[1]])
            
        


