from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.write("main page info tornado!")


class HomeIndexHandler(RequestHandler):
    def get(self):
        def funcSum(a, b):
            return a + b

        self.render("home.html", func=funcSum)


class CartHandler(RequestHandler):
    def get(self):
        self.render("cart.html")


# 数据库
class StudentsHandler(RequestHandler):
    def get(self):
        # 先整个数据试试
        stus = [
            {"name": "张三", "age": 21, "sex": "man"},
            {"name": "李四", "age": 23, "sex": "woman"},
            {"name": "赵六", "age": 22, "sex": "woman"},
            {"name": "田七", "age": 17, "sex": "woman"},
            {"name": "王五", "age": 19, "sex": "woman"},
        ]


        #
        # # sql语句
        # sql = "select name,age from students"
        # # 去数据库中提取数据
        # stus = self.application.db.get_all_obj(sql, "students","name","age")

        # print(stus)
        # 打印出来的结果
        # 数据库里面的数据是这样的
        '''
        [
            {'name': '张三', 'age': 15, 'sex': '男'}, 
            {'name': '李四', 'age': 18, 'sex': '女'},
            {'name': '赵柳', 'age': 24, 'sex': '男'},
            {'name': '知乎', 'age': 19, 'sex': '男'},
            {'name': 'Nancy', 'age': 21, 'sex': '女'},
            {'name': '小强', 'age': 23, 'sex': '未知'}
         ]
        '''
        # 这个get_all_obj挺好用的了,你还可以用这个get_all
        # 只不过这个get_all返回的是元组类型的数据,
        # 不太方便你在这个前台页面的遍历和展示

        # 插入一条数据
        ins_sql = "insert into students values('Nancy',22,'gril')"
        stus = self.application.db.insert(ins_sql)
        print(stus)
        self.render("students.html", stus=stus)
