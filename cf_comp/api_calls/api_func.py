import requests

def status(username):
    # username = 'nikhiltotla'
    url = 'https://codeforces.com/api/user.status?'
    response = requests.get(f'{url}handle={username}')
    if response.status_code == 200:
        user_info =response.json()
        p = []
        a = ['name','sub_status','tags','problem']
        for c1 in user_info.get('result'):
            a1 = [c1.get('problem').get('name'),c1['verdict'],c1['problem']['tags'],c1['problem']]
            p.append({ a:a1 for (a,a1) in zip(a, a1)})
        return p
    else:
        return None
def rating(username):
    # username = 'nikhiltotla'
    url = 'https://codeforces.com/api/user.rating?'
    response = requests.get(f'{url}handle={username}')
    if response.status_code == 200:
        user_info =response.json()
        # p = []
        # a = ['name','sub_status','tags','problem']
        # for c1 in user_info.get('result'):
        #     a1 = [c1.get('problem').get('name'),c1['verdict'],c1['problem']['tags'],c1['problem']]
        #     p.append({ a:a1 for (a,a1) in zip(a, a1)})
        return user_info['result'][-1]['newRating']
    else:
        return None
def problem(tag,rating):
    # username = 'nikhiltotla'
    url = 'https://codeforces.com/api/problemset.problems?'
    response = requests.get(f'{url}tags={tag}')
    if response.status_code == 200:
        user_info =response.json()
        b = []
        for c1 in user_info['result']['problems']:
            try:
                c1['rating']
            except:
                continue
            
            if(c1['rating'] == rating):
                b.append({'contest' : c1['contestId'],'index' : c1['index'], 'name' : c1['name']})
        return b
    else:
        return None

# print(rating('nikhiltotla')['result'][-1]['newRating'])
# print(rating('nikhiltotla'))
# b = []
# print(problem('dp',1700)[:10])
# print(b[:10])
