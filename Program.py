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
	"0x00000050": "PAGE_FAULT_IN_NONPAGED_AREA, Meaning: This error occurs when a system process attempts to access a page of memory that is not present in the system's memory. Causes: Often linked to defective RAM, corrupted drivers, or issues with the hard drive.",
	"0x0000001A": "MEMORY_MANAGEMENT, Meaning: Indicates that there is a problem with the memory management system. Causes: Usually results from faulty RAM or issues with drivers that manage memory.",
	"0x0000003B": "SYSTEM_SERVICE_EXCEPTION, Meaning: This error suggests that an exception occurred while executing a routine that runs at a higher IRQL (Interrupt Request Level). Causes: Can be caused by corrupted drivers, incompatible software, or malware infections.",
	"0x00000001": "APC_INDEX_MISMATCH, Meaning:  indicates a synchronization issue in Windows, causing system crashes and preventing normal startup. Cause: The APC_INDEX_MISMATCH error (0x1) typically arises from mismatched asynchronous procedure calls (APCs) in drivers or file systems",
	"0x00000002": "DEVICE_QUEUE_NOT_BUSY, Meaning: indicates a system issue, often due to driver problems or corrupted files, leading to potential system instability. Cause : incompatible software or hardware issues, often linked to driver problems or recent changes.",
	"0x0000000A": "IRQL_NOT_LESS_OR_EQUAL, Meaning: This error indicates that a driver or system process attempted to access memory that it was not allowed to. Cause: Typically caused by faulty drivers, incompatible software, or hardware issues such as malfunctioning RAM.",
    "0x0000007E": "",
    "0x000000EF": "",
    "0x0000001E": "",
    "0x00000117": "",
    "0x0000002E": "",
    "0x0000003B": "",
    "0x00000133": "",
    "0x00000024": "",
    "0x00000139": ""
	}

#Print the corresponding message for the user-defined BSOD error code
print(bsod_errors[user_bsoderror])

diskcleanup = "(sfc /scannow) and (chkdsk c:/r)"
print("Enter these commands into CMD:", diskcleanup)


bsod_error_script = {
"0x0000000A":   "Enter This Command into Command Prompt, (verifier /standard /all)",
"0x00000050":	"Enter This Command into Command Prompt, (DISM.exe /Online /Cleanup-image /Restorehealth)",
"0x0000001A":	"Enter This Command into Command Prompt, (msconfig)",
"0x0000003B":	"Enter This Command into Command Prompt, (DISM.exe /Online /Cleanup-image /Restorehealth)",
"0x00000001":	"Enter These Commands one by one into Command Prompt, (bootrec /fixmbr), then (bootrec /fixboot), then  (bootrec /rebuildbcd)",
"0x00000002":	"Enter These Commands one by one into Command Prompt, (DISM.exe /Online /Cleanup-image /Scanhealth), then (DISM.exe /Online /Cleanup-image /Checkhealth), then   (DISM.exe /Online /Cleanup-image /Restorehealth)",
"0x0000007E":	"(DISM /Online /Cleanup-image /Restorehealth)",
"0x000000EF":	"(DISM /Online /Cleanup-Image /RestoreHealth)",
"0x0000001E":	"(DISM /Online /Cleanup-Image /RestoreHealth)",
"0x00000117":	"(bcdedit /enum all), them (bcdedit /deletevalue {badmemory} badmemorylist",
"0x0000002E":	"Enter These Commands one by one into Command Prompt, (DISM.exe /Online /Cleanup-image /Scanhealth), then (DISM.exe /Online /Cleanup-image /Checkhealth), then   (DISM.exe /Online /Cleanup-image /Restorehealth)",
"0x0000003B":	"(DISM /Online /Cleanup-Image /RestoreHealth), then (bootrec /fixmbr), then (bootrec /fixboot), then  (bootrec /scanos), then (bootrec /rebuildbcd)",
"0x00000133":	"(wmic baseboard get product,Manufacturer,version,serialnumber)",
"0x00000024":	"(verifier)",
"0x00000139":	"(DISM /Online /Cleanup-Image /RestoreHealth)"
}



#Print the corresponding message for the user-defined BSOD error code
print(bsod_error_script[user_bsoderror])
