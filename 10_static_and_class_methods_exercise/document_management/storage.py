class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        current_category = [c for c in self.categories if category_id == c.id][0]
        current_category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        current_topic = [t for t in self.topics if topic_id == t.id][0]
        current_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        current_document = [d for d in self.documents if document_id == d.id][0]
        current_document.edit(new_file_name)

    def delete_category(self, category_id):
        self.categories.remove([c for c in self.categories if category_id == c.id][0])

    def delete_topic(self, topic_id):
        self.topics.remove([t for t in self.topics if topic_id == t.id][0])

    def delete_document(self, document_id):
        self.documents.remove([d for d in self.documents if document_id == d.id][0])

    def get_document(self, document_id):
        return [d for d in self.documents if document_id == d.id][0]

    def __repr__(self):
        return '\n'.join(str(x) for x in self.documents)

