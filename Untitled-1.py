
def calculate_tax(building_area, num_floors):
    tax_amounts=[]
    
    for i in range(len(building_area)):
        area = building_area[i]
        floors = num_floors[i]
        
        if area <= 1000:
            tax_amount = area * 1 * (floors + 1)  
        else:
            tax_amount = area * 1.50 * (floors + 1)  
        
        tax_amounts.append((i, tax_amount))
        
    return tax_amounts


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        print(key)
        j = i - 1
        while j >= 0 and arr[j][1] > key[1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    


N = 5
building_area = [500, 550, 2000, 1500, 1200]
num_floors = [0, 1, 0, 1, 0]

tax_amounts = calculate_tax(building_area, num_floors)

insertion_sort(tax_amounts)

print("House order based on tax amount collected:")
for house_index, tax_amount in tax_amounts:
    print(f"House {house_index + 1}: Tax Amount = {tax_amount} Rs")

