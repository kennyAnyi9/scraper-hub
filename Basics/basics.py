from bs4 import BeautifulSoup

with open('scraper.html', 'r') as html_file:
    content = html_file.read()
    #print(content)
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    
    body = soup.find('body')
    div_courses = body.find_all('div', class_='course')
    
    for course in div_courses:
        course_title = course.h1.text
        course_desctiption = course.p.text
        course_price = course.a.text.split(' ')[-1]
        print(f'This course is the {course_title} course and it cost {course_price}')