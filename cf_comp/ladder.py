from .api_calls.api_func import status,problem

def gen(username,tag):
    a = status(username)
    b = tag
    z = 0
    total = 0
    di = {}
    for ques in a:
        p1 = 0
        for tag_i in ques['tags']:
            p1 += 1
            if(p1 == 4):
                break
            if(tag_i == b):
                s1 = ques['name']
                if(ques['sub_status'] != 'OK'):
                    try:
                        m=di[s1]
                    except:
                        try:
                            z += ques['problem']['rating'] - 200
                            total += 1
                        except:
                            continue
                        di[s1] = 'NO'
                        continue
                elif(ques['sub_status'] == 'OK'):
                    try:
                        m=di[s1]
                    except:
                        try:
                            z += ques['problem']['rating'] + 200
                            total += 1
                        except:
                            continue
                        di[s1] = 'OK'
                        continue
                    if(di[s1] == 'OK'):
                        continue
                        di[s1] = 'OK'
                        try:
                            z += ques['problem']['rating'] + 200
                            total += 1
                        except:
                            continue
    # return int(round(z/total,-2))
    return problem(b,z/total)
            # print(s1)
# print(gen('nikhiltotla','dp'))
# print(problem('dp',1700)[0])

