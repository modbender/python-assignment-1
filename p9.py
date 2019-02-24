def write_output():
    print("Enter transactions (Type 'exit' to exit)")
    net_amt = 0
    all_trans = []
    main_i = 1
    while True:
        trans = input("Enter trasaction string %d : "%(main_i))
        if trans.lower() == 'exit':
            if main_i == 1:
                print("No transactions done")
                return
            break
        else:
            all_trans.append(trans)
            trans = trans.split(' ')
        index=0
        try:
            for i in trans:
                if i == 'D' or i == 'd':
                    net_amt+=int(trans[index+1])
                if i == 'W' or i == 'w':
                    net_amt-=int(trans[index+1])
                index+=1
            main_i+=1
        except:
            print("Wrong transaction string format, format should be d/w followed by positive integer after a space")
    print("Transaction Log and Net Amount is :\n%s, net=%d"
        %(" ".join(trans for trans in all_trans),net_amt))
    
write_output()
