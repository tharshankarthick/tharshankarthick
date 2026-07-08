import matplotlib.pyplot as pt
c,d=0,{}
while True:
    c+=1
    l1,l2=[],[]
    print(f"What are all your expense in Day {c}")
    while True:
        a,b=input("Enter name of expense: "),int(input("Enter amount of expense: "))
        l1.append(a)
        l2.append(b)
        e=input(f"Do you still need to add more expence in Day {c}(y/n): ")
        if e.lower()=="no" or e.lower()=='n':
            break
    d[f"Day {c}"]=[l1,l2]
    f=input("Do you want to add more of your expense: ")
    if f.lower()=="yes" or f.lower()=='y':
        continue
    elif f.lower()=="no" or f.lower()=='n':
        fig, ax = pt.subplots(1,2)
        ax[0].plot([i for i in d],[sum(d[i][1]) for i in d],marker=".",ms=15)
        ax[1].bar([i for i in d],[sum(d[i][1]) for i in d])
        ax[0].set_title('Expense Tracker')
        ax[0].set_xlabel('Days')
        ax[0].set_ylabel('Expense in ₹')
        ax[1].set_title('Expense Tracker')
        ax[1].set_xlabel('Days')
        ax[1].set_ylabel('Expense in ₹')
        pt.show()
        break
    else:
        print("Enter valid option (y/n)")
        f=input("Do you want to add more of your expense: ")
