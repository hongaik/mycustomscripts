#This script is a simulation of the Secretary Problem.

#imagine an administrator who wants to hire the best secretary out of n rankable applicants for a position. The applicants are interviewed one by 
#one in random order. A decision about each particular applicant is to be made immediately after the interview. Once rejected, an applicant 
#cannot be recalled. During the interview, the administrator gains information sufficient to rank the applicant among all applicants interviewed 
#so far, but is unaware of the quality of yet unseen applicants. The question isabout the optimal strategy (stopping rule) to maximize the 
#probability of selecting the best applicant. The difficulty is that the decision must be made immediately.

#The optimal stopping rule prescribes always rejecting the first applicants that are interviewed and then stopping at the first applicant who is 
#better than every applicant interviewed so far (or continuing to the last applicant if this never occurs). This rule is simple and selects 
#the single best candidate about 37% of the time, irrespective of whether there are 100 or 100 million applicants.

import random, math

def secretary_space(num_applicants, num_simulations):
    counter = 0
    for i in range(num_simulations):
        
        stop = round(num_applicants/math.exp(1))
        candidates = list(range(num_applicants))

        first_rej = random.sample(candidates, stop)
        remaining = [i for i in candidates if i not in first_rej]
        
        while len(remaining) > 0:
            cand = random.choice(remaining)
            if cand > max(first_rej):
                if cand == num_applicants-1:
                    counter += 1
                break
            else:
                remaining.remove(cand)
                first_rej.append(cand)
    return counter/num_simulations

print(secretary_space(100, 100000))

    
       


    