import re

# Provided data of customers and products
customer_number = [40686, 49827, 37819, 10537, 73905, 18383, 27407, 78736, 18765, 90299, 58005, 88390, 20056, 14099,
                   56315, 17539, 29251, 14884, 20717, 26589, 21898, 93596, 83844, 53750, 49492, 51727, 99788, 44901,
                   48969, 63850]
customer_name = ["Carey, Drew Allison", "Butler, Geoffrey Barbara", "Burkhart, Jackie Beulah", "Sheffield, Maxwell B",
                 "Deveraux, Blanche E", "Ricardo, Lucy Esmeralda", "Mosby, Ted Evelyn", "Montgomery, Dharma F",
                 "Addams, Wednesday Friday", "Scott, Michael Gary", "Fonzarelli, Arthur H", "Torres, Callie Iphigenia",
                 "Simpson, Bart Jojo", "Sisko, Benjamin L", "Hofstadter, Leonard L", "Norton, Edward Lilywhite",
                 "Costanza, George Louis", "Griffin, Peter Lowenbrau", "Burns, Frank Marion", "Lemon, Liz Miervaldis",
                 "Bing, Chadler Muriel", "Keaton, Alex P", "Petrie, Ritchie Rosebud", "Hennessey, Cate Stinky",
                 "Boyd, Woody Tiberius", "Carter, John Truman", "Douglass, Oliver Wendell", "Feeney, Shirley Wilhemina",
                 "Mulder, Fox William", "Crane, Frasier Winslow"]
customer_balance = [301652.58, 36958.5, 374105.23, 32202.08, 331741.13, 28457.42, 395649.6, 29726.1, 1796.93, 37471.83,
                    347370.39, 36620.43, 34406.58, 2907.09, 7318.02, 32680.73, 17758.06, 9146.31, 36020.05, 19911.97,
                    14724.23, 12059.91, 38900.33, 20447.64, 26802.38, 14537.16, 29255.65, 39782.92, 30949.89, 14171.2]
customer_password = ["Iz9*z$", "Eu7#*%", "Fv6&x", "Ea0#5", "Tw6!b8", "Ye4&", "Up2%)", "Rk2!F", "Ig6)Dw", "Dr3@J",
                     "Oi2^Wg", "Co7@(", "Ra4@(", "Hl3#Uk8", "Xu9!w#@", "Nf0&", "Wd9(", "Gh7*Op", "Mf2#D$", "Oj9@&",
                     "Ha3$", "Oz6^%", "Lr7@E", "Bj2#7*", "Pz3!", "Go1(", "Fe8(k*", "Jb4)%", "Ue4&", "Qy2&w("]
item_number = ["K733", "LO917", "L223", "O261", "NQ813", "TH851", "YJ467", "UN941", "WR893", "SD743", "IL993", "L761",
               "NO204", "GO642", "BC571", "TX31", "NG108", "AF977", "SA868", "A411", "YJ195", "YC871", "NN896", "D636",
               "K233", "BM608", "L982", "UO399", "Y337", "T397"]
item_description = ["Pens", "Pencils", "Markers", "Highlighters", "Paper clips", "Tape", "Rubber bands", "Erasers",
                    "Stamp pads", "Ink for stamp pads", "Spiral notebooks", "Writing pads", "Post–it® notes",
                    "Phone message pads", "Laser printer paper", "Copy paper", "Fax paper", "Graph paper",
                    "Colored paper", "Pocket notebook", "Manila file folders", "Hanging file folders", "Pocket folders",
                    "File labels", "Index dividers", "Tabs", "Letter envelopes", "Catalog envelopes",
                    "Padded envelopes", "Shipping paper"]
item_price = [12.88, 2.83, 30.38, 82.93, 99.64, 68.81, 96.08, 55.55, 9.06, 40.42, 23.08, 58.72, 18.77, 27.43, 20.17,
              67.91, 39.33, 81.6, 60.94, 44.16, 55.5, 52.09, 94.17, 67.89, 46.67, 15.33, 81.83, 63.26, 11.9, 27.05]

data = str(input())
transaction_type = data[0:2].upper()

# NC for Name change request
# NP for New password request
# CO for Customer order

if transaction_type == "NC":  # NC for Name change request
    customer_id = data[2:7]
    if int(customer_id) in customer_number:
        full_name = data[7:]
        first_name = full_name[:full_name.find(" ")]
        middle_name = full_name[full_name.find(" "):full_name.rfind(" ")]
        last_name = full_name[full_name.rfind(" ") + 1:]
        revised_name = last_name + ', ' + first_name + middle_name
        i = customer_number.index(int(customer_id))
        customer_name.remove(customer_name[i])
        (customer_name.insert(i, revised_name))
        print(customer_name)
    else:
        print("Customer number {0} is invalid.".format(customer_id))
elif transaction_type == "NP":  # NP for New password request
    customer_id = data[2:7]
    if int(customer_id) in customer_number:
        password = data[7:]
        password_is_valid = False
        length = len(password.strip())
        if length >= 6:
            if password[0].isupper() and password[0].isalpha():  # 1st is Capital
                if password[1].islower() and password[1].isalpha():  # 2nd is small
                    if password[2].isdigit():  # 3rd is digit
                        regex = re.compile('[!@#$%^&*()]')
                        if regex.search(password[3]) is not None:  # 4th is special
                            password_is_valid = True
        if password_is_valid:
            i = customer_number.index(int(customer_id))
            customer_password.remove(customer_password[i])
            customer_password.insert(i, password)
            print(customer_password)
        else:
            print("New password not secure. Request denied.")
    else:
        print("Customer number {0} is invalid.".format(customer_id))
elif transaction_type == "CO":  # CO for Customer order
    customer_id = data[2:7]
    if int(customer_id) in customer_number:
        number_of_orders = data[7]
        input_order_date = data[8:]
        month = input_order_date[:2]
        day = input_order_date[2:4]
        year = input_order_date[4:8]
        order_date = month + '/' + day + '/' + year
        j = customer_number.index(int(customer_id))
        order1 = input().upper()
        quantity_item1 = order1[:order1.find('^')]
        item_id1 = order1[order1.find('^') + 1:order1.rfind('^')]
        if item_id1 in item_number:
            i = item_number.index(item_id1)
            price_item1 = item_price[i]
            total_price_item1 = price_item1 * int(quantity_item1)
            total_price_item2 = 0.0
            item_description1 = item_description[i]
            input_order_date = order1[order1.rfind('^') + 1:]
            month = input_order_date[:2]
            day = input_order_date[2:4]
            year = input_order_date[4:8]
            request_date_item1 = month + '/' + day + '/' + year
            if number_of_orders == '2':
                order2 = input().upper()
                quantity_item2 = order2[:order2.find('^')]
                item_id2 = order2[order2.find('^') + 1:order2.rfind('^')]
                if item_id2 in item_number:
                    i = item_number.index(item_id2)
                    price_item2 = item_price[i]
                    item_description2 = item_description[i]
                    total_price_item2 = price_item2 * int(quantity_item2)
                    input_order_date = order2[order2.rfind('^') + 1:]
                    month = input_order_date[:2]
                    day = input_order_date[2:4]
                    year = input_order_date[4:8]
                    request_date_item2 = month + '/' + day + '/' + year
                else:
                    print("Item number {0} is invalid".format(item_id2))
                    exit()
            print("{0:>11}{1:>15}".format("Order Date:", order_date))
            print("{0:>11}{1:>15}{2:>30}".format("Customer:", customer_number[j], customer_name[j]))
            print("")
            print("{0:6}{1:18}{2:29}{3:17}{4:9}{5:8}{6:>11}".format("Ln#", "Item #", "Item Description", "Req Date", "Qty",
                                                                   "Price", "Total"))
            print("{0:6}{1:18}{2:28}{3:10}{4:>11}{5:>11}{6:>4}{7:>10.2f}".format(" 1", item_id1, item_description1, request_date_item1,
                                                                   quantity_item1, str(price_item1),
                                                                   "$", float(total_price_item1)))
            if number_of_orders == '2':
                print("{0:6}{1:18}{2:28}{3:10}{4:>11}{5:>11}{6:>4}{7:>10.2f}".format(" 2", item_id2, item_description2,
                                                                                     request_date_item2,
                                                                                     quantity_item2, str(price_item2),
                                                                                     "$", float(total_price_item2)))
            total = total_price_item1 + total_price_item2
            print("")
            print("{0:>80}{1:>18.2f}".format("Total", float(total)))
        else:
            print("Item number {0} is invalid".format(item_id1))
    else:
        print("Customer number {0} is invalid".format(customer_id))
else:
    print("Transaction type {0} is invalid ".format(transaction_type))
