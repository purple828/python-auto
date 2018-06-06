import peewee

#ORM6,数据库关系映射
db = peewee.SqliteDatabase("blog.db")

class Article(peewee.Model):
    title = peewee.CharField(max_length=32)
    time = peewee.CharField(max_length=32)
    author = peewee.CharField(max_length=32)
    description = peewee.TextField()
    content = peewee.TextField()

    class Meta:
        database = db

if __name__ == "__main__":
    Article.create_table()