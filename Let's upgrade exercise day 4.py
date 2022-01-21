def new_land_function_1(Known_people,area,recently_visited,length_width,l_w_h,cost_total,cost_total_summary):
   print(f"People you know here:{(Known_people)}\nArea of land :{(area)}\nIs it visited recently :{recently_visited}\nLength & width :{(length_width)}\nWith height of boundry:{(l_w_h)}\nTotal land cost:{(cost_total)}\nSummary:{cost_total_summary}")
new_land_function_1(2,2047.5,False,[45,45.5],{45,45.5,2},({20475,362}),{"Land Levelling":"20475 @ 10/unit cost","Boundry making":"362 @ 2/unit cost"})
print("End Function_1")
def function_2(Only_dictionary):
    for i,j in Only_dictionary.items():
        print(f"This is your key : {i}, This is your value : {j}")
function_2({"Name":"Shivam","Date of birth":"21/02/2002","Address":"Ghaziabad"})
print("End Function_2")
def function_3(input1,input2,):
    print(f"this is your output in list format:{[input1,input2]}")
function_3(input("write first list item/number = "),input("write second list item/number = "))
print("End Function_3")