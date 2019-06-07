# properties : ClaimID, ClaimType, Description, ClaimAmount, DateOfIncident, DateOfClaim, IsValid
# allows claim to be made up to 30 days : is valid test
# Claim type could be : Car, Home, Theft
# methods: 1. see all claims 2. take care of next claim 3. enter a new claim
# see all claims should be dictionary that 
import datetime

class Claim:
    def __init__(self, ClaimID, ClaimType, Description, ClaimAmount,year, month, day):
        self.ClaimID = ClaimID
        
        self.ClaimType = ClaimType
        self.Description = Description
        self.ClaimAmount = ClaimAmount
        self.year = year
        self.month = month
        self.day = day
        self.DateOfIncident = datetime.date(year, month, day)
        self.DateOfClaim = datetime.date.today()
        delta = self.DateOfIncident - self.DateOfClaim
        days = str(delta).split(' ')[0]
        if int(days)> 30:
            self.IsValid = True
        else:
            self.IsValid = False
        
    def __repr__(self):
        return f'{self.ClaimID} \n{self.ClaimType} \n{self.Description} \n{self.ClaimAmount} \n{self.DateOfIncident} \n{self.DateOfClaim} \n{self.IsValid}'


class ClaimRepository:
    def __init__(self):
        self.claim_list = []
    
    def see_claims(self):
        return self.claim_list

    def add_claim(self, ClaimID, ClaimType, Description, ClaimAmount, year, month, day):
        new_claim = Claim(ClaimID, ClaimType, Description, ClaimAmount, year, month, day)
        self.claim_list.append(new_claim)
        

    def __repr__(self):
        return f'Claim ID: {self.claim_list}'
    
    
    def finish_claim(self, ClaimID):
        claim_to_remove = self._check_for_claim(ClaimID)
        if claim_to_remove:
            self.claim_list.remove(claim_to_remove)
            return True
        else:
            return False

    def _check_for_claim(self, ClaimID):
        for i in self.claim_list:
            if i.ClaimID == ClaimID:
                return i
        return None


    #cr.add_claim()
    #all_calims = cr.see_claims()
    #for i in all_claims:
    #    print(i)
    #def valid_chec(self):
    #    if self.Inc_Claim_Dif > 30:
    #        if self.Inc_Claim_Dif < 0:
    #            self.claimdic.update({'IsValid': False})
    #    else:
    #        self.claimdic.update({'IsValid' : True})
                
            
#claim1 = Claim(1, 'home','boat accident',400,'March 20','March 21')
#print(claim1.valid_test())
