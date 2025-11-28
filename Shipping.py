# Ground shipping
ground_flat_charge = 20.00

def ground_shipping_cost(weight):
    if weight <= 2:
        price_per_lb = 1.50
    elif weight <= 6:
        price_per_lb = 3.00
    elif weight <= 10:
        price_per_lb = 4.00
    else:
        price_per_lb = 4.75
    
    return ground_flat_charge + (price_per_lb * weight)


# Drone shipping 
def drone_shipping_cost(weight):
    if weight <= 2:
        price_per_lb = 4.50
    elif weight <= 6:
        price_per_lb = 9.00
    elif weight <= 10:
        price_per_lb = 12.00
    else:
        price_per_lb = 14.25
    
    return price_per_lb * weight


# Premium shipping
premium_shipping_cost = 125.00


# Function to find the cheapest method
def cheapest_shipping(weight):
    ground = ground_shipping_cost(weight)
    drone = drone_shipping_cost(weight)
    premium = premium_shipping_cost

    print(f"Ground Shipping: ${ground:.2f}")
    print(f"Drone Shipping:  ${drone:.2f}")
    print(f"Premium Shipping: ${premium:.2f}")
    print()

    if ground < drone and ground < premium:
        print(f"Cheapest method: Ground Shipping — ${ground:.2f}")
    elif drone < ground and drone < premium:
        print(f"Cheapest method: Drone Shipping — ${drone:.2f}")
    else:
        print(f"Cheapest method: Premium Shipping — ${premium:.2f}")



if __name__ == "__main__":
    weight = float(input("Enter package weight (lb): "))
    cheapest_shipping(weight)
