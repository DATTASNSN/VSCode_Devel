if __name__ == '__main__':
    records={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in records:
            records[score].append(name)
        else:records[score]=[name]
    r1=sorted(records)
    r2=sorted(records[r1[1]])
    print(*r2,sep="\n")
