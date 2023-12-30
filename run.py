from classify import move_resize_images


# Define the original folders
car_folder = 'C:/Users/Propietario/Desktop/Dataset/Car'
truck_folder = 'C:/Users/Propietario/Desktop/Dataset/Truck'
motorbike_folder = 'C:/Users/Propietario/Desktop/Dataset/Motorcycle'
bus_folder = 'C:/Users/Propietario/Desktop/Dataset/Bus'
van_folder = 'C:/Users/Propietario/Desktop/Dataset/Van'
# Create destination folders
train_folder = 'C:/Users/Propietario/Desktop/DatasetTypeVehicle/train'
validation_folder = 'C:/Users/Propietario/Desktop/DatasetTypeVehicle/validation'
test_folder = 'C:/Users/Propietario/Desktop/DatasetTypeVehicle/test'

# Percentages
train_percentage = 0.7
validation_percentage = 0.2
test_percentage = 0.1
new_size = (200,200)

print("Start train image............................\n ")
move_resize_images(car_folder, train_folder + '/Car', train_percentage, new_size)
move_resize_images(truck_folder, train_folder + '/Truck', train_percentage, new_size)
move_resize_images(motorbike_folder, train_folder + '/Motorbike', train_percentage, new_size)
move_resize_images(bus_folder, train_folder + '/Bus', train_percentage, new_size)
move_resize_images(van_folder, train_folder + '/Van', train_percentage, new_size)
print("Start validation image............................\n ")
move_resize_images(car_folder, validation_folder + '/Car', validation_percentage, new_size)
move_resize_images(truck_folder, validation_folder + '/Truck', validation_percentage, new_size)
move_resize_images(motorbike_folder, validation_folder + '/Motorbike', validation_percentage, new_size)
move_resize_images(bus_folder, validation_folder + '/Bus', validation_percentage, new_size)
move_resize_images(van_folder, validation_folder + '/Van', validation_percentage, new_size)
print("Start test image............................\n ")
move_resize_images(car_folder, test_folder + '/Car', test_percentage, new_size)
move_resize_images(truck_folder, test_folder + '/Truck', test_percentage, new_size)
move_resize_images(motorbike_folder, test_folder + '/Motorbike', test_percentage, new_size)
move_resize_images(bus_folder, test_folder + '/Bus', test_percentage, new_size)
move_resize_images(van_folder, test_folder + '/Van', test_percentage, new_size)