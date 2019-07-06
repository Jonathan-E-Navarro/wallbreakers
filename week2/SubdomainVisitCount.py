class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        table = dict()
        results = []
        for domain in cpdomains:
            parted =  domain.split()
            num = parted[0]
            domains = parted[1].split('.')
            
            for idx in range(len(domains)):
                subdomain = ".".join(domains[idx:]) 
                if subdomain not in table:
                    table[subdomain] = int(num)
                else:
                    table[subdomain] += int(num)
                    
        for domain,count in table.items():
            results.append(str(count)+" "+domain)
                    
        return results
            
            