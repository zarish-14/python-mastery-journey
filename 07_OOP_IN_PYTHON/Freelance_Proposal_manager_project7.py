class Proposal:
    def __init__(self,client_name=None,platform=None,budget=None,
                 proposal_status=None):
        self.client_name=client_name
        self.platform=platform
        self.budget=budget
        self.proposal_status=proposal_status
    def display_proposal(self):
        print("Client Name:     ",self.client_name)
        print("Platform:        ",self.platform)
        print("Budget:          ",self.budget)
        print("Status:          ",self.proposal_status)
    def update_status(self):
        print("Change the status:\n Pending, Accepted , Rejected")
        new_status=input("Enter status=")
        self.proposal_status=new_status
    def update_budget(self):
        print("Update Budget")
        new_budget=input("Enter new amount=")
        self.budget=new_budget
class ProposalManager():
    def __init__(self):
        self.proposals=[]
    def add_proposal(self,proposal_status="Pending" ):
        print("\n" + "-" * 40)
        print("      ADD NEW PROPOSAL")
        print("-" * 40)
        self.client_name=input("Enter client name=")
        self.platform=input("Enter platform=")
        self.budget=input("Enter budget=")
        p1=Proposal(self.client_name,self.platform,self.budget,
                    proposal_status)
        self.proposals.append(p1)
        print("\n✅ Proposal added successfully!")
        
      
    def view_propsals(self):
        print("\n" + "-" * 40)
        print("      VIEW ALL PROPOSAL")
        print("-" * 40)
        for el in self.proposals:
            print(el)
            el.display_proposal()
            print("-----------------")
    def search_proposal(self):
        print("\n" + "-" * 40)
        print("      SEARCH PROPOSAL")
        print("-" * 40)
        name_to_search=input("Enter client name=")
        found=False
        for el in self.proposals:
            if el.client_name == name_to_search:
                found=True
                el.display_proposal()
        if found == False:
            print("No proposal found for this client.")
    def update_proposal_status(self):
        print("\n" + "-" * 40)
        print("      UPDATE PROPOSAL STATUS")
        print("-" * 40)
        clientname=input("Enter client name=")
        found=False;
        for el in self.proposals:
            if el.client_name == clientname:
                el.update_status()
                found=True
                print("\n✅ Status updated successfully!")
                break
        if not found:
            print("❌ Proposal not found")
    def delete_proposal(self):
        print("\n" + "-" * 40)
        print("      DELETE ANY PROPOSAL")
        print("-" * 40)
        clientname=input("Enter client name=")
        for el in self.proposals:
            if el.client_name == clientname:
                self.proposals.remove(el)
                break
        print("\n✅ Proposal deleted successfully!")
    def count_proposals(self):
        print("\n" + "-" * 40)
        print("      COUNT PROPOSAL")
        print("-" * 40)
        if len(self.proposals) == 0:
             print("No proposals available.")
             return

        total_proposals=len(self.proposals)
        print("Total proposals= ",total_proposals)
    def display_statistics(self):
        print("\n" + "-" * 40)
        print("      DISPLAY PROPOSALS STATISTICS")
        print("-" * 40)
        pending_proposals=0
        accepted_proposals=0
        rejected_proposals=0
        for el in self.proposals:
            if el.proposal_status == "Pending":
                 pending_proposals= pending_proposals+1
            elif el.proposal_status == "Accepted":
                accepted_proposals=accepted_proposals+1
            elif el.proposal_status == "Rejected":
                 rejected_proposals= rejected_proposals+1
        print("\n------ Proposal Statistics ------")
        print("Pending  :", pending_proposals)
        print("Accepted :", accepted_proposals)
        print("Rejected :", rejected_proposals)
        print("---------------------------------")

    @staticmethod
    def freelancing_tips():
        print("\n" + "-" * 40)
        print("      FREELANCING TIPS")
        print("Customize every proposal \n  Dont copy-paste.\n Always read client requirements.")
val=True
manager=ProposalManager()
while val:
    print("=" * 45)
    print("      FREELANCE PROPOSAL TRACKER")
    print("=" * 45)
    print("\n========= MENU =========")
    print("1. Add Proposal")
    print("2. Search Proposal")
    print("3. Delete Proposal")
    print("4. Proposal Statistics")
    print("5. Count Proposals")
    print("6. Update Status")
    print("7. View All Proposals")
    print("8. Freelancing Tips")
    print("9. Exit")
    print("=" * 24)
    choice=int(input("Enter your choice="))
    if choice==1:
        manager.add_proposal()
    elif choice ==2:
        manager.search_proposal()
    elif choice == 3:
        manager.delete_proposal()
    elif choice == 4:
        manager.display_statistics()
    elif choice == 5:
        manager.count_proposals()
    elif choice == 6:
        manager.update_proposal_status()
    elif choice == 7:
        manager.view_propsals()
    elif choice==8:
        manager.freelancing_tips()
    elif choice == 9:
        val=False
        print("\nThank you for using Freelance Proposal Tracker!")
        print("Have a productive freelancing journey.")
    else:
        print("❌ Invalid choice. Please try again.")
    


        

    

    

