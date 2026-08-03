def submit_report(inc, d, p, e):
    if inc not in ['lost id','room issue','lab equipment damage','bullying'] and e in ['no']:
        return "Rejected"
    elif inc in ['lost id','room issue','lab equipment damage','bullying'] and p in ['high'] and e in ['yes']:
        return "For Review."
    elif inc in ['lost id','room issue','lab equipment damage','bullying'] and p in ['low','medium'] and e in ['yes']:
        return "On Progress."
    else:
        return "Needs revision"

id = []
n = []
i = []
pr = []
dess = []
ea = []
cs = []

assigned = 0
while True:
    print("\n === STUDENT INCIDENT REPORT MANAGEMENT SYSTEM === \n1. Submit a new report \n2. Review all submitted reports \n3. Update report status \n4. Count reports by status \n5. Exit ")
    menu = input("Enter your choice: ")

    if menu == "1":
        print('\n=== SUBMIT NEW REPORT ===')
        name = input("Enter reporter name: ").strip()
        incident = input("\nEnter incident type (lost id / room issue / lab equipment damage / bullying): \n").strip()
        prio = input("\nEnter priority (low / medium / high): \n").strip()
        des = input("\nEnter incident description: \n").strip()
        evidence = input("\nIs there evidence attached? (yes/no): \n").strip()

        result = submit_report(incident, des, prio, evidence)
        if result == "Rejected":
            print('Report submitted successfully.\nAssigned Report ID: 0\nCurrent Status:',result)
        elif result == "For Review.":
            assigned +=1
            id.append(assigned)
            n.append(name)
            i.append(incident)
            pr.append(prio)
            dess.append(des)

            if evidence in ['yes']:
                ea.append("True")
            else:
                ea.append("False")

            cs.append(result)
            print('Report submitted successfully.\nAssigned Report ID: ',assigned,'\nCurrent Status:',result)
        elif result == "On Progress.":
            assigned +=1
            id.append(assigned)
            n.append(name)
            i.append(incident)
            pr.append(prio)
            dess.append(des)

            if evidence in ['yes']:
                ea.append("True")
            else:
                ea.append("False")

            cs.append(result)
            print('Report submitted successfully.\nAssigned Report ID: ',assigned,'\nCurrent Status:',result)
        elif result == "Needs revision":
            assigned +=1
            id.append(assigned)
            n.append(name)
            i.append(incident)
            pr.append(prio)
            dess.append(des)

            if evidence in ['yes']:
                ea.append("True")
            else:
                ea.append("False")

            cs.append(result)
            print('Report submitted successfully.\nAssigned Report ID: ',assigned,'\nCurrent Status:',result)
        else:
            print('Report Invalid.\nAssigned Report ID: Invalid\nCurrent Status: Invalid')
    
    if menu == "2":
        print("\n=== ALL SUBMITTED REPORTS === ")
        for ass in range(assigned):
            print('\nReport ID:',id[ass])
            print('Reporter Name:',n[ass])
            print('Incident Type:',i[ass])
            print('Priority:',pr[ass])
            print('Description:',dess[ass])
            print('Evidence Attached:',ea[ass])
            print('Current Status:',cs[ass])
    else:
        print()