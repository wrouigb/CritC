#Prompts For Username and Verify it meets the criteria
print("Please enter the username :")
while True:
    username = input()
    if 1 <= len(username) <= 8:
        break
    else:
        print("Incorrect Username, Please enter again :")

#Prompts For Password and Verify it meets the criteria
print("Please enter the password:")
while True:
    password = input()
    if 8 <= len(password) <= 256:
        break
    else:
        print("Incorrect Password, Please enter again :")

#Prompts For BSOD error and Verify it meets the criteria
BSODErrorDigit = "0x"
bsod_error_length = 10
# Compare the first two letters
print("Please enter your BSOD error: ")
while True:
    user_bsoderror = input()
    if user_bsoderror[:2] == BSODErrorDigit:
        count_bsoderror = len(user_bsoderror)
        if count_bsoderror == bsod_error_length:
            break
        else:
            print("BSOD error code invalid, please enter your BSOD error code again :")
    else:
        print("BSOD error code invalid please enter your BSOD error code again :")



bsod_errors = {
   "0x0000000A": "IRQL_NOT_LESS_OR_EQUAL, Meaning: This error indicates that a driver or system process attempted to access memory that it was not allowed to. Cause: Typically caused by faulty drivers, incompatible software, or hardware issues such as malfunctioning RAM.",
   "0x00000050": "PAGE_FAULT_IN_NONPAGED_AREA, Meaning: This error occurs when a system process attempts to access a page of memory that is not present in the system's memory. Causes: Often linked to defective RAM, corrupted drivers, or issues with the hard drive.",
   "0x0000001A": "MEMORY_MANAGEMENT, Meaning: Indicates that there is a problem with the memory management system. Causes: Usually results from faulty RAM or issues with drivers that manage memory.",
   "0x0000003B": "SYSTEM_SERVICE_EXCEPTION, Meaning: This error suggests that an exception occurred while executing a routine that runs at a higher IRQL (Interrupt Request Level). Causes: Can be caused by corrupted drivers, incompatible software, or malware infections."
}





# Print the corresponding message for the user-defined BSOD error code
print(bsod_errors[user_bsoderror])
bsod_error_script = {
    "0x0000000A": "verifier /standard /all",
    "0x00000050": "verifier /standard /all",
    "0x0000001A": "mdsched",
    "0x0000003B": "verifier /standard /all"
}



# Print the corresponding message for the user-defined BSOD error code
print("Enter this command into CMD:", bsod_error_script[user_bsoderror])

diskcleanup = "sfc /scannow"
print("Enter this command into CMD:", diskcleanup)