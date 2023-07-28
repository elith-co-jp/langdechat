from collections import Counter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.evaluation.qa import QAEvalChain

from .data.task.gpt4_with_calc.date import date_questions

DATE_QUESTIONS = date_questions()

class TastingPrompt:
    def __init__(self, prefix_prompt=None, suffix_prompt=None):
        self.suffix_prompt = suffix_prompt
        self.prompt = PromptTemplate(
            template=f"{prefix_prompt}\n"+"質問: {question}"+f"{suffix_prompt}\n回答:", 
            input_variables=["question"]
        )
        

    def run(self):
        chain = LLMChain(
            llm=OpenAI(temperature=0), 
            prompt=self.prompt
        )

        predictions = chain.apply(DATE_QUESTIONS)

        eval_chain = QAEvalChain.from_llm(
            llm=OpenAI(temperature=0)
        )

        graded_outputs = eval_chain.evaluate(
            DATE_QUESTIONS, 
            predictions, 
            question_key="question", 
            prediction_key="text"
        )


        counts = Counter(d['results'].strip() for d in graded_outputs)
        
        print(predictions)
        print(graded_outputs)
        print(f"正答数: {counts['CORRECT']}, 誤答数:{counts['INCORRECT']}")

        
