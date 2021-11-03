import registration
import log


while True:
    user = input("Enter either you want to Login (l, L) or Register (r, R):  ").strip()

    if user == 'l' or user == "L":
        log.login()
    elif user == 'r' or user == "R":
        registration.registering()
    else:
        print("invalid choice")