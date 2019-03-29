from library_manager import LibraryManager
accounts={}
member_id=1000



while True:
	choice = int(input("Hello, what do you want to do today\n\n\
		1. Create membership\n\
		2. Show list of books\n\
		3. Count of books\n\
		4. Borrow books\n\
		5. Return books\n"))


	if choice==1:
		account_name=input("Enter your name : ")
		pin=int(input("Enter a PIN : "))
		accounts[member_id]=LibraryManager(account_name,pin,member_id)
		print(accounts[member_id])
		print(f"Congratulations! You are now a member and your member_id is {member_id}")
		member_id +=1

		
	elif choice==2:
		member_id=eval(input("Enter your Member ID : "))
		upin=int(input("Enter your PIN : "))
		if upin==accounts[member_id].pin:
			accounts[member_id].show_list_of_books()
		else:
			print("Wrong PIN, please try again. ")


	elif choice==3:
		member_id=eval(input("Enter your Member ID : "))
		upin=eval(input("Enter your PIN : "))
		if upin==accounts[member_id].pin:
			accounts[member_id].display_count_of_books()
		
	elif choice==4:
		member_id=eval(input("Enter your Member ID : "))
		upin=eval(input("Enter your PIN : "))
		if upin==accounts[member_id].pin:
			accounts[member_id].borrow_book()

		
	elif choice==5:
		member_id=eval(input("Enter your Member ID : "))
		upin=eval(input("Enter your PIN : "))
		if upin==accounts[member_id].pin:
			accounts[member_id].return_book()
	
	else:
		break

