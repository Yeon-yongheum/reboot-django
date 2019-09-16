# Django

## Model 정의

* title :  charfield
* content : textfield
* created_at : auto_now_add, datetimefield
* updated_at : auto_now, datetimefield

# CRUD

* C
  * `/new/` : 글작성 form
  * `/create/` : 저장 후 index로 보내기(redirect)
* R
  * `/1/`
* D
  * `/1/delete/` : 삭제 후 index로 보내기
* U
  * `/1/edit/` : 글 수정 form
  * `/1/update/` : 저장 후 Read로 보내기



# 2019-09-16

makemigrations 이후에

바뀌는 것을 미리 보고 싶을때 python manage.py sqlmigrate articles 0002



그냥 쉘보단 ipython 쉘이 더 편함

pip install ipython

python manage.py shell



pip install django_extensions

python manage.py shell_plus



>1. '홍길동' 이름가진 reporter1 생성
>
>2. '철수' 이름 가진 reporter2 생성
>
>3. reporter1의 article1추가
>
>   (오브젝트를 통해서)
>
>   article.reporter = reporter오브젝트
>
>4. reporter1의 article2 추가
>
>   (article_set을 통해서)
>
>5. reporter2의 article3추가
>
>   (id값을 통해서)
>
>   article.reporter_id = reporter pk(FK)
>
>6. 각 reporter 의 article들 조회
>
>   (filter?_set?)
>
>   reporter1이 가진 article 찾기
>
>   ​	reporter1.article_set.all()
>
>   ​	Article.objects.filter(reporter_id=1)
>
>   
>
>   In [17]: article3.reporter
>   Out[17]: <Reporter: Reporter object (1)>
>
>   In [18]: article3.reporter_id
>   Out[18]: 1
>
>   
>
>7. article1에 댓글 두개 추가
>
>   In [31]: article1 = Article.objects.get(pk=1)
>
>   In [32]: comment1 = Comment()
>
>   In [33]: comment1.content = '댓글댓글'
>
>   In [34]: comment1.article = article1
>
>   In [35]: comment1.save()
>
>   
>
>8. 마지막 댓글의 기사를 작성한 기자?
>
>   In [41]: comment2.article.reporter
>   Out[41]: <Reporter: Reporter object (1)>
>
>   
>
>9. 기사별 댓글 내용 출력
>
>   In [42]: articles = Article.objects.all()
>
>   In [45]: for article in articles:
>       ...:     for comment in article.comment_set.all():
>       ...:         print(comment.content)
>       ...: 
>       ...: 
>   댓글댓글
>   댓글댓글2
>
>   
>
>10. 기자별 기사 내용 출력
>
>    In [47]: reporters = Reporter.objects.all()
>
>    In [48]: for reporter in reporters:
>        ...:     for article in reporter.article_set.all():
>        ...:         print(article.content)
>        ...: 
>    내용
>    내용
>    내용
>    내용4
>
>    
>
>11. 





