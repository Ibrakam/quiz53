from fastapi import FastAPI
from db import Base, engine


app = FastAPI(docs_url="/", title="Project")





# User
# колонки
# username
# phone_number
# level
# reg_date

# Question
# main_question
# v1, v2, v3, v4
# timer
# correct_answer

correct_answers
level
user_id

#UserCorrectAnswers
# user_id
# question_id
# level
# user_answer
# correctnes
# timer

