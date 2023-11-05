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

# print(rating('nikhiltotla')['result'][-1]['newRating'])
# print(rating('nikhiltotla'))