# Prompt the user to enter a username
print("Please enter the username :")

# Loop until a valid username is entered
while True:
    username = input()  # Get input from the user
    # Check if the username length is between 1 and 8 characters
    if 1 <= len(username) <= 8:
        break  # Exit the loop if the username is valid
    else:
        print("Incorrect Username, Please enter again :")  # Prompt for re-entry if invalid

# Prompt the user to enter a password
print("Please enter the password:")

# Loop until a valid password is entered
while True:
    password = input()  # Get input from the user
    # Check if the password length is between 8 and 256 characters
    if 8 <= len(password) <= 256:
        break  # Exit the loop if the password is valid
    else:
        print("Incorrect Password, Please enter again :")  # Prompt for re-entry if invalid

# Define constants for BSOD error code validation
BSODErrorDigit = "0x"  # The prefix that BSOD error codes start with
bsod_error_length = 10  # Expected length of a valid BSOD error code

# Prompt the user to enter a BSOD error code
print("Please enter your BSOD error: ")

# Loop until a valid BSOD error code is entered
while True:
    user_bsoderror = input()  # Get input from the user
    # Check if the input starts with '0x'
    if user_bsoderror[:2] == BSODErrorDigit:
        count_bsoderror = len(user_bsoderror)  # Get length of the entered error code
        # Check if the length matches the expected BSOD error code length
        if count_bsoderror == bsod_error_length:
            break  # Exit the loop if valid
        else:
            print("BSOD error code invalid, please enter your BSOD error code again :")  # Prompt for re-entry if invalid
    else:
        print("BSOD error code invalid please enter your BSOD error code again :")  # Prompt for re-entry if invalid

# Dictionary mapping BSOD error codes to their Official Names, The Meaning of the BSOD error, And the cause of the BSOD error code
bsod_errors = {
	"0x00000050": "PAGE_FAULT_IN_NONPAGED_AREA, Meaning: This error occurs when a system process attempts to access a page of memory that is not present in the system's memory. Causes: Often linked to defective RAM, corrupted drivers, or issues with the hard drive.",
	"0x0000001A": "MEMORY_MANAGEMENT, Meaning: Indicates that there is a problem with the memory management system. Causes: Usually results from faulty RAM or issues with drivers that manage memory.",
	"0x0000003B": "SYSTEM_SERVICE_EXCEPTION, Meaning: This error suggests that an exception occurred while executing a routine that runs at a higher IRQL (Interrupt Request Level). Causes: Can be caused by corrupted drivers, incompatible software, or malware infections.",
	"0x00000001": "APC_INDEX_MISMATCH, Meaning:  indicates a synchronization issue in Windows, causing system crashes and preventing normal startup. Cause: The APC_INDEX_MISMATCH error (0x1) typically arises from mismatched asynchronous procedure calls (APCs) in drivers or file systems",
	"0x00000002": "DEVICE_QUEUE_NOT_BUSY, Meaning: indicates a system issue, often due to driver problems or corrupted files, leading to potential system instability. Cause : incompatible software or hardware issues, often linked to driver problems or recent changes.",
	"0x0000000A": "IRQL_NOT_LESS_OR_EQUAL, Meaning: This error indicates that a driver or system process attempted to access memory that it was not allowed to. Cause: Typically caused by faulty drivers, incompatible software, or hardware issues such as malfunctioning RAM.",
    "0x0000007E": "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED, Meaning: This error indicates that a system thread used to manage tasks encountered a problem that it couldn't handle correctly. Cause: Typically caused by a Fault in a driver or Function within Windows that caused this error.",
    "0x000000EF": "CRITICAL_PROCESS_DIED, Meaning: This error indicates a critical system process terminated. Cause: This error typically occurs when a system process required by Windows is corrupted and needs to be reinstalled or updated.",
    "0x0000001E": "KMODE_EXCEPTION_NOT_HANDLED, Meaning: This error indicates that there was an error in a low-level component of the Windows machine. Cause: This error could have potentially been caused by faulty RAM in the Windows machine, or a corrupted driver.",
    "0x00000117": "VIDEO_TDR_TIMEOUT_DETECTED, Meaning: The error indicates that a driver used to display a video on the screen has failed to respond to a command given by the Windows machine. Cause: This error is usually set off by an issue in the drivers of the computer, or an overheating issue within the physical system.",
    "0x0000002E": "DATA_BUS_ERROR, Meaning: This error indicates that there was an error within the RAM that is alerting the user that data isn't being stored correctly. Cause: This error is caused by a physical issue within the RAM of the system or potentially a faulty driver.",
    "0x0000003B": "SYSTEM_SERVICE_EXCEPTION, Meaning: The computer didn't have the privileges required for a system-critical process. Cause: This error is typically caused by a Faulty or Corrupted driver that changed the privilege requirements, or malware that changed the admin code leading to this error.",
    "0x00000133": "DPC_WATCHDOG_VIOLATION, Meaning: This error indicates there was an error within the system clock of the system. Cause: This error is usually caused by a Driver conflict where there are multiple installations of a driver doing similar routines.",
    "0x00000024": "NTFS_FILE_SYSTEM, Meaning: There is an error in a file called ntfs.sys, which allows the system to read and write onto the disk. Cause: This is caused by the NTFS file system which is primarily caused by corruption or a malfunction.",
    "0x00000139": "KERNEL_SECURITY_CHECK_FAILURE, Meaning: This error indicates that the kernel has detected the corruption of a critical data structure. Cause: This is caused by an error within the drivers which set off the error, or a problem with the physical RAM leading to an incorrect memory allocation."
	}

# Print the description of the entered BSOD error code
print(bsod_errors[user_bsoderror])

# Define commands for disk cleanup operations
diskcleanup = "(sfc /scannow) and (chkdsk c:/r)"
print("Enter these commands into CMD:", diskcleanup)  # Instruct user on what to input into windows Command Prompt

# Dictionary mapping BSOD error codes to Windows Command prompt Commands to attempt to correct the bsod error code
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

# Print the command associated with the entered BSOD error code
print("Enter these commands into CMD:", bsod_error_script[user_bsoderror])
