# Get user input for complex numbers
real_part_1 = float(input("Enter the real part of Complex Number 1: "))
imaginary_part_1 = float(input("Enter the imaginary part of Complex Number 1: "))
real_part_2 = float(input("Enter the real part of Complex Number 2: "))
imaginary_part_2 = float(input("Enter the imaginary part of Complex Number 2: "))

# Create complex numbers using user input
complex_num_1 = complex(real_part_1, imaginary_part_1)
complex_num_2 = complex(real_part_2, imaginary_part_2)

# Display the complex numbers
print("\nComplex Number 1:", complex_num_1)
print("Complex Number 2:", complex_num_2)

# Perform operations on complex numbers
sum_complex = complex_num_1 + complex_num_2
difference_complex = complex_num_1 - complex_num_2
product_complex = complex_num_1 * complex_num_2
quotient_complex = complex_num_1 / complex_num_2

# Display the results of operations
print("\nSum:", sum_complex)
print("Difference:", difference_complex)
print("Product:", product_complex)
print("Quotient:", quotient_complex)

# Access real and imaginary parts of a complex number
real_part_result = sum_complex.real
imaginary_part_result = sum_complex.imag

# Display real and imaginary parts of the sum
print("\nReal Part of Sum:", real_part_result)
print("Imaginary Part of Sum:", imaginary_part_result)
