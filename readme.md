# 🧙‍♀️🔮 CrystalBall 🌙✨
[🏹🦊🌳](https://drive.google.com/file/d/1gcFXBOl8DrdIpi9OSPMYztMWRxu9gxHe/view?usp=drivesdk)


CrystalBall combines the power of divination and question-answering using Hugging Face's NLP (Natural Language Processing) LLM (Large Language Models). Unlock the secrets hidden within your documents and receive answers to your questions using the wisdom of CrystalBall.

## 🧪Installation 🔬
Create and activate a virtual environment:

```shell
python3 -m venv myenv
source myenv/bin/activate
```

Install the required dependencies:

```shell
pip3 install -r requirements.txt
```

## ✨Usage🔮

Prepare your document:

Ensure your document is in the desired format (e.g., text or Markdown).
Store your document in a suitable location.
Seek answers from CrystalBall:

Create an instance of the CrystalBall class.
Use the read_document() method to provide the document path.
Invoke the answer_question() method with your question.
Experience the wisdom and insights of CrystalBall.
Sample code:

```python
from crystal_ball import CrystalBall

crystal_ball = CrystalBall()
crystal_ball.read_document('path/to/document.txt')

question = "What is the main theme of the document?"
answers = crystal_ball.answer_question(question)

for answer in answers:
    print("Answer:", answer['answer'])
    print("Score:", answer['score'])
    print()
```

May the magic of CrystalBall guide you on your quest for knowledge and insights! ✨🔮🌙
