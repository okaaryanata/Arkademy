import json

def soal1() :
    name = 'A.A. Gede Oka Aryanata'
    address = 'Jalan Tarakanita III no 9, Jakarta'
    hobbies = ['menonton youtube','internetan','futsal']
    is_married = False
    school = {}
    school['highSchool'] = 'SMAN 7 Denpasar'
    school['university'] = 'Telkom University'
    skills = []
    skill1 = {}
    skill2 = {}
    skill3 = {}
    skill4 = {}
    skill5 = {}
    skill6 = {}
    skill1['name'] = 'Java'
    skill1['score'] = 8
    skill2['name'] = 'Python'
    skill2['score'] = 8
    skill3['name'] = 'Golang'
    skill3['score'] = 7
    skill4['name'] = 'CSS'
    skill4['score'] = 6.5
    skill5['name'] = 'HTML'
    skill5['score'] = 7
    skill6['name'] = 'JS'
    skill6['score'] = 7
    skills.append(skill1)
    skills.append(skill2)
    skills.append(skill3)
    skills.append(skill4)
    skills.append(skill5)
    skills.append(skill6)
    data = {}
    data['name'] = name
    data['address'] = address
    data['hobbies'] = hobbies
    data['is_married'] = is_married
    data['school'] = school
    data['skills'] = skills
    json_data = json.dumps(data)
    return json_data

print(soal1())
        