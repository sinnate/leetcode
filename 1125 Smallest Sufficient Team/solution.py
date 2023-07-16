class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(people)
        skillset= [set(people[person]) for person in range(n)]
        for p1 in range(n):
            for p2 in range(p1 + 1,n):
                if p1 != p2 and skillset[p1] > skillset[p2]:
                    skillset[p2].clear()
        avaible_p = collection.defaultdict(set)
        for p,s in enumerate(skillset):
            for skill in s:
                avaible_p[skill].add(p)
        
        result,sn = [i for i in range(n)],set(req_skills)


        def bt(i,combo):
            nonlocal result,sn
            
            if len(combo) >= len(result):
                return
            if not sn :
                result = list(combo)
                return
            if req_skills[i] not in sn :
                return bt(i+1,combo)
            
            for p in avaible_p[req_skills[i]]:
                skilln = skillset[p] & sn
                combo.append(p)
                sn -= skill
                bt(i+1,combo)
                combo.pop()
                sn |= skilln
        bt(0,[])
        return result