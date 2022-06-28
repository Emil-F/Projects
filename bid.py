name = input("What is your name? ")
bid = int(input("What is your bid? $"))
dict = {
    name: bid
}

end = False
while end == False:
    cont = input("Is there another bidder? 'no' or 'yes' ")
    if cont == "no":
        mux = max(dict, key=dict.get)
        values = dict.values()
        mix = max(values)
        print(f"{mux} wins with a bid of ${mix}.")
        end = True
    else:
        # clear()
        name2 = input("What is your name? ")
        bid2 = int(input("What is your bid? $"))
        dict[name2] = bid2
        print(dict)

