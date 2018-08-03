def main():
    Z = input()
    VOWELS = 0
    for char in Z:
        if char in 'aeiou':
            VOWELS += 1
    print(VOWELS)	
if __name__ == "__main__":
	main()
