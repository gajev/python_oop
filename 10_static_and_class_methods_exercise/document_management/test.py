from document_management.category import Category
from document_management.document import Document
from document_management.storage import Storage
from document_management.topic import Topic

c = Category(1, "C")
t = Topic(1, "T", "C:\\user")
d = Document(1, 1, 1, "D")
s = Storage()



s.add_category(c)
s.delete_category(1)
print(s.categories, [])


#def test_storage_delete_topic(self):
   # self.s.add_topic(self.t)
    #self.s.delete_topic(1)
   # self.assertEqual(self.s.topics, [])