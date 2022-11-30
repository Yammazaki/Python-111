from hh import get_max_page,get_hh_jobs
from save import save_to_csv

max_page = get_max_page()
jobs = get_hh_jobs(max_page)
print(jobs)


 







#     try:
#         page_count = int(soup.find("div",attrs={"class":"bloko-gap bloko-gap_top"}).find_all("span",recursive=False)[-1].find("a").find("span").text)
#     except:
#         return
#     for page in range(page_count):
#         try:
#             data = requests.get(
#                 url=f"https://ryazan.hh.ru/search/vacancy?text={text}&area=&page={page}",
#                 headers={"user-agent":ua.random}
#             )
#             if data.status_code != 200:
#                 soup = BeautifulSoup(data.content, "lxml")
#                 for a in soup.find_all("a",attrs={"class":"serp-item__title"}):
#                     yield f'https://ryazan.hh.ru{a.attrs["href"].split("?")[0]}'
#                 print(a)
#         except Exception as e:
#             print(f"{e}")
#         time.sleep(1)
#     print(data.content)      
# get_links("python")


# def get_resume(link):
#     ua =fake_useragent.UserAgent()
#     data = requests.get(
#         url=link,
#         headers={"user-agent":ua.random}
#     )
#     if data.status_code != 200:
#         return
#     soup = BeautifulSoup(data.content, "lxml")
#     try:
#         name = soup.find(attrs={"class":"vacancy-block__title-text"}).text
#     except:
#         name = ""
#     try:
#         salary = soup.find(attrs={"class":"vacancy-block__title-text_salary"}).text.replace("\u2009","").replace("\xa0"," ")
#     except:
#         salary = ""
#     try:
#         tags = [tag.text for tag in soup.find(attrs={"class":"bloko-tag-list"}).find_all("span",attrs={"class":"bloko-tag__section_text"})]
#     except:
#         tags = []
#     vacancy = {
#         "name":name,
#         "salary":salary,
#         "tags":tags,
#     }
#     return vacancy

# def download_data(tag, filename):
#     data = []
#     for a in get_links(tag):
#         data.append(get_resume(a))
#         time.sleep(1)
#         with open(filename,"w",encoding="utf-8")as f:
#             json.dump(data,f,indent = 4, ensure_ascii=False)

# def read_data(filename):
#     with open(filename, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#     return data

# def get_skills(data, freq):
#     skills = {}
#     dataCount = 0
#     for d in data:
#         if not d:
#             continue
#         dataCount += 1
#         for tag in d.get("tags", []):
#             skills[tag] = skills.get(tag, 0) + 1
    
#     skills = {k: v / dataCount for k, v in skills.items() if v / dataCount >= freq}
#     skills_sorted = sorted(skills, key=lambda x: skills[x], reverse=True)
#     return {skill: skills[skill] for skill in skills_sorted}

# if __name__ == "__main__":
#     for a in get_links("python"):
#         print(a)
            
    # data = read_data("data.json")
    # print("PYTHON")
    # for k, v in get_skills(data, 0.1).items():
    #     print(k, v)

