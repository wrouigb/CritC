##Prompts For Username and Verify it meets the criteria
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
	"0x00000003": "INVALID_AFFINITY_SET, Meaning: indicates a system error that restricts access to your computer, often due to hardware or driver issues. Cause: is typically caused by corrupted disk drivers, hardware issues, or incompatible software.",
	"0x00000004": "INVALID_DATA_ACCESS_TRAP, Meaning: overflow trap, a critical system error that causes Windows to halt, often leading to data loss and requiring troubleshooting to resolve. Cause: often caused by corrupted system files, outdated drivers, or hardware failures.",
	"0x00000005": "INVALID_PROCESS_ATTACH_ATTEMPT, Meaning:  indicates an invalid process attachment attempt, often linked to driver issues or faulty hardware. It can lead to system crashes and instability. Cause: caused by memory access violations, often due to faulty RAM, system file errors, or driver issues.",
	"0x00000006": "INVALID_PROCESS_DETACH_ATTEMPT, Meaning: indicates a software issue, often due to a process trying to detach improperly. This can lead to system crashes or instability. Cause: arises from issues like corrupted system files or problematic driver interactions.",
	"0x00000007": "INVALID_SOFTWARE_INTERRUPT, Meaning: serious issue, often related to hardware or driver malfunctions. If encountered, it can lead to system crashes and data loss.. Cause: faulty or mismatched hardware, particularly memory issues, or hardware failures.",
	"0x00000008": "IRQL_NOT_DISPATCH_LEVEL, Meaning: Indicates a failure during exception handling, often due to hardware issues or driver conflicts. Cause: hardware memory corruption or conflicts, low disk space, or corrupted drivers.",
	"0x00000009": "IRQL_NOT_GREATER_OR_EQUAL, Meaning: linked to driver conflicts or memory problems, potentially causing system instability. Cause: caused by faulty hardware, outdated drivers, or incompatible software.",
	"0x0000000A": "IRQL_NOT_LESS_OR_EQUAL, Meaning: This error indicates that a driver or system process attempted to access memory that it was not allowed to. Cause: Typically caused by faulty drivers, incompatible software, or hardware issues such as malfunctioning RAM.",
	"0x0000000B": "NO_EXCEPTION_HANDLING_SUPPORT, Meaning: hardware issues or problematic applications, leading to system crashes. Cause:typically caused by a broken hard drive or problematic applications or Other potential causes include outdated drivers, corrupted system files, and hardware compatibility issues .",
	"0x0000000C": "MAXIMUM_WAIT_OBJECTS_EXCEEDED, Meaning: indicates the system exceeded the maximum number of wait objects, potentially causing crashes or data loss. Cause: ccurs when the system surpasses the maximum number of wait objects allowed. Causes include corrupted system files, hardware failures, malware infections, and outdated drivers .",
	"0x0000000D": "MUTEX_LEVEL_NUMBER_VIOLATION, Meaning:  a driver issue, often related to accessing invalid memory. This can lead to system instability and crashes. Cause: driver issues, often related to faulty or incompatible drivers, particularly with printers ot other potential causes include corrupted system files, malware, and incorrect system configurations.",
	"0x0000000E": "NO_USER_MODE_CONTEXT, Meaning: Corrupt Boot Configuration Data (BCD), preventing Windows from booting. This may lead to data loss and system instability.  Cause:  from corrupted system files, incorrect drive configurations, or hardware issues like undetectable drives.",
	"0x0000000F": "SPIN_LOCK_ALREADY_OWNED, Meaning: Indicates a failure in reading boot configuration data, often due to corrupted files or hardware issues. This can prevent your PC from starting properly. Cause: primarily caused by issues with the Boot Configuration Data (BCD), corrupted system files, or faulty hardware.",
}





#Print the corresponding message for the user-defined BSOD error code
print(bsod_errors[user_bsoderror])
bsod_error_script = {
"0x0000000A":"verifier /standard /all",
"0x00000050":	"verifier /standard /all",
"0x0000001A":	"mdsched",
"0x0000003B":	"verifier /standard /all"
}



#Print the corresponding message for the user-defined BSOD error code
print("Enter this command into CMD:", bsod_error_script[user_bsoderror])

diskcleanup = "sfc /scannow"
