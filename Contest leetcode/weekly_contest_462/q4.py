# class Solution:
#     def specialPalindrome(self, n: int) -> int:

class Solution:
    def specialPalindrome(self, n: int) -> int:
        n_str = str(n)
        L_n = len(n_str)
        evens, odds = [2,4,6,8], [1,3,5,7,9]

        def even_subsets():
            r=[[]]
            for d in evens: r += [x+[d] for x in r]
            return r

        profiles_by_len = {}
        subs = even_subsets()
        for s in subs:
            if not s: continue
            length = sum(s)
            cnt = {d:d for d in s}
            profiles_by_len.setdefault(length, []).append(cnt)
        for c in odds:
            for s in subs:
                length = c + sum(s)
                cnt = {d:d for d in s}; cnt[c]=c
                profiles_by_len.setdefault(length, []).append(cnt)

        def min_pal_from_counts(cnt):
            center=None
            for d in range(1,10):
                if cnt.get(d,0)%2==1: center=d;break
            left=[]
            for d in range(1,10):
                left.append(str(d)*(cnt.get(d,0)//2))
            L="".join(left)
            return L+("" if center is None else str(center))+L[::-1]

        def min_pal_gt_bound(bound, cnt):
            L=len(bound)
            if sum(cnt.values())!=L: return None
            counts=[0]*10
            for d,c in cnt.items(): counts[d]=c
            res=[""]*L
            def dfs(i, prefix_equal):
                j=L-1-i
                if i>j:
                    s="".join(res)
                    return s if s>bound else None
                if i<j:
                    b=int(bound[i]) if prefix_equal else 0
                    for d in range(max(1,b),10):
                        if counts[d]>=2:
                            counts[d]-=2; res[i]=res[j]=str(d)
                            s=dfs(i+1, prefix_equal and d==b)
                            if s is not None: return s
                            counts[d]+=2
                    return None
                else:
                    b=int(bound[i]) if prefix_equal else 0
                    for d in range(max(1,b),10):
                        if counts[d]%2==1:
                            counts[d]-=1; res[i]=str(d)
                            s=dfs(i+1, prefix_equal and d==b)
                            counts[d]+=1
                            if s is not None: return s
                    return None
            return dfs(0, True)

        if L_n in profiles_by_len:
            best=None
            for cnt in profiles_by_len[L_n]:
                cand=min_pal_gt_bound(n_str,cnt)
                if cand is not None and (best is None or int(cand)<int(best)): best=cand
            if best is not None: return int(best)

        for length in sorted([x for x in profiles_by_len if x>L_n]):
            best=None
            for cnt in profiles_by_len[length]:
                cand=min_pal_from_counts(cnt)
                if best is None or int(cand)<int(best): best=cand
            if best is not None: return int(best)
        return -1