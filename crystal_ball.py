import re
import os 
# heroku repo:purge_cache -a guarded-chamber-72176
#os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

class CrystalBall:
    def __init__(self, model_name=None, revision=None):
        if model_name and revision:
            self.model_name = model_name
            self.revision = revision
            self.nlp = pipeline("question-answering", model=model_name, revision=revision)
        else:
            # Default model and revision if not provided
            self.model_name = "distilbert-base-cased-distilled-squad"
            self.revision = "626af31"
            self.nlp = pipeline("question-answering", model=self.model_name, revision=self.revision)

    def answer_question(self, question, document):
        result = self.nlp(question=question, context=document)
        return result['answer']
        self.document = None
        self.model_name = "distilbert-base-cased-distilled-squad"
        self.revision = "626af31"
        self.nlp = pipeline("question-answering", model=self.model_name, revision=self.revision)


    def remove_markdown_syntax(self, text):
        # Remove markdown syntax and emojis
        text = re.sub(r'\!?\[.*?\]\(.*?\)', '', text)
        text = re.sub(r'(:[^:\s]*:)', '', text)
        return text

    def read_document(self, file_path, doc_type='txt'):
        with open(file_path, 'r') as file:
            text = file.read()

        if doc_type.lower() == 'md':
            self.document = self.remove_markdown_syntax(text)
        else:
            self.document = text

    def answer_question(self, question):
        result = self.nlp(question=question, context=self.document, topk=3)
        return result

# Example usage
if __name__ == "__main__":
    #file_path = '/Users/kjams/Desktop/Jiji/README.md'
    file_path = '/Users/kjams/Desktop/Jiji/api/testing/untiycourse.md'
    question = "what language should I program in"

    crystal_ball = CrystalBall()
    crystal_ball.read_document(file_path, doc_type='md')

    answers = crystal_ball.answer_question(question)

    print("Top 3 likely answers:")
    for answer in answers:
        print("Answer:", answer['answer'])
        print("Score:", answer['score'])
        print()
